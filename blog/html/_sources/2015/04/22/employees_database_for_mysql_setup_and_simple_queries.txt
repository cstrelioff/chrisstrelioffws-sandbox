.. _MySQL employees database setup:

Employees database for MySQL, setup and simple queries
======================================================

In a recent post I covered :ref:`MySQL setup on Ubuntu 14.04`.  In this post 
I will cover downloading and setting up the `employees sample database`_ that
will be used for the example queries in this, and other posts, on my blog.  As
mentioned in the previous post, I'm using `Jump Start MySQL`_ as a guide book
for these posts-- you should check it out for more examples.  More specifically,
`Jump Start MySQL`_ uses the `sakila sample database`_ (DVD store database),
providing another set of examples with a different database.

.. more::

**1.** To get the database you can go directly to the
`launchpad download page`_ and download the latest "full" version-- 1.0.6 at
this time.  Or, to download the version I'm using from the terminal (it doesn't
seem update much, but you can check the link above for the latest). Use:

.. code-block:: bash

    $ wget https://launchpad.net/test-db/employees-db-1/1.0.6/+download/employees_db-full-1.0.6.tar.bz2

Next, we need to unpack the data and import into MySQL. Following the
`MySQL installation instructions`_ for the employees database, this starts with
(assuming you are in the directory with the downloaded archive):

.. code-block:: bash

    $ tar -xjf employees_db-full-1.0.6.tar.bz2
    $ cd employees_db/

Next we check the **employee.sql** file to make sure that the InnoDB storage
engine is selected. Look for a section of the file that looks like this::

      set storage_engine = InnoDB;
   -- set storage_engine = MyISAM;
   -- set storage_engine = Falcon;
   -- set storage_engine = PBXT;
   -- set storage_engine = Maria;

indicating that the InnoDB engine is chosen.  Next, to import the database we
do:

.. code-block:: bash

    $ mysql -u root -p -t < employees.sql

**Note:** the official instructions say to use :code:`$ mysql -t < employees.sql`
but this will give an error for most people because no user is specified and a
password is not requested. In any case, the output as the database is loaded
should look something like (excluding the request for a password)::

    +-----------------------------+
    | INFO                        |
    +-----------------------------+
    | CREATING DATABASE STRUCTURE |
    +-----------------------------+
    +------------------------+
    | INFO                   |
    +------------------------+
    | storage engine: InnoDB |
    +------------------------+
    +---------------------+
    | INFO                |
    +---------------------+
    | LOADING departments |
    +---------------------+
    +-------------------+
    | INFO              |
    +-------------------+
    | LOADING employees |
    +-------------------+
    +------------------+
    | INFO             |
    +------------------+
    | LOADING dept_emp |
    +------------------+
    +----------------------+
    | INFO                 |
    +----------------------+
    | LOADING dept_manager |
    +----------------------+
    +----------------+
    | INFO           |
    +----------------+
    | LOADING titles |
    +----------------+
    +------------------+
    | INFO             |
    +------------------+
    | LOADING salaries |
    +------------------+


Finally, for setup of this database, we can validate the database with md5
using:

.. code-block:: bash

    $ time mysql -u root -p -t < test_employees_md5.sql

The output should be something like this (hopefully), showing that all is
well::

    +----------------------+
    | INFO                 |
    +----------------------+
    | TESTING INSTALLATION |
    +----------------------+
    +--------------+------------------+----------------------------------+
    | table_name   | expected_records | expected_crc                     |
    +--------------+------------------+----------------------------------+
    | employees    |           300024 | 4ec56ab5ba37218d187cf6ab09ce1aa1 |
    | departments  |                9 | d1af5e170d2d1591d776d5638d71fc5f |
    | dept_manager |               24 | 8720e2f0853ac9096b689c14664f847e |
    | dept_emp     |           331603 | ccf6fe516f990bdaa49713fc478701b7 |
    | titles       |           443308 | bfa016c472df68e70a03facafa1bc0a8 |
    | salaries     |          2844047 | fd220654e95aea1b169624ffe3fca934 |
    +--------------+------------------+----------------------------------+
    +--------------+------------------+----------------------------------+
    | table_name   | found_records    | found_crc                        |
    +--------------+------------------+----------------------------------+
    | employees    |           300024 | 4ec56ab5ba37218d187cf6ab09ce1aa1 |
    | departments  |                9 | d1af5e170d2d1591d776d5638d71fc5f |
    | dept_manager |               24 | 8720e2f0853ac9096b689c14664f847e |
    | dept_emp     |           331603 | ccf6fe516f990bdaa49713fc478701b7 |
    | titles       |           443308 | bfa016c472df68e70a03facafa1bc0a8 |
    | salaries     |          2844047 | fd220654e95aea1b169624ffe3fca934 |
    +--------------+------------------+----------------------------------+
    +--------------+---------------+-----------+
    | table_name   | records_match | crc_match |
    +--------------+---------------+-----------+
    | employees    | OK            | ok        |
    | departments  | OK            | ok        |
    | dept_manager | OK            | ok        |
    | dept_emp     | OK            | ok        |
    | titles       | OK            | ok        |
    | salaries     | OK            | ok        |
    +--------------+---------------+-----------+
    
    real    0m18.133s
    user    0m0.000s
    sys     0m0.008s

User Account
------------

Next, we setup a user with access to the employees database so that we don't
use **root** all  of the time.  Of course we do that with the root account:

.. code-block:: bash

    $ mysql -u root -p

In MySQL we set the following permissions::

    mysql> GRANT CREATE, DROP, ALTER, INSERT, UPDATE, SELECT,
        -> DELETE, INDEX, CREATE VIEW, CREATE ROUTINE,
        -> ALTER ROUTINE, EXECUTE, TRIGGER,
        -> INDEX ON employees.* TO 'username'@'localhost';

    mysql> FLUSH PRIVILEGES;

where :code:`username` is substituted with a valid user account-- see
:ref:`MySQL setup on Ubuntu 14.04` if you need help setting up a user account.
Finally, exit from the **root** account, we'll use the **username** account
below::

    mysql> exit

Exploring the employees database
--------------------------------

Okay, now we're set to actually do some queries and explore the employees
database.  First, start-up MySQL with the **username** account:

.. code-block:: bash

    $ mysql -u username -p

Next, let's see what databases we have access to::

    mysql> SHOW DATABASES;
    +--------------------+
    | Database           |
    +--------------------+
    | information_schema |
    | employees          |
    | testdb             |
    +--------------------+
    3 rows in set (0.00 sec)

Importantly we can see the employees database along with the testdb setup in
the previous post.  To switch to the employees database and see what is there
try the following::

    mysql> USE employees;
    Reading table information for completion of table and column names
    You can turn off this feature to get a quicker startup with -A
    
    Database changed

    mysql> SHOW TABLES;
    +---------------------+
    | Tables_in_employees |
    +---------------------+
    | departments         |
    | dept_emp            |
    | dept_manager        |
    | employees           |
    | salaries            |
    | titles              |
    +---------------------+
    6 rows in set (0.00 sec)

The `employees database structure`_ is available for inspection, but we can also
access this information inside MySQL. For example, try the following to see
what makes up the employees and salaries tables::

    mysql> DESCRIBE employees;
    +------------+---------------+------+-----+---------+-------+
    | Field      | Type          | Null | Key | Default | Extra |
    +------------+---------------+------+-----+---------+-------+
    | emp_no     | int(11)       | NO   | PRI | NULL    |       |
    | birth_date | date          | NO   |     | NULL    |       |
    | first_name | varchar(14)   | NO   |     | NULL    |       |
    | last_name  | varchar(16)   | NO   |     | NULL    |       |
    | gender     | enum('M','F') | NO   |     | NULL    |       |
    | hire_date  | date          | NO   |     | NULL    |       |
    +------------+---------------+------+-----+---------+-------+
    6 rows in set (0.00 sec)
    
    mysql> DESCRIBE salaries;
    +-----------+---------+------+-----+---------+-------+
    | Field     | Type    | Null | Key | Default | Extra |
    +-----------+---------+------+-----+---------+-------+
    | emp_no    | int(11) | NO   | PRI | NULL    |       |
    | salary    | int(11) | NO   |     | NULL    |       |
    | from_date | date    | NO   | PRI | NULL    |       |
    | to_date   | date    | NO   |     | NULL    |       |
    +-----------+---------+------+-----+---------+-------+
    4 rows in set (0.00 sec)

Let's do some basic queries on the employees table. First, a very basic
:code:`SELECT` query.  I've limited to 10 items because this table is large::

    mysql> SELECT emp_no, first_name, last_name, gender 
        -> FROM employees
        -> LIMIT 10;
    +--------+------------+-----------+--------+
    | emp_no | first_name | last_name | gender |
    +--------+------------+-----------+--------+
    |  10001 | Georgi     | Facello   | M      |
    |  10002 | Bezalel    | Simmel    | F      |
    |  10003 | Parto      | Bamford   | M      |
    |  10004 | Chirstian  | Koblick   | M      |
    |  10005 | Kyoichi    | Maliniak  | M      |
    |  10006 | Anneke     | Preusig   | F      |
    |  10007 | Tzvetan    | Zielinski | F      |
    |  10008 | Saniya     | Kalloufi  | M      |
    |  10009 | Sumant     | Peac      | F      |
    |  10010 | Duangkaew  | Piveteau  | F      |
    +--------+------------+-----------+--------+
    10 rows in set (0.00 sec)

Notice that I can break the statement across lines to make it (I think) more
readable, the semicolon tells MySQL the statement is done.  Next, let's use
:code:`ORDER BY` to sort by :code:`last_name`::

    mysql> SELECT emp_no, first_name, last_name, gender
        -> FROM employees
        -> ORDER BY last_name ASC
        -> LIMIT 10;
    +--------+------------+-----------+--------+
    | emp_no | first_name | last_name | gender |
    +--------+------------+-----------+--------+
    |  17885 | Takanari   | Aamodt    | M      |
    |  19898 | Vidar      | Aamodt    | M      |
    |  17400 | Basim      | Aamodt    | F      |
    |  12982 | Sachem     | Aamodt    | F      |
    |  12516 | Sreenivas  | Aamodt    | F      |
    |  12791 | Mokhtar    | Aamodt    | M      |
    |  16572 | Matt       | Aamodt    | M      |
    |  18182 | Dekang     | Aamodt    | F      |
    |  15427 | Aluzio     | Aamodt    | M      |
    |  11761 | Bartek     | Aamodt    | M      |
    +--------+------------+-----------+--------+
    10 rows in set (0.14 sec)

We can also sort by multiple fields, like so::

    mysql> SELECT emp_no, first_name, last_name, gender
        -> FROM employees 
        -> ORDER BY last_name ASC, first_name ASC 
        -> LIMIT 10;
    +--------+------------+-----------+--------+
    | emp_no | first_name | last_name | gender |
    +--------+------------+-----------+--------+
    | 258641 | Abdelkader | Aamodt    | M      |
    | 258005 | Adhemar    | Aamodt    | F      |
    | 455773 | Aemilian   | Aamodt    | M      |
    | 436560 | Alagu      | Aamodt    | F      |
    | 266651 | Aleksander | Aamodt    | F      |
    | 487598 | Alexius    | Aamodt    | M      |
    | 216963 | Alois      | Aamodt    | M      |
    |  15427 | Aluzio     | Aamodt    | M      |
    | 100860 | Amabile    | Aamodt    | F      |
    | 107070 | Anestis    | Aamodt    | M      |
    +--------+------------+-----------+--------+
    10 rows in set (0.15 sec)

Wow! There are a lot of employees with the last name Aamodt!  Let's count them
using :code:`COUNT`::

    mysql> SELECT COUNT(emp_no)
        -> FROM employees
        -> WHERE last_name = 'Aamodt';
    +---------------+
    | count(emp_no) |
    +---------------+
    |           205 |
    +---------------+
    1 row in set (0.08 sec)
   
Hmm, how many employees are there in total?::
 
    mysql> SELECT COUNT(emp_no) 
        -> FROM employees;
    +---------------+
    | count(emp_no) |
    +---------------+
    |        300024 |
    +---------------+
    1 row in set (0.06 sec)

Okay, 205 out of 300024 is not so bad. Let's try to find the top family names
in the company (here we use :code:`AS` to rename :code:`COUNT(emp_no)` and
reference it in the :code:`ORDER BY` expression) ::

    mysql> SELECT last_name, COUNT(emp_no) AS num_emp
        -> FROM employees 
        -> GROUP BY last_name
        -> ORDER BY num_emp DESC
        -> LIMIT 10;
        
    +-----------+---------+
    | last_name | num_emp |
    +-----------+---------+
    | Baba      |     226 |
    | Gelosh    |     223 |
    | Coorg     |     223 |
    | Sudbeck   |     222 |
    | Farris    |     222 |
    | Adachi    |     221 |
    | Osgood    |     220 |
    | Masada    |     218 |
    | Mandell   |     218 |
    | Neiman    |     218 |
    +-----------+---------+
    10 rows in set (0.19 sec)

Interesting, Aamodt doesn't even make the top 10.

Okay, that's enough for this post-- try other queries on single tables and see
what you can learn about the employees database.  Next post we'll starting
looking at queries using multiple tables via :code:`JOINS`. As always,
corrections, comments and questions are welcome.

.. _employees sample database: http://dev.mysql.com/doc/employee/en/index.html
.. _employees database structure: http://dev.mysql.com/doc/employee/en/sakila-structure.html
.. _MySQL installation instructions: http://dev.mysql.com/doc/employee/en/employees-installation.html
.. _sakila sample database: http://dev.mysql.com/doc/sakila/en/index.html

.. _launchpad download page: https://launchpad.net/test-db/+download

.. _Jump Start MySQL: https://learnable.com/books/jump-start-mysql

.. author:: default
.. categories:: none
.. tags:: mysql, sql, ubuntu 14.04
.. comments::

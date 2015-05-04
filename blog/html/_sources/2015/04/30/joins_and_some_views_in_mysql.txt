JOINs, and some VIEWs, in MySQL
===============================

This is the third in a series of posts on MySQL, starting with
:ref:`MySQL setup on Ubuntu 14.04` and :ref:`MySQL employees database setup`.
The second post also covered simple queries using SELECT, LIMIT, ORDER BY, etc.
If you are starting out, you should start with these posts.  In this post I will
go over multi-table queries, using JOINs (with some help from VIEWs).  As you
might expect, I'll use the `employees sample database`_, setup in the previous
post. If that sounds like fun, or at least useful, follow along.

.. more::

Let's get started... first I use our **user account** to logon:

.. code-block:: bash

    $ mysql -u username -p

then, I switch to the **employees database** -- if you don't have these setup
look at my previous posts on these topics (links above)::

    mysql> USE employees;

Let's take a look at the tables again to remember what's in the database::

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

I'll focus on employee salaries, so let's look at these tables, as well as the
number of entries::

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
    
    mysql> SELECT COUNT(emp_no) AS NumEmployees FROM employees;
    +--------------+
    | NumEmployees |
    +--------------+
    |       300024 |
    +--------------+
    1 row in set (0.07 sec)
    
    mysql> DESCRIBE salaries;
    +-----------+---------+------+-----+---------+-------+
    | Field     | Type    | Null | Key | Default | Extra |
    +-----------+---------+------+-----+---------+-------+
    | emp_no    | int(11) | NO   | PRI | NULL    |       |
    | salary    | int(11) | NO   |     | NULL    |       |
    | from_date | date    | NO   | PRI | NULL    |       |
    | to_date   | date    | NO   |     | NULL    |       |
    +-----------+---------+------+-----+---------+-------+
    4 rows in set (0.01 sec)
    
    mysql> SELECT COUNT(emp_no) AS NumSalaries FROM salaries;
    +-------------+
    | NumSalaries |
    +-------------+
    |     2844047 |
    +-------------+
    1 row in set (0.66 sec)

Hmm, many more entries in the **salaries** table.  This table must include
a complete history with all salary levels. We can use the :code:`DISTINCT`
command to get a count of the number of unique employees in the **salaries**
table::

    mysql> SELECT COUNT(DISTINCT emp_no) AS NumSalaries FROM salaries;
    +-------------+
    | NumSalaries |
    +-------------+
    |      300024 |
    +-------------+
    1 row in set (0.67 sec)

Good, that matches with the number of employees, as expected.  However, when I
do later queries I don't want to deal with multiple salaries for each employee,
instead let's use the maximum value available. To do this I will create a
:code:`VIEW` -- a virtual table made from a query that we can use for later
queries.

A detour on VIEWs
-----------------

A :code:`VIEW` can be created with a query as follows (I'll post
just the code, without the mysql prompt, so that the statement can be copied
into a running MySQL session-- use CNTRL-SHFT-V to paste to the terminal):

.. code-block:: sql

    CREATE VIEW salaries_max AS
    SELECT 
      emp_no, MAX(salary) AS salary
    FROM
      salaries
    GROUP BY
      emp_no;

Now, if I look at the tables in the database I see the new :code:`VIEW`
**salaries_max** created above::

    mysql> SHOW TABLES;
    +---------------------+
    | Tables_in_employees |
    +---------------------+
    | departments         |
    | dept_emp            |
    | dept_manager        |
    | employees           |
    | salaries            |
    | salaries_max        |
    | titles              |
    +---------------------+
    7 rows in set (0.00 sec)

Back to JOINS
-------------

Let's try to get the names and genders of the top-10 paid employees. To do this
I need to pull from two tables.  This requires a :code:`JOIN`.  In this case,
the query is:

.. code-block:: sql

    SELECT
      msa.salary, em.emp_no, em.first_name,
      em.last_name, em.gender
    FROM
      salaries_max AS msa
      JOIN 
      employees AS em
    ON 
      msa.emp_no = em.emp_no
    ORDER BY
      msa.salary DESC
    LIMIT 10;

resulting in::

    +--------+--------+------------+-----------+--------+
    | salary | emp_no | first_name | last_name | gender |
    +--------+--------+------------+-----------+--------+
    | 158220 |  43624 | Tokuyasu   | Pesch     | M      |
    | 156286 | 254466 | Honesty    | Mukaidono | M      |
    | 155709 |  47978 | Xiahua     | Whitcomb  | M      |
    | 155513 | 253939 | Sanjai     | Luders    | M      |
    | 155377 | 109334 | Tsutomu    | Alameldin | M      |
    | 154459 |  80823 | Willard    | Baca      | M      |
    | 154376 | 493158 | Lidong     | Meriste   | M      |
    | 153715 | 205000 | Charmane   | Griswold  | M      |
    | 152710 | 266526 | Weijing    | Chenoweth | F      |
    | 152687 | 237542 | Weicheng   | Hatcliff  | F      |
    +--------+--------+------------+-----------+--------+
    10 rows in set (0.92 sec)

Let's point out the essential features of this query:

* In the :code:`SELECT` portion of the query I must specify the source tables,
  here I use **msa** and **em**-- these are aliases defined later in the query.

* The :code:`FROM` portion of the query uses :code:`AS`  to alias (give short
  names) to the source tables and specify the :code:`JOIN` -- in this case I
  use an :code:`INNER JOIN`. I'll go over the different type below.

* The :code:`ON` statement specifies the field used to :code:`JOIN` the tables.
  In this case I use the unique employee number **emp_no**.

* The :code:`ORDER BY` and :code:`LIMIT` serve the same purpose as we've seen
  with single-table queries in previous posts-- to sort and limit the number of
  records returned.

So, that's the basics of a :code:`JOIN`. **Note:** If I *had not* constructed
our new :code:`VIEW`, I would get the following (notice that I use the
**salaries** table instead of **salaries_max** view):

.. code-block:: sql

    SELECT
      sa.salary, em.emp_no, em.first_name,
      em.last_name, em.gender
    FROM
      salaries AS sa
      JOIN 
      employees AS em
    ON 
      sa.emp_no = em.emp_no
    ORDER BY
      sa.salary DESC
    LIMIT 10;

resulting in::

    +--------+--------+------------+-----------+--------+
    | salary | emp_no | first_name | last_name | gender |
    +--------+--------+------------+-----------+--------+
    | 158220 |  43624 | Tokuyasu   | Pesch     | M      |
    | 157821 |  43624 | Tokuyasu   | Pesch     | M      |
    | 156286 | 254466 | Honesty    | Mukaidono | M      |
    | 155709 |  47978 | Xiahua     | Whitcomb  | M      |
    | 155513 | 253939 | Sanjai     | Luders    | M      |
    | 155377 | 109334 | Tsutomu    | Alameldin | M      |
    | 155190 | 109334 | Tsutomu    | Alameldin | M      |
    | 154888 | 109334 | Tsutomu    | Alameldin | M      |
    | 154885 | 109334 | Tsutomu    | Alameldin | M      |
    | 154459 |  80823 | Willard    | Baca      | M      |
    +--------+--------+------------+-----------+--------+
    10 rows in set (2.05 sec)


which *has the undesirable multiple entries* for some employees.

JOINs: INNER, LEFT and RIGHT
----------------------------

Now that we have some sense of the spirit of the :code:`JOIN` from the above
example let's consider the types of JOINs available in MySQL.  A useful set of
reference pages are available at w3schools: `SQL JOIN`_, `SQL LEFT JOIN`_ and
`SQL RIGHT JOIN`_-- take a look at those for more examples. Also, as I
mentioned in previous posts, I found the new book `Jump Start MySQL`_ very clear
and helpful.

First I will create two :code:`VIEW`\s, based on the employees database, that are small
and will help show the difference between the types of :code:`JOIN`\s:

.. code-block:: sql

    CREATE VIEW small_salaries AS
    SELECT
      *
    FROM
      salaries_max 
    WHERE 
      emp_no IN (254466, 47978, 253939);

and

.. code-block:: sql

    CREATE VIEW small_employees AS
    SELECT
      emp_no, first_name, gender
    FROM
      employees
    WHERE 
      emp_no IN (254466, 47978, 237542);

After creating these :code:`VIEW`\s we can see what's in them with a simple
:code:`SELECT` ::

    mysql> SELECT * FROM small_salaries;
    +--------+--------+
    | emp_no | salary |
    +--------+--------+
    |  47978 | 155709 |
    | 253939 | 155513 |
    | 254466 | 156286 |
    +--------+--------+
    3 rows in set (0.86 sec)

    mysql> SELECT * FROM small_employees;
    +--------+------------+--------+
    | emp_no | first_name | gender |
    +--------+------------+--------+
    |  47978 | Xiahua     | M      |
    | 237542 | Weicheng   | F      |
    | 254466 | Honesty    | M      |
    +--------+------------+--------+
    3 rows in set (0.00 sec)

The import difference between these :code:`VIEW`\s is that **small_employees**
does not have **emp_no** 253939 and **small_salaries** does not have **emp_no**
237542.  This difference is by design and will allow us to see the result of
different types of :code:`JOIN`\s.

To help in *visually* understanding the :code:`JOIN`\s I will use Venn diagrams
that show the **emp_no**'s in the two :code:`VIEW`\s: 


.. image:: images/venn.svg
    :width: 500px
    :align: left
    :alt: Venn diagram for two VIEWs

From this figure we can see that **emp_no**'s 254466, 47978 and 253939 are all
in **small_salaries**-- this is indicated by the fact that all these numbers
are inside the blue circle (right). Similarly, we can see that **emp_no**'s
254466, 47978 and 237542 are in **small_employees**-- indicated by the fact
that these number are inside the green circle (left).  Because **emp_no**'s
254466 and 47978 *are inside both circles*, we know that these numbers appear
in both :code:`VIEW`\s. However, 237542 and 253939 appear in only one
:code:`VIEW` and this is visually reflected by the fact that the numbers appear
in only one of the circles, green *or* blue, not both. In the examples below,
I'll highlight regions of the Venn diagram to indicate the **emp_no**'s
returned by each of the :code:`JOIN` types.

**JOIN or INNER JOIN**

The :code:`JOIN` is an :code:`INNER JOIN` and returns rows that are in both
:code:`TABLE`\s or :code:`VIEW`\s. So, using this command:

.. code-block:: sql

    SELECT
      sem.*, ssa.*
    FROM
      small_employees AS sem
    JOIN
      small_salaries AS ssa
    ON
      sem.emp_no = ssa.emp_no;

or, this one:

.. code-block:: sql

    SELECT
      sem.*, ssa.*
    FROM
      small_employees AS sem
    INNER JOIN
      small_salaries AS ssa
    ON
      sem.emp_no = ssa.emp_no;

will produce::

    +--------+------------+--------+--------+--------+
    | emp_no | first_name | gender | emp_no | salary |
    +--------+------------+--------+--------+--------+
    |  47978 | Xiahua     | M      |  47978 | 155709 |
    | 254466 | Honesty    | M      | 254466 | 156286 |
    +--------+------------+--------+--------+--------+
    2 rows in set (1.04 sec)

In this example, only 47978 and 254466
are in both :code:`VIEW`\s so we get these rows.  Notice that the first three
columns are information from **small_employees** and the last two columns are
from **small_salaries**-- this ordering comes from the use of
:code:`SELECT sem.*, ssa.*` in both queries.  I note this here because this 
ordering is important for understanding the other :code:`JOIN`\s.

Finally, we visualize the :code:`INNER JOIN` using a Venn diagram, as introduced
above.  Here the overlap of the circles reflects the :code:`INNER JOIN` and
shows **emp_no**'s that are returned:

.. image:: images/join.svg
    :width: 500px
    :align: left
    :alt: The (INNER) JOIN


**LEFT OUTER JOIN**

Next, we try the :code:`LEFT OUTER JOIN` (or :code:`LEFT JOIN`). Both:

.. code-block:: sql

    SELECT
      sem.*, ssa.*
    FROM
      small_employees AS sem
    LEFT OUTER JOIN
      small_salaries AS ssa
    ON
      sem.emp_no = ssa.emp_no;

and:

.. code-block:: sql

    SELECT
      sem.*, ssa.*
    FROM
      small_employees AS sem
    LEFT JOIN
      small_salaries AS ssa
    ON
      sem.emp_no = ssa.emp_no;


produce::

    +--------+------------+--------+--------+--------+
    | emp_no | first_name | gender | emp_no | salary |
    +--------+------------+--------+--------+--------+
    |  47978 | Xiahua     | M      |  47978 | 155709 |
    | 237542 | Weicheng   | F      |   NULL |   NULL |
    | 254466 | Honesty    | M      | 254466 | 156286 |
    +--------+------------+--------+--------+--------+
    3 rows in set (1.05 sec)


In the :code:`LEFT JOIN` all rows in the first-- this makes it the left--
:code:`TABLE` or :code:`VIEW` are returned. In this example,
**small_employees** is the first (left) :code:`VIEW`, as defined in the
:code:`FROM` section of the query. So, all of its rows are returned. However,
the **emp_no** 237542 does not appear in the second (right) :code:`VIEW`
**small_salaries** so :code:`NULL`\s appear in the second row.  The
:code:`NULL`\s appear in the fourth and fifth columns, corresponding to the
**small_salaries** :code:`VIEW` -- this is why the column ordering is important
to remember.

Using the Venn diagram, we can show the results of the :code:`LEFT JOIN` as:

.. image:: images/left_join.svg
    :width: 500px
    :align: left
    :alt: The LEFT (OUTER) JOIN

where the highlighted **emp_no**'s are returned.

**RIGHT OUTER JOIN**

Finally, we try the :code:`RIGHT OUTER JOIN` (or :code:`RIGHT JOIN`). Again,
both:

.. code-block:: sql

    SELECT
      sem.*, ssa.*
    FROM
      small_employees AS sem
    RIGHT OUTER JOIN
      small_salaries AS ssa
    ON
      sem.emp_no = ssa.emp_no;

and:

.. code-block:: sql

    SELECT
      sem.*, ssa.*
    FROM
      small_employees AS sem
    RIGHT JOIN
      small_salaries AS ssa
    ON
      sem.emp_no = ssa.emp_no;

produce::

    +--------+------------+--------+--------+--------+
    | emp_no | first_name | gender | emp_no | salary |
    +--------+------------+--------+--------+--------+
    |  47978 | Xiahua     | M      |  47978 | 155709 |
    |   NULL | NULL       | NULL   | 253939 | 155513 |
    | 254466 | Honesty    | M      | 254466 | 156286 |
    +--------+------------+--------+--------+--------+
    3 rows in set (0.87 sec)

In this case the :code:`RIGHT JOIN` returns all rows in the right (second)
:code:`TABLE` or :code:`VIEW`.  For our example the second (right) :code:`VIEW`
is **small_salaries** so the :code:`NULL`\s appear in the first three columns,
corresponding to the **small_employees** :code:`VIEW`.  The Venn diagram nicely
visualizes the :code:`RIGHT JOIN` as:

.. image:: images/right_join.svg
    :width: 500px
    :align: left
    :alt: The RIGHT (OUTER) JOIN

Summing Up
----------

So, that's it. Hopefully :code:`JOIN`\s of all types make more sense and you
found the Venn diagrams a useful tool for visualizing the results of the
different :code:`JOIN` types.  As always, corrections, comments and questions
are welcome below.

.. _Jump Start MySQL: https://learnable.com/books/jump-start-mysql

.. _employees sample database: http://dev.mysql.com/doc/employee/en/index.html

.. _SQL JOIN: http://www.w3schools.com/sql/sql_join.asp
.. _SQL LEFT JOIN: http://www.w3schools.com/sql/sql_join_left.asp
.. _SQL RIGHT JOIN: http://www.w3schools.com/sql/sql_join_right.asp

.. author:: default
.. categories:: none
.. tags:: mysql, sql, ubuntu 14.04
.. comments::

.. _MySQL setup on Ubuntu 14.04:

Installing MySQL on Ubuntu 14.04
================================

In this post I will cover installing MySQL on Ubuntu 14.04, using the
repository available at the `mysql apt repo`_. The idea is to setup a repository
that allows our MySQL to be current-- in this case MySQL 5.6.  The
instructions I'm documenting here are derived from the above link, as well as
the nice book `Jump Start MySQL`_ (April 2015).  If this is of interest to you,
follow along and be sure checkout the resources mentioned above.

.. more::

Okay, you're still reading, so let's get started.

**1.** First we download a *deb* file that will setup the repository information
from `mysql apt repo`_-- look for the Ubuntu 14.04 download button. As noted
in `Jump Start MySQL`_, it looks like you have to login or sign up, *but you
don't*.  Just click *No thanks, just start my download* near the bottom of
the page and choose a convenient place to save the file.

Next, start the terminal and go to the save location.  To install, simply
type (your file name might be different, so adjust accordingly):

.. code-block:: bash

    $ sudo dpkg -i mysql-apt-config_0.3.3-1ubuntu14.04_all.deb

This will bring up a menu that asks which MySQL product we'd like to configure:

* We leave the selection as **Server**, the default, and hit Enter.

* Next, we select **mysql-5.6**, again the default, and hit Enter.  This takes
  us back to main menu.
  
* Finally, select **Apply** and hit Enter-- this should exit to the terminal
  with a simple *OK*.

**2.** Now that the repository is setup we can use the usual install commands:

.. code-block:: bash

    $ sudo apt-get update
    $ sudo apt-get install mysql-server

In our Ubuntu install of MySQL we will be prompted to choose a **root passsword**.
Note, just to be clear, that this root account and password apply only to the
MySQL server and not to the Ubuntu OS. As always, choose a strong password and
record it using a suitable tool.

**3.** We can check the status of the MySQL server using

.. code-block:: bash

    $ service mysql status

This should tell us the server is running.  To start and stop the server, use

.. code-block:: bash

    $ sudo service mysql start

and

.. code-block:: bash

    $ sudo service mysql stop

That's it, MySQL is up and running.


Beginnings
----------

To connect with the server, try the following, using the root password setup
above:

.. code-block:: bash

    $ mysql -u root -p
    Enter password:

The response should be something like::

    Welcome to the MySQL monitor.  Commands end with ; or \g.
    Your MySQL connection id is 3
    Server version: 5.6.24 MySQL Community Server (GPL)
    
    Copyright (c) 2000, 2015, Oracle and/or its affiliates. All rights reserved.
    
    Oracle is a registered trademark of Oracle Corporation and/or its
    affiliates. Other names may be trademarks of their respective
    owners.
    
    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
    
    mysql> 

The :code:`mysql>` prompt is where we type all of our commands. It is
conventional to use CAPS for SQL keywords like so::

    mysql> SHOW DATABASES;
    +--------------------+
    | Database           |
    +--------------------+
    | information_schema |
    | mysql              |
    | performance_schema |
    +--------------------+
    3 rows in set (0.00 sec)

These are the existing DBs after the initial install.  To exit, simply type::

    mysql> exit
    Bye

or, hit **CNTRL-D**.


User Accounts
-------------

As suggested in `Jump Start MySQL`_ it is a good idea to create user accounts
for daily use instead of using the root account.  This can be done with a
command like::

    mysql> CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';

where **username** and **password** are substituted with the desired values.
The hostname, in this case *localhost*, can also be changed if connections off
of the local machine are needed.  However, that's beyond the scope of this
post.  Finally, the new user can connect to the MySQL server using:

.. code-block:: bash

    $ mysql -u username -p

where the appropriate *username* and *password* are used.  Of course, privileges
can be granted and revoked in quite specific ways to databases, tables, etc.
Again following `Jump Start MySQL`_, a quick example of this might go:

* Create :code:`testdb` database using root account::

    mysql> CREATE DATABASE testdb;

* Enable privileges::

    mysql> GRANT CREATE, DROP, ALTER, INSERT, UPDATE, SELECT,
        -> INDEX ON testdb.* TO 'username'@'localhost';

* Flush privileges to make them active without restarting MySQL server::

     mysql> FLUSH PRIVILEGES;

With these commands, the user **username** should be able to access the new
:code:`testdb`.  To revoke some of the privileges, the command would be
something like the following::

    mysql> REVOKE CREATE, DROP, ALTER, INDEX 
        -> INDEX ON testdb.* TO 'username'@'localhost';

Of course, this would be followed by a :code:`FLUSH PRIVILIGES;` to make the
changes active.


Final Thoughts
--------------

That's all the basics. I'll be posting more on SQL, covering various topics in
the coming weeks and months, so check back.  As always, corrections, comments
and questions are welcome.

.. _mysql apt repo: http://dev.mysql.com/downloads/repo/apt/
.. _Jump Start MySQL: https://learnable.comd/books/jsmysql1/

.. author:: default
.. categories:: none
.. tags:: mysql, sql, ubuntu 14.04
.. comments::

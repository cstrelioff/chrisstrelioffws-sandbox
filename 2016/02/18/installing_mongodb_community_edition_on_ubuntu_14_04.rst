Installing MongoDB Community Edition on Ubuntu 14.04
====================================================

In this post I'll cover installing the Community Edition of MongoDB on Ubuntu
14.04 in a way that lets me use more recent versions of MongoDB than are
available using the standard :code:`$ sudo apt-get install`. If that sounds
interesting, follow along.

.. more::

To do this, I will use the instructions provided at the MongoDB site:
`Install MongoDB Community Edition`_ -- **you should check to see if there are
more recent, or diffent, instuctions** before you proceed! At the time I
installed, the process was to first get the MongoDB public GPG key:

.. code:: bash

    $ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927

Next, we create a list file that tell Ubuntu where the repositories are located--
this location depends on the version of Ubuntu being used. For **Ubuntu 14.04**,
the file is created using:

.. code:: bash

    $ echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list

Now, if you try:

.. code:: bash

    $ ls /etc/apt/sources.list.d/

you should see :code:`mongodb-org-3.2.list`. Finally, the install commands are:

.. code:: bash

    $ sudo apt-get update
    $ sudo apt-get install -y mongodb-org

The Mongo server can be started, stooped, etc using the typical commands for
this type of service.  To start, use (notice the service is called
:code:`mongod`):

.. code:: bash

    $ sudo service mongod start
    start: Job is already running: mongod

You should get an "already running" message if all went well above.  You can
also check the status using:

.. code:: bash

    $ sudo service mongod status
    mongod start/running, process 15373

and, stop is (as you might expect):

.. code:: bash

    $ sudo service mongod stop

That's it! Now, checkout the `MongoDB docs`_ for learning more about Mongo. As
always, questions, corrections and comments are welcome-- just be nice!

.. _Install MongoDB Community Edition: https://docs.mongodb.org/manual/tutorial/install-mongodb-on-ubuntu/#install-mongodb-community-edition
.. _MongoDB docs: https://docs.mongodb.org/manual/

.. author:: default
.. categories:: none
.. tags:: Ubuntu 14.04, MongoDB
.. comments::

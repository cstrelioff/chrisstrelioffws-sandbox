.. _python ubuntu 16.04:

python setup on Ubuntu 16.04
============================

In this post I will document my approach to python on Ubuntu 16.04. To be
clear, this *is not the only way to do things* and I make no claims that it is
the best strategy. However, it is useful for me to write this information down
for future reference and it might be helpful for you too-- let me know. You
can also read over my thoughts on python on Ubuntu 14.04 here-- see
:ref:`initial python setup` and :ref:`virtualenvs on ubuntu 14.04` as well as
:ref:`python3 on ubuntu 14.04`. However, be aware that some things have
changed since those posts were written. 

.. more::

First up, what are we working with? Without installing anything we already have
versions of python 2.7 and 3.5:

.. code-block:: bash

  $ python --version
  Python 2.7.12
  $ python2 --version
  Python 2.7.12
  $ python3 --version
  Python 3.5.2

So, if I just type **python** I get python 2.7+, but python 3.5+ is also
easily available. It also useful to see where these versions of python live. I
can find that using :code:`which`:

.. code-block:: bash

  $ which python2
  /usr/bin/python2
  $ which python3
  /usr/bin/python3

Keep these locations in mind for later-- I will use them to set up virtual 
environments that use different python versions.

build, python-dev and pip
-------------------------

To start I will install Ubuntu-specific packages that are python-related, or
needed to compile/link new installs. To start, I install the basic development
packages as follows:

.. code-block:: bash

  $ sudo apt-get install build-essential
  $ sudo apt-get install python-dev
  $ sudo apt-get install python3-dev

Of course, that can all be done on one line, but I want to make it clear what
is being installed. These Ubuntu installs provide gcc, make, as well as headers
for python 2 and python 3.

Next I install Ubuntu 16.04 versions of pip for both python 2 and python 3:

.. code-block:: bash

  $ sudo apt-get install python-pip
  $ sudo apt-get install python3-pip

Unfortunately, this is where things get confusing and one has to make choices
about how to approach installing python packages.  If I check on pip after
the above installs I get:

.. code-block:: bash

  $ which pip
  /usr/bin/pip
  $ which pip3
  /usr/bin/pip3

In fact, if I list pip-like things in :code:`/usr/bin/` I get

.. code-block:: bash

  $ ls /usr/bin/pip*
  /usr/bin/pip  /usr/bin/pip2  /usr/bin/pip3

So, the pip situation is like the python executables, with python 2 versions
(pip and pip2) as well as a python 3 version (pip3). If I try to list the
python packages installed I get

.. code-block:: none

  $ pip list

  -- list of python 2 packages installed --

  You are using pip version 8.1.1, however version 8.1.2 is available.
  You should consider upgrading via the 'pip install --upgrade pip' command.

The result is similar for pip3 (except more packages listed):

.. code-block:: none

  $ pip3 list

  -- list of python 3 packages installed --

  You are using pip version 8.1.1, however version 8.1.2 is available.
  You should consider upgrading via the 'pip install --upgrade pip' command.

What to do? As far as I can tell only one of the "pip"s can be updated in a
consistent way, it doesn't really matter which one, so I chose to
upgrade (the python 2 version) pip:

.. code-block:: bash

  $ pip install --user --upgrade pip

I think the Ubuntu python-pip will do a user install even if the
:code:`--user` flag is not used.  Once this is done, I make sure the path for
user installs is included by adding the following lines to end of
my **~/.bashrc** file:

.. code-block:: none

  # include .local/bin for local python scripts
  export PATH=~/.local/bin:$PATH

In order to get bash to recognize this change I can source the file:

.. code-block:: bash

  $ source ~/.bashrc

or close and re-start the terminal. Either way, inspecting pip should now
give:

.. code-block:: bash

  $ which pip
  /home/cstrelioff/.local/bin/pip
  $ which pip3
  /usr/bin/pip3
  
Now I have the updated version of pip and still have pip3 available.

strategy
--------

Now that I have the basics in place, let's talk strategy. How will I install
python packages that I need? In practice there are three options that I will
use at various times. I'll start with the short, brief overview here and go
into more detail in the sections below.

**Option 1:** Use the Ubuntu-specific packages that can be installed using

.. code-block:: bash

  $ sudo apt-get *packagename*

This has the advantage of not having to worry about dependencies, but comes at
the cost of not (always) having the most current version.

**Option 2:** Use pip to install as a user, like:

.. code-block:: bash

  $ pip install --user *packagename*

or

.. code-block:: bash

  $ pip3 install --user *packagename*

This allows me to install packages that need to be up-to-date but can be more
complicated if dependencies need to be found and installed. I will only use
this for a few packages.

**Option 3:** Use a virtual environment to have the most up-to-date python 2
or python 3 packages.  I will use this approach quite a bit.

An important note on these options-- **I only use sudo with apt-get**. The pip
installs will always be with the --user option, or in a virtual environment.
The goal here is to avoid conflict between Ubuntu-packages and pip-packages.

Let's get into the specifics of all the options with examples...

Option 1: python packages with sudo apt-get
-------------------------------------------

This is probably the safest way to install any python package on Ubuntu 16.04
because we are using code that has been designed to work with the OS package
manager. As an example, I will install the very popular pandas_ package.

For a python 2 version, I install with:

.. code-block:: bash

  $ sudo apt-get install python-pandas

and for a python 3 version, I use:

.. code-block:: bash

  $ sudo apt-get install python3-pandas

Even though I didn't install with pip, I can get information above the versions
of pandas_ installed using

.. code-block:: none

	$ pip show pandas
	---
	Metadata-Version: 1.1
	Name: pandas
	Version: 0.17.1
	Summary: Powerful data structures for data analysis, time series,and statistics
	Home-page: http://pandas.pydata.org
	Author: The PyData Development Team
	Author-email: pydata@googlegroups.com
	License: BSD
	Location: /usr/lib/python2.7/dist-packages
	Requires: python-dateutil, pytz, numpy
	Classifiers:
	  Development Status :: 5 - Production/Stable
	  Environment :: Console
	  Operating System :: OS Independent
	  Intended Audience :: Science/Research
	  Programming Language :: Python
	  Programming Language :: Python :: 2
	  Programming Language :: Python :: 3
	  Programming Language :: Python :: 2.6
	  Programming Language :: Python :: 2.7
	  Programming Language :: Python :: 3.3
	  Programming Language :: Python :: 3.4
	  Programming Language :: Python :: 3.5
	  Programming Language :: Cython
	  Topic :: Scientific/Engineering

Notice that the version is 0.17.1 and the location is
/usr/lib/python2.7/dist-packages. From this information I can see the version
is not the latest; at the time of this post the current version is 0.18.1.
Also, the location indicates the install was done with sudo apt-get
because it is not in ~/.local/lib/.

Try out the same command for the python 3 install:

.. code-block:: bash

  $ pip3 show pandas

You should get similar information with a different location. Also, the pip
warning will appear because pip3 was used.

**Note** If you are having trouble finding the name of a python package on
Ubuntu try apt-cache search, like so:

.. code-block:: bash

  $ apt-cache search pandas

You'll see for the above example both the python 2 and python 3 packages names
are found in addition to other, related items.

Option 2: pip install --user
----------------------------

This option is one that I do not use that I often. However, for
virtualenv_, virtualenvwrapper_, and tmuxp_ I like to have the latest versions
without starting up a virtual environment.  I'll install those here, using the
python 2 versions:

.. code-block:: bash

  $ pip install --user virtualenv
  $ pip install --user virtualenvwrapper
  $ pip install --user tmuxp

A couple of important things to note here:

1. I install with the --user option; **don't use "sudo pip"**.
2. I only install the python 2 version using pip.

I would keep this type of install to a minimum. Instead use virtual
environments, as described below, if you'd like to the most up-to-date versions
of a package. Or, if you'd like package that a certain to work well with Ubuntu
16.04 try Option 1, described above.

Option 3: virtualenv and virtualenvwrapper
------------------------------------------

setup
+++++

The first step for this option is to finish the setup of virtualenvwrapper_,
by making some additions to **~/.bashrc**. Again, put these at the end of the
file and *source* the file or restart the terminal:

.. code-block:: none

  # where to store our virtual envs
  export WORKON_HOME=$HOME/virtenvs
  # where projects will reside
  export PROJECT_HOME=$HOME/Projects-Active
  # where is the virtualenvwrapper.sh
  source $HOME/.local/bin/virtualenvwrapper.sh

These settings

1. Save virtual environments in the **~/virtenvs** directory,
2. Create new projects in **~/Projects-Active/new_project** directory,
3. Specify the location of the **virtualenvwrapper.sh** file-- you can find
   this with 

.. code-block:: bash

  $ which virtualenvwrapper.sh
  /home/cstrelioff/.local/bin/virtualenvwrapper.sh

Again, this is in ~/.local/bin because I installed with the --user option.

usage
+++++

Now that the basics are installed and setup I start installing the most
up-to-date version of python packages for both python 2 and python 3. The key
to make all of this work nicely is virtualenvwrapper_. To demonstrate I create
two virtual environments and install pandas in both.

.. _pandas: http://pandas.pydata.org/
.. _virtualenv: https://virtualenv.pypa.io/en/stable/
.. _virtualenvwrapper: https://virtualenvwrapper.readthedocs.io/en/latest/
.. _tmuxp: 

.. author:: default
.. categories:: none
.. tags:: python, ubuntu 16.06, pip, virtualenv, virtualenvwrapper
.. comments::

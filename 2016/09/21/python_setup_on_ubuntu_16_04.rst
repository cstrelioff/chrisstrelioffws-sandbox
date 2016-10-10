.. _python ubuntu 16.04:

python setup on Ubuntu 16.04
============================

In this post I will document my approach to python on Ubuntu 16.04. To be
clear, this *is not the only way to do things* and I make no claims that it is
the best strategy. However, it is useful for me to write this information down
for future reference. Who knows, it might be helpful for you too!? Let me know
if it is. I also love to read about other approaches, so leave comments and/or
links below.

You can also read over my thoughts on python on Ubuntu 14.04 here-- see
:ref:`initial python setup` and :ref:`virtualenvs on ubuntu 14.04` as well as
:ref:`python3 on ubuntu 14.04`. I will be using elements of those ideas in my
approach to python on 16.04. However, be aware that some things have changed
since those posts were written-- proceed with care!

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

.. code-block:: none

	$ apt-cache search pandas
	libgraxxia-java - Wrappers for doing Mathematics in Groovy
	neurodebian - neuroscience-oriented distribution - repository configuration
	neurodebian-archive-keyring - neuroscience-oriented distribution - GnuPG archive keys
	neurodebian-desktop - neuroscience-oriented distribution - desktop integration
	neurodebian-dev - neuroscience-oriented distribution - development tools
	neurodebian-popularity-contest - neuroscience-oriented distribution - popcon integration
	python-geopandas - Python tools for geographic data
	python-geopandas-doc - Documentation for the geopandas library
	python-pandas - data structures for "relational" or "labeled" data
	python-pandas-doc - documentation and examples for pandas
	python-pandas-lib - low-level implementations and bindings for pandas
	python-seaborn - statistical visualization library
	python-sklearn-pandas - Pandas integration with sklearn (Python 2)
	python3-geopandas - Python3 tools for geographic data
	python3-pandas - data structures for "relational" or "labeled" data - Python 3
	python3-pandas-lib - low-level implementations and bindings for pandas - Python 3
	python3-seaborn - statistical visualization library
	python3-sklearn-pandas - Pandas integration with sklearn (Python 3)

You'll see for the above example both the python 2 and python 3 packages names
are found, python-pandas and python3-pandas respectively, in addition to other
items.

Option 2: pip install --user
----------------------------

This option is one that I do not use that I often. However, for
virtualenv_, virtualenvwrapper_, and tmuxp_ I like to have the latest versions
without starting up a virtual environment.  I'll install those here, using the
python 2 versions:

.. code-block:: bash

  $ pip install --user virtualenv
  $ pip install --user virtualenvwrapper

and, if you like (you don't need to install tmuxp-- I use it with tmux; but
that's for a different post):

.. code-block:: bash

  $ pip install --user tmuxp

A couple of important things to note here:

1. I install with the --user option; **don't use "sudo pip"**.
2. I only install the python 2 version using pip.

I would keep this type of install to a minimum. Instead use virtual
environments, as described below, if you'd like to the most up-to-date versions
of a package. Or, if you'd like a package that is certain to work well with
Ubuntu 16.04 try Option 1, described above.

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

Again, this is in ~/.local/bin because I installed with the --user option. If
you'd like to keep the virtual environment files or project directories in a
different location just change the paths in your **~/.bashrc**.

usage
+++++

Now that the basics are installed and setup I can start installing the most
up-to-date version of python packages for both python 2 and python 3. The key
to make all of this work nicely is virtualenvwrapper_. To demonstrate I create
two virtual environments and install pandas in both.


**python 2 --**
First I create a python 2 virtual environment using the virtualenvwrapper_
tools (I will specify the python2 path even though it's not required here):

.. code-block:: none

  $ mkvirtualenv py2 -p /usr/bin/python2
  Running virtualenv with interpreter /usr/bin/python2
  New python executable in /home/cstrelioff/virtenvs/py2/bin/python2
  Also creating executable in /home/cstrelioff/virtenvs/py2/bin/python
  Installing setuptools, pip, wheel...done.
  virtualenvwrapper.user_scripts creating /home/cstrelioff/virtenvs/py2/bin/predeactivate
  virtualenvwrapper.user_scripts creating /home/cstrelioff/virtenvs/py2/bin/postdeactivate
  virtualenvwrapper.user_scripts creating /home/cstrelioff/virtenvs/py2/bin/preactivate
  virtualenvwrapper.user_scripts creating /home/cstrelioff/virtenvs/py2/bin/postactivate
  virtualenvwrapper.user_scripts creating /home/cstrelioff/virtenvs/py2/bin/get_env_details
  (py2) $

The terminal will now indicates that the py2 virtual environment is active with
a (py2). Next, let's make sure that we have the desired python and pip
versions:

.. code-block:: none

  (py2) $ python --version
  Python 2.7.12
  (py2) $ pip --version
  pip 8.1.2 from /home/cstrelioff/virtenvs/py2/local/lib/python2.7/site-packages (python 2.7)

Looks good. Next, I use pip to install pandas_. Because I am in a virtual
environment I can install without sudo and I don't need to use the --user
flag. Just do

.. code-block:: none

  (py2) $ pip install pandas
  Collecting pandas
    Downloading pandas-0.18.1-cp27-cp27mu-manylinux1_x86_64.whl (14.2MB)
      100% |████████████████████████████████| 14.2MB 88kB/s
  Collecting pytz>=2011k (from pandas)
    Using cached pytz-2016.6.1-py2.py3-none-any.whl
  Collecting python-dateutil (from pandas)
    Using cached python_dateutil-2.5.3-py2.py3-none-any.whl
  Collecting numpy>=1.7.0 (from pandas)
    Using cached numpy-1.11.1-cp27-cp27mu-manylinux1_x86_64.whl
  Collecting six>=1.5 (from python-dateutil->pandas)
    Using cached six-1.10.0-py2.py3-none-any.whl
  Installing collected packages: pytz, six, python-dateutil, numpy, pandas
  Successfully installed numpy-1.11.1 pandas-0.18.1 python-dateutil-2.5.3 pytz-2016.6.1 six-1.10.0

Look at that! pandas_, as well as dependencies, are installed and there is no
compiling-- thanks to python wheels! Also note that the current version of
pandas, 0.18.1 at the time of this post, is installed. If we use pip to see
what's in our py2 environment at this point we get:

.. code-block:: none

	(py2) $ pip list
	numpy (1.11.1)
	pandas (0.18.1)
	pip (8.1.2)
	python-dateutil (2.5.3)
	pytz (2016.6.1)
	setuptools (27.3.0)
	six (1.10.0)
	wheel (0.30.0a0)

Nice.

**python 3 --**
Next up, I do the same thing with python 3. First up, create the virtual
environment using virtualenvwrapper_:

.. code-block:: none

  (py2) $ mkvirtualenv py3 -p /usr/bin/python3
  Running virtualenv with interpreter /usr/bin/python3
  Using base prefix '/usr'
  New python executable in /home/cstrelioff/virtenvs/py3/bin/python3
  Also creating executable in /home/cstrelioff/virtenvs/py3/bin/python
  Installing setuptools, pip, wheel...done.
  virtualenvwrapper.user_scripts creating /home/cstrelioff/virtenvs/py3/bin/predeactivate
  virtualenvwrapper.user_scripts creating /home/cstrelioff/virtenvs/py3/bin/postdeactivate
  virtualenvwrapper.user_scripts creating /home/cstrelioff/virtenvs/py3/bin/preactivate
  virtualenvwrapper.user_scripts creating /home/cstrelioff/virtenvs/py3/bin/postactivate
  virtualenvwrapper.user_scripts creating /home/cstrelioff/virtenvs/py3/bin/get_env_details
  (py3) $

Notice that I run the :code:`mkvirtualenv` command while still in the py2
virtual environment and virtualenvwrapper_ is smart enough to create the
new py3 environment and switch to (py3)-- great stuff! Next, check the python
and pip versions to make sure we have what we expect:

.. code-block:: none

	(py3) $ python --version
	Python 3.5.2
	(py3) $ pip --version
	pip 8.1.2 from /home/cstrelioff/virtenvs/py3/lib/python3.5/site-packages (python 3.5)

Awesome-- notice that this is the latest pip in the python 3 environment.
Finally, let's install pandas_ (notice that I can use pip and don't need to use
pip3 here because I am in the py3 environment):

.. code-block:: none

  (py3) $ pip install pandas
  Collecting pandas
    Using cached pandas-0.18.1-cp35-cp35m-manylinux1_x86_64.whl
  Collecting pytz>=2011k (from pandas)
    Using cached pytz-2016.6.1-py2.py3-none-any.whl
  Collecting python-dateutil>=2 (from pandas)
    Using cached python_dateutil-2.5.3-py2.py3-none-any.whl
  Collecting numpy>=1.7.0 (from pandas)
    Using cached numpy-1.11.1-cp35-cp35m-manylinux1_x86_64.whl
  Collecting six>=1.5 (from python-dateutil>=2->pandas)
    Using cached six-1.10.0-py2.py3-none-any.whl
  Installing collected packages: pytz, six, python-dateutil, numpy, pandas
  Successfully installed numpy-1.11.1 pandas-0.18.1 python-dateutil-2.5.3 pytz-2016.6.1 six-1.10.0

Finally, I list what's in the environment

.. code-block:: none

  (py3) $ pip list
  numpy (1.11.1)
  pandas (0.18.1)
  pip (8.1.2)
  python-dateutil (2.5.3)
  pytz (2016.6.1)
  setuptools (27.3.0)
  six (1.10.0)
  wheel (0.30.0a0)

**workon, deactivate --**
Finally, I will provide a few ideas on how to get around virtual environments
using the virtualenvwrapper_ tools.  The main tool is :code:`workon`-- for
example try the following to get a list of available virtual environments:

.. code-block:: none

	(py3) $ workon
	py2
	py3
	(py3) $

As you can see, this lists the two environments that I created: py2 and py3. If
I want to change to the py2 environment, it is as simple as:

.. code-block:: none

	(py3) $ workon py2
	(py2) $ python --version
	Python 2.7.12

I check the python version after the change, just to make sure! To close out
the current virtual environment the command :code:`deactivate` is available:

.. code-block:: none

  (py2) $ deactivate
  $

and, workon still works to list and start any existing virtual environment.

.. code-block:: none

  $ workon
  py2
  py3

**mkvirtualenv, rmvirtualenv--**

I already used :code:`mkvirtualenv` above to create the py2 and py3 virtual
environments.  As you might guess, there is also a :code:`rmvirtualenv` that
removes an existing virtual environment. An example would go like this:

.. code-block:: none

	$ workon
	py2
	py3
	$ mkvirtualenv junk -p /usr/bin/python3
	Running virtualenv with interpreter /usr/bin/python3
	Using base prefix '/usr'
	New python executable in /home/cstrelioff/virtenvs/junk/bin/python3
	Also creating executable in /home/cstrelioff/virtenvs/junk/bin/python
	Installing setuptools, pip, wheel...done.
	virtualenvwrapper.user_scripts creating /home/cstrelioff/virtenvs/junk/bin/predeactivate
	virtualenvwrapper.user_scripts creating /home/cstrelioff/virtenvs/junk/bin/postdeactivate
	virtualenvwrapper.user_scripts creating /home/cstrelioff/virtenvs/junk/bin/preactivate
	virtualenvwrapper.user_scripts creating /home/cstrelioff/virtenvs/junk/bin/postactivate
	virtualenvwrapper.user_scripts creating /home/cstrelioff/virtenvs/junk/bin/get_env_details
	(junk) $ workon
	junk
	py2
	py3
	(junk) $ deactivate
	$ rmvirtualenv junk
	Removing junk...
	$ workon
	py2
	py3
	$

Hopefully that all makes sense-- you should try it out.

wrapping up
-----------

So that's it for this post. I know that it's a lot to read, but that's the best
overview of python (2.7+ and 3.5+) on Ubuntu 16.04 that I can give. If you find
typos or mistakes please leave a comment. Also, as I said above, I would love
to learn about other approaches-- please comment if you have one.  Just one
rule-- be nice!

.. _pandas: http://pandas.pydata.org/
.. _virtualenv: https://virtualenv.pypa.io/en/stable/
.. _virtualenvwrapper: https://virtualenvwrapper.readthedocs.io/en/latest/
.. _tmuxp: https://github.com/tony/tmuxp 

.. author:: default
.. categories:: none
.. tags:: python, ubuntu 16.04, pip, virtualenv, virtualenvwrapper
.. comments::

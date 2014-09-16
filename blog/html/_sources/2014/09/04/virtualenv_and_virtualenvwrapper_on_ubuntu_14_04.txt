.. _virtualenvs on ubuntu 14.04:

virtualenv and virtualenvwrapper on Ubuntu 14.04
================================================

In this post I'll go over my attempt to setup virtual environments for
Python development.  Most Python users probably don't want to use virtual
environments and should just set up a single user environment that works for
their needs. However, if you are working on writing one or more Python modules
or packages, these tools are geared towards creating isolated Python
environments for each project.  This is very useful for keeping track of such
things as the minimal Python requirements for each project.

.. more::

Assuming you want to proceed, my goal will is to setup and use
virtualenvwrapper_ (see `virtualenvwrapper docs`_ for more info), a set of
shell tools wrapped around the  virtualenv_ package.  Both the
`Doug Hellman post`_ and the `simonsoftware post`_ provide some motivation for
the development and use of the wrapper formulation-- in simple terms
virtualenvwrapper_ provides some shortcuts for common actions.  So, I've
decided to use the wrapped version.

Basic install
-------------

Following the `virtualenvwrapper basic install`_, the installation process is
to install virtualenv_ and virtualenvwrapper_ using pip. I have already
installed virtualenv_, as can be seen by using ``pip show``:

.. code-block:: bash

    $ pip show virtualenv
    ---
    Name: virtualenv
    Version: 1.11.6
    Location: /home/cstrelioff/.local/lib/python2.7/site-packages
    Requires:

If you need to install, the command is -- I install as a user:

.. code-blocK:: bash

    $ pip install --user virtualenv

Next, install the virtualenvwrapper_:

.. code-block:: bash

    $ pip install --user virtualenvwrapper

Now a ``pip show`` should show something like:

..  code-block:: bash

    $ pip show virtualenvwrapper
    ---
    Name: virtualenvwrapper
    Version: 4.3.1
    Location: /home/cstrelioff/.local/lib/python2.7/site-packages
    Requires: virtualenv, virtualenv-clone, stevedore

Finally, we add some information to our ``~/.bashrc`` file -- I added to the
end of the file, as usual for such things. The actual contents for you will be
different.

* I wanted my virtual environments in ``~/virtenvs/`` and I had already made
  that directory.
* I want to keep my active projects in ``~/Projects-Active/``, an existing
  directory.
* Finally, because I installed as a user, the path to my
  ``virtualenvwrapper.sh`` is in ``~/.local/bin/``, as indicated by using
  ``which``:

.. code-block:: bash

    $ which virtualenvwrapper.sh
    /home/cstrelioff/.local/bin/virtualenvwrapper.sh

Putting all of that specific information together, I added the following to
``~/.bashrc``::

    # where to store our virtual envs
    export WORKON_HOME=$HOME/virtenvs
    # where projects will reside
    export PROJECT_HOME=$HOME/Projects-Active
    # where is the virtualenvwrapper.sh
    source $HOME/.local/bin/virtualenvwrapper.sh

After saving the changes, I sourced the file to make the changes active:

.. code-block:: bash

    $ source ~/.bashrc

Working with virtualenvs
------------------------

Next up, let's figure out how to use all this-- you should also look at the
`simonsoftware post`_ for another take on this. The main command to remember
is ``workon``, as in *I'm going to work on this project*.  However, if we
try it now we get nothing:

.. code-block:: bash

    $ workon
    $

We need to make a virtual environment.  So, let's make one:

.. code-block:: bash

    $ mkvirtualenv test_env01
    New python executable in test_env01/bin/python
    Installing setuptools, pip...done.

We can use ``pip list`` to see the packages available:

.. code-block:: bash

    (test_env01)$ pip list
    argparse (1.2.1)
    pip (1.5.6)
    setuptools (3.6)
    wsgiref (0.1.2)

Notice that the command prompt has changed to include the environment name.  If
we want to install a package in this environment we use ``pip``:

.. code-block:: bash

    (test_env01)$ pip install pyaml

Now, a ``pip list`` gives:

.. code-block:: bash

    (test_env01)$ pip list
    argparse (1.2.1)
    pip (1.5.6)
    pyaml (14.05.7)
    PyYAML (3.11)
    setuptools (3.6)
    wsgiref (0.1.2)

To *deactivate* the virtual environment, we type exactly what you'd expect:

.. code-block:: bash

    (test_env01)$ deactivate
    $

and we get back to the normal command prompt.  However, now the ``workon``
command will show the virtual environment that we created:

.. code-block:: bash

    $ workon
    test_env01
    $ 

To start working on it again, simply try out the following to see everything is
there:

.. code-block:: bash

    $ workon test_env01
    (test_env01)$ pip list
    argparse (1.2.1)
    pip (1.5.6)
    pyaml (14.05.7)
    PyYAML (3.11)
    setuptools (3.6)
    wsgiref (0.1.2)
    (test_env01)$ deactivate 

Projects in virtualenvwrapper
-----------------------------

Finally, let's talk about *projects* in `virtualenvwrapper`_. This creates both
(i) a virtual environment and (ii) a project directory in the location
specified by ``PROJECT_HOME`` variable in the additions to the ``~/.bashrc``
file.  Let's try it out:

.. code-block:: bash

    $ mkproject test_project02
    New python executable in test_project02/bin/python
    Installing setuptools, pip...done.
    Creating /home/cstrelioff/Projects-Active/test_project02
    Setting project for test_project02 to
    /home/cstrelioff/Projects-Active/test_project02
    (test_project02)~/Projects-Active/test_project02$

Notice that this also creates a directory and cd's to directory-- very nice!
Now, if we try ``pip list`` we'll see only the packages for a new environmnet:

.. code-block:: bash

    (test_project02)~/Projects-Active/test_project02$ pip list
    argparse (1.2.1)
    pip (1.5.6)
    setuptools (3.6)
    wsgiref (0.1.2)

Switching between environments
------------------------------

Now we have two virtual environments setup, but only one is setup as a project.
We can see both with ``workon``:

.. code-block:: bash

    $ workon
    test_env01
    test_project02

To get a sense of how this all works, let startup ``test_env01`` and use
``pip list`` to see that PyYAML is installed:

.. code-block:: bash

    $ workon test_env01
    (test_env01)$ pip list
    argparse (1.2.1)
    pip (1.5.6)
    pyaml (14.05.7)
    PyYAML (3.11)
    setuptools (3.6)
    wsgiref (0.1.2)

Next, while in ``test_env01``, let's switch to ``test_project02`` using
``workon`` and look at the installed packages (no PyYAML):

.. code-block:: bash

    (test_env01)$ workon test_project02
    (test_project02)~/Projects-Active/test_project02$ pip list
    argparse (1.2.1)
    pip (1.5.6)
    setuptools (3.6)
    wsgiref (0.1.2)

Notice that the ``workon`` cd's to the project directory.  This happens because
we setup ``test_project02`` as a **project** and not just a **virtualenv**.  If
you use ``workon`` to switch back to ``test_env01`` there will be **no cd**
because there is no project file associated with that virtual environment.
In practice I imagine I will always use ``mkproject`` to set things up.

Cleaning up
-----------

Finally, to clean up the example above we can use ``rmvirtualenv``:

.. code-block:: bash

    $ workon
    test_env01
    test_project02
    $ rmvirtualenv test_env01
    Removing test_env01...
    $ rmvirtualenv test_project02
    Removing test_project02...
    $ workon
    $

With the final ``workon`` we can see that all of our environments are gone.
However, note that the directory created in ``PROJECT_HOME`` will not be deleted
by the above-- this is probably a good default behaviour.  You'll have to go
delete the directory (if you want).

That's it, hopefully some will find this useful post useful.  If you have
cool/better ways to use these tools leave a comment below.


.. _virtualenv: https://virtualenv.pypa.io/en/latest/virtualenv.html
.. _virtualenvwrapper: https://bitbucket.org/dhellmann/virtualenvwrapper
.. _virtualenvwrapper docs: http://virtualenvwrapper.readthedocs.org/en/latest/index.html
.. _virtualenvwrapper basic install: http://virtualenvwrapper.readthedocs.org/en/latest/install.html#basic-installation

.. _Doug Hellman post: http://doughellmann.com/2008/05/01/virtualenvwrapper.html
.. _simonsoftware post: http://simononsoftware.com/virtualenv-tutorial-part-2/

.. author:: default
.. categories:: none
.. tags:: python, virtualenv, virtualenvwrapper, my python setup
.. comments::

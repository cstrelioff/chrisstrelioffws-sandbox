Python 3.4 on Ubuntu 14.04 using virtual environments
=====================================================

In a previous post discussing :ref:`virtualenvs on Ubuntu 14.04` I talked about
using virtual environments with the default Python version-- this is Python
2.7.6 for Ubuntu 14.04.  However, both Python 2.7 and 3.4 are available on
Ubuntu 14.04.  In this post I'll go over setting up a virtual environment for
working with Python 3 code.

.. more::

To see that both versions of Python are available without additional
installations try out the following at the terminal:

.. code-block:: bash

    $ python --version
    Python 2.7.6
    $ python3 --version
    Python 3.4.0

For installing Python 3 packages, I'm going to install the ``python3-dev``
Ubuntu package using apt-get:

.. code-block:: bash

    $ sudo apt-get update
    $ sudo apt-get install python3-dev

This will require that you have sudo privileges, but the 4 packages that are
installed will be needed to install Python 3 packages using pip.

Next, I create a virtual environment for Python3 using `virtualenvwrapper`_, 
instead of `virtualenv`_, because the environment will be put in a standard
place that I have already setup and specified-- see my post on
:ref:`virtualenvs on Ubuntu 14.04` for more information on this aspect. I will
call the environment **py3** and specify that I want Python 3:

.. code-block:: bash

    $ mkvirtualenv py3 -p /usr/bin/python3
    Running virtualenv with interpreter /usr/bin/python3
    Using base prefix '/usr'
    New python executable in py3/bin/python3
    Also creating executable in py3/bin/python
    Installing setuptools, pip...done.
    (py3)$

First, notice that the prompt now indicates the name of the created virtual
environment.  Also notice that ``setuptools`` and ``pip`` are automatically
added. Next let's check the python version and use ``pip`` to see what's
installed:

.. code-block:: bash

    (py3)$ python --version
    Python 3.4.0
    (py3)$ 
    (py3)$ pip list
    pip (1.5.6)
    setuptools (3.6)
    (py3)$ 

That all looks good.  The Python version is 3.4 and only ``pip`` and
``setuptools`` are installed.

Next, let's install some packages in **py3**.  I'm working on a project that
uses both ``jinja2`` and ``pyyaml`` and I'd like to make sure that the package
works for both Python 2.7 and 3.4. **Note:** if you have not installed the
**python3-dev** Ubuntu package, as described above, the following will
*not work*.  Instead you'll get compilation errors. The reason for this is that
the code downloaded by ``pip`` needs to compile against files provided in
**python3-dev**.  Assuming, you're ready to go, the install is easy:

.. code-block:: bash

    (py3)$ pip install jinja2

    --- edited out compiling ---
    
    (py3)$ pip install pyyaml

    --- edited out compiling ---
    
    (py3)$
    (py3)$ pip list
    Jinja2 (2.7.3)
    MarkupSafe (0.23)
    pip (1.5.6)
    PyYAML (3.11)
    setuptools (3.6)

The final ``pip list`` shows that the desired Python packages, in addition to
``MarkupSafe`` that is required by ``jinja2``, are installed.

Finally, you can deactivate the environment using:

.. code-block:: bash

    (py3)$ deactivate
    $

and you're back to the normal environment and using Python 2.7.6.  The next
time the **py3** environment is needed starting it up is as simple as:

.. code-block:: bash

    $ workon py3
    (py3)$

and you're all set.

As always please leave comments, suggestions and questions...anything that will
be helpful to me or other readers.

.. _virtualenv: https://virtualenv.pypa.io/en/latest/virtualenv.html
.. _virtualenvwrapper: https://bitbucket.org/dhellmann/virtualenvwrapper
.. _virtualenvwrapper docs: http://virtualenvwrapper.readthedocs.org/en/latest/index.html
.. _virtualenvwrapper basic install: http://virtualenvwrapper.readthedocs.org/en/latest/install.html#basic-installation

.. author:: default
.. categories:: none
.. tags:: python, python 3.4, virtualenv, virtualenvwrapper, my python setup
.. comments::

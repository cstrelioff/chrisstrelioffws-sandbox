Python and YAML on Ubuntu 14.04
===============================

In this post I will cover installing PyYAML_ using Python 2.7. I've previously
covered my approach to Python package installation using **pip** in this post--
:ref:`initial python setup` so you can read there to get a sense of my
approach.

.. more::

First we install the YAML libraries for Ubuntu (apparently this is not needed
and PyYAML can be installed as pure Python, so skip this step if you like):

.. code-block:: bash

    $ sudo apt-get install libyaml-dev

Next, we install PyYAML_ for Python support:

.. code-block:: bash

    $ pip install --user PyYAML

If you installed ``libyaml-dev`` above, some compiling occurs, otherwise a pure
Python version is installed.  In either case, we can see the version of PyYAML
installed using:

.. code-block::bash

    $ pip show PyYAML
    ---
    Name: PyYAML
    Version: 3.11
    Location: /home/cstrelioff/.local/lib/python2.7/site-packages
    Requires: 

This package will both parse and render YAML as demonstrated in the
`PyYAML documentation`_ -- I show a `yaml.load` below:

.. code-block:: python

    >>> import yaml
    >>> 
    >>> print yaml.load("""
    ... field1: value1
    ... field2: value2
    ... a list:
    ...  - list item 1
    ...  - list item 2
    ... """)
    {'field2': 'value2', 'a list': ['list item 1', 'list item 2'], 'field1':
    'value1'}

That's it for now, checkout the PyYAML_ site for more.

.. _PyYAML: http://pyyaml.org/wiki/PyYAML
.. _PyYAML documentation: http://pyyaml.org/wiki/PyYAML#Documentation

.. author:: default
.. categories:: none
.. tags:: my python setup, python 2.7, yaml, pyyaml
.. comments::

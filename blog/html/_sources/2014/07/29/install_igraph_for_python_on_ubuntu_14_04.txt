Install igraph for Python on Ubuntu 14.04
=========================================

In this post I will describe installing `python-igraph`_ on Ubuntu 14.04, using
the default Python 2.7.  Previously I wrote a (long) post about how to
:ref:`initial python setup`, which provides lots of detail about how I approach
Python package installation.  In particular, I use **pip** and install as a
**user**.  Of course, you can do otherwise.

.. more::

On Ubuntut 14.04 `python-igraph`_ requires ``build-essential`` and
``python-dev``.  I detail how to install these in the **Ubuntu dependencies**
section of the :ref:`initial python setup` post.  Assuming that these
dependencies are satisfied, the install command is:

.. code-block:: bash

    $ pip install --user python-igraph

If you haven't previously compiled the c-core there will be lots of compiling.
Once done, you should get a note about successful installation, and information
about the install is available using:

.. code-block:: bash

    $ pip show python-igraph
    ---
    Name: python-igraph
    Version: 0.7
    Location: /home/cstrelioff/.local/lib/python2.7/site-packages
    Requires:

Of potential interest is the ``igraph`` start script.  This script will start
``IPython`` or ``IDLE`` (if available) and import all ``igraph`` into the main
namespace.

.. _python-igraph: http://igraph.org/python/

.. author:: default
.. categories:: none
.. tags:: python 2.7, igraph, social networks, networks, graphs
.. comments::

Install and use sphinx-bootstrap-theme on Ubuntu 14.04
======================================================

In this post I will try out the `sphinx-bootstrap-theme`_.  As the name
suggests, this project combines sphinx_, a Python documentation tool that
generates html/pdf/etc from rst files, and bootstrap_, a modern web framework
from Twitter for generating responsive websites.

.. more::

First, we install using **pip** (see my post :ref:`initial python setup` if you
are getting started with Python and installing packages on Ubuntu 14.04):

.. code-block:: bash

    $ pip install --user sphinx-bootstrap-theme

We can see where it installed (and other package information) using:

.. code-block:: bash

    $ pip show sphinx-bootstrap-theme
    ---
    Name: sphinx-bootstrap-theme
    Version: 0.4.0
    Location: /home/cstrelioff/.local/lib/python2.7/site-packages
    Requires: setuptools

First, use ``sphinx-quickstart`` to get an initial setup (I will do this in my
*Sandbox* directory for testing things out-- you can do this wherever you
like):

.. code-block:: bash

    $ cd ~/Sandbox
    $ mkdir sbt_test
    $ cd sbt_test
    $ sphinx-quickstart

The ``sphinx-quickstart`` asks a bunch of setup questions (you can usually
select the default option by hitting *enter*).  After the setup, I have a
directory like this:

.. code-block:: bash

    $ ls sbt_test/
    _build  conf.py  index.rst  Makefile  _static  _templates

Next, I will try to follow the instructions at `sphinx-bootstrap-theme`_ to get
a basic site up and running.  This involves editing the ``conf.py`` file that
contains the *sphinx* options for generating html, pdf, etc output.  The
minimal changes to ``conf.py`` in order to get the bootstrap theme working are
in the `sphinx-bootstrap-theme installation`_ section and involve 

* importing the python code
* setting the *html_theme*
* setting the *html_theme_path*. 
  
Once that it done, use the generated ``Makefile`` to generate the html. The
command, and resulting output should look something like this:

.. code-block:: bash

    $ make html
    sphinx-build -b html -d _build/doctrees   . _build/html
    Making output directory...
    Running Sphinx v1.2.2
    loading pickled environment... not yet created
    building [html]: targets for 1 source files that are out of date
    updating environment: 1 added, 0 changed, 0 removed
    reading sources... [100%] index                                                                                                                                    
    looking for now-outdated files... none found
    pickling environment... done
    checking consistency... done
    preparing documents... done
    writing output... [100%] index                                                                                                                                     
    writing additional files... genindex search
    copying static files... done
    copying extra files... done
    dumping search index... done
    dumping object inventory... done
    build succeeded.
    
    Build finished. The HTML pages are in _build/html.

Now, open the ``index.html`` located in ``*_build/htlml`` to see the results.
Also checkout `customization of sphinx-bootstrap-theme`_ for more ideas.

.. _sphinx-bootstrap-theme: https://github.com/ryan-roemer/sphinx-bootstrap-theme
.. _sphinx-bootstrap-theme installation: https://github.com/ryan-roemer/sphinx-bootstrap-theme#installation
.. _customization of sphinx-bootstrap-theme: https://github.com/ryan-roemer/sphinx-bootstrap-theme#customization
.. _sphinx: http://sphinx-doc.org/
.. _bootstrap: http://getbootstrap.com/

.. author:: default
.. categories:: none
.. tags:: bootstrap, sphinx, python 2.7, my python setup, resume
.. comments::

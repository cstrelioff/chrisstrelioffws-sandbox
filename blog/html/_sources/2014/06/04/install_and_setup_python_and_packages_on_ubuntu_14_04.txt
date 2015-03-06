.. _initial python setup:

Install Python packages on Ubuntu 14.04
=======================================

In this post I will document my setup of Python 2.7.6 in Ubuntu 14.04.  Of
course, the base Python is installed by default, both Python 2.7.6 and Python
3.4.  Try the following in the terminal:

.. code-block:: bash

    $ python --version
    Python 2.7.6
    $ python2 --version
    Python 2.7.6
    $ python3 --version
    Python 3.4.0

As you can see, using ``python`` points to Python 2.7.6 by default.  However, 
``python2`` and ``python3`` can be used to access the desired version. I will
focus on installing packages for Python 2.7.6 here.

.. more::

Strategy
--------

In the past I have installed Python packages:

1. Using the Ubuntu repository:

.. code-block:: bash

    $ sudo apt-get packagename

2. Or, from a git/svn repository:

.. code-block:: bash

    $ sudo python setup.py

Approach 1 *has many advantages for Python users that don't need to have the
latest versions of every package*. In particular, all of the package
dependencies including other Python packages, linear algebra libraries, etc.
are also installed automatically.  As a result, if you are new to Ubuntu and
Python, strategy 1 is the way to go.

I will take a different tact, using pip_  to install, upgrade, and
remove packages.  Also, I will install all Python packages as a **user**, that
is, no use of **sudo**.  This makes it easy to use the same install procedure
on a machine where I don't have sudo privileges--say an Ubuntu cluster.
However, I will need **sudo** to install non-Python libraries, Fortran
compilers, etc. that the Python packages employ. On a cluster, the SysAdmin
would have to to do this part for me and other users.

pip_
----

Of course, the starting point is to get pip_ installed. Official
instructions are also available for `installing pip`_.  pip_ depends on
setuptools, but we can install both using the ``get-pip.py`` script,
as described at the install link.  To be concrete, I did the following:

.. code-block:: bash

    $ cd ~/Downloads
    $ curl -O https://bootstrap.pypa.io/get-pip.py
    $ python get-pip.py --user

If you don't have ``curl`` installed, this can be remedied using:

.. code-block:: bash

    $ sudo apt-get install curl

Because we have chosen local installation, the path  **~/.local/bin** has to be
added to our path.  To do that, add the following to the end of your
**~/.bashrc** file::

    # include .local/bin for local python scripts
    export PATH=~/.local/bin:$PATH

Then, source **~/.bashrc**:

.. code-block:: bash

    $ source ~/.bashrc

Try the following to see if you get similar results and to make sure the basic
setup is working:

.. code-block:: bash

    $ which pip
    /home/cstrelioff/.local/bin/pip
    $ pip --version
    pip 1.5.6 from /home/cstrelioff/.local/lib/python2.7/site-packages (python 2.7)

Of course, *your username* should be in the path, but the output should look
something like the above.

virtualenv_
-----------

Another major tool for Python 2.7 project management is virtualenv_. This
package allows the user to create many *virtual* Python environments, with
different packages installed, and to *activate* and *deactive* these
environments whenever the user desires. This is extremely useful for developers
who want to create a minimal environment for their application.

The virtualenv_ installation is simple with pip_ (again, I'm doing a user
install with no sudo):

.. code-block:: bash
    
    $ pip install --user virtualenv

To test it out, see if you get something like the following:

.. code-block:: bash

    $ virtualenv --version
    1.11.6
    $ pip show virtualenv
    ---
    Name: virtualenv
    Version: 1.11.6
    Location: /home/cstrelioff/.local/lib/python2.7/site-packages
    Requires: 

Now that virtualenv_ is installed, there will be two paths forward for the
rest of the Python installs:

1. Keep installing as a user -- **I'll use this approach**
2. Create a virtual environment and install everything there to have a
   completely isolated Python environment -- **I'll write a post about
   this later**

.. _Ubuntu 14.04 Python dependencies:

Ubuntu dependencies
-------------------

A variety of Ubuntu-specific packages are needed by Python packages.  These are
libraries, compilers, fonts, etc.  I'll detail these here along with install
commands. Depending on what you want to install you might not need all of
these.

* General development/build:

.. code-block:: bash

     $ sudo apt-get install build-essential python-dev

* Compilers/code integration:

.. code-block:: bash

    $ sudo apt-get install gfortran
    $ sudo apt-get install swig

* Numerical/algebra packages:

.. code-block:: bash

    $ sudo apt-get install libatlas-dev
    $ sudo apt-get install liblapack-dev

* Fonts (for matplotlib)

.. code-block:: bash

   $ sudo apt-get install libfreetype6 libfreetype6-dev

* More fonts (for matplotlib on Ubuntu Server 14.04-- see comment at end of
  post) -- added 2015/03/06

.. code-block:: bash

   $ sudo apt-get install libxft-dev

* Graphviz for pygraphviz, networkx, etc.

.. code-block:: bash

    $ sudo apt-get install graphviz libgraphviz-dev

* IPython require pandoc for document conversions, printing, etc.

.. code-block:: bash

    $ sudo apt-get install pandoc

* Tinkerer dependencies

.. code-block:: bash

    $ sudo apt-get install libxml2-dev libxslt-dev zlib1g-dev

That's it, now we start installing the Python packages.

numpy_
------

numpy_ is one of the fundamental numerical packages in Python. To install using
pip_ type:

.. code-block:: bash

    $ pip install --user numpy

This will result in a fair amount of compiling followed by a note that the
package was successfully installed.  If not, make a note of the error.  Often
this results from not having libraries and/or compilers installed (see above).

Information about the installation location and the version can be obtained
with the following:

.. code-block:: bash

    $ pip show numpy
    ---
    Name: numpy
    Version: 1.8.1
    Location: /home/cstrelioff/.local/lib/python2.7/site-packages
    Requires:

You should also be able to start python at the terminal and ``import numpy``
without complaint:

.. code-block:: python

    Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
    [GCC 4.8.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import numpy as np
    >>> print np.__version__
    1.8.1
    >>> exit()

scipy_
------

scipy_ has many useful mathematical utilities, complementing numpy_.
Installation is accomplished with:

.. code-block:: bash

    $ pip install --user scipy

Again, expect lots of compiling! As with numpy_, try:

.. code-block:: bash

    $ pip show scipy
    ---
    Name: scipy
    Version: 0.14.0
    Location: /home/cstrelioff/.local/lib/python2.7/site-packages
    Requires:

and, loading python:

.. code-block:: python

    Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
    [GCC 4.8.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import scipy
    >>> print scipy.__version__
    0.14.0
    >>> exit()

matplotlib_
-----------

matplotlib_ is one of the main plotting packages for Python and many other
packages use the utilities.  Install with:

.. code-block:: bash

    $ pip install --user matplotlib

If you look carefully, the completion of the installation will say::

    Successfully installed matplotlib python-dateutil tornado pyparsing nose
    backports.ssl-match-hostname
    Cleaning up...

So, matplotlib_ installs a variety of Python-dependencies.  As usual, try:

.. code-block:: bash

    $ pip show matplotlib
    ---
    Name: matplotlib
    Version: 1.3.1
    Location: /home/cstrelioff/.local/lib/python2.7/site-packages
    Requires: numpy, python-dateutil, tornado, pyparsing, nose

Finally try a simple plot:

.. code-block:: python

    Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
    [GCC 4.8.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import matplotlib.pyplot as plt
    >>> plt.plot([1,2,3,4])
    [<matplotlib.lines.Line2D object at 0x7f13a8571890>]
    >>> plt.ylabel('some numbers')
    <matplotlib.text.Text object at 0x7f13a85c47d0>
    >>> plt.show()
    >>> exit()

A plot should open in a new window when ``plot.show()`` is executed.

sympy_
------

sympy_ is a computer algebra system for Python.  Install with pip_ using:

.. code-block:: bash

    $ pip install --user sympy

Again, installation information from pip_ is obtained with:

.. code-block:: bash

    $ pip show sympy
    ---
    Name: sympy
    Version: 0.7.5
    Location: /home/cstrelioff/.local/lib/python2.7/site-packages
    Requires: 

Finally, following the `sympy tutorial`_, start Python and try:

.. code-block:: python

    Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
    [GCC 4.8.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from sympy import symbols
    >>> x, y = symbols('x y')
    >>> expr = x + 2*y
    >>> expr
    x + 2*y
    >>> expr + 1
    x + 2*y + 1
    >>> expr - x
    2*y
    >>> exit()

Cool!

IPython_
--------

Next, we install IPython_ (including notebooks), which has become a major tool
for sharing python projects in an interactive format.  To install we use:

.. code-block:: bash

    $ pip install --user ipython[notebook]

At the end, we get the message::

    Successfully installed ipython jinja2 pyzmq markupsafe
    Cleaning up...

showing that jinja2, pyzmq and markupsafe have also been installed.  Get
install information from pip_:

.. code-block:: bash

    $ pip show ipython
    ---
    Name: ipython
    Version: 2.1.0
    Location: /home/cstrelioff/.local/lib/python2.7/site-packages
    Requires: 

Now, try:

.. code-block:: bash

    $ ipython

which launches the IPython_ terminal.  Notice the IPython_ version is provided
and the prompt looks different from the normal ``>>>`` Python prompt (see the
IPython_ documentation for more information):

.. code-block:: python

    Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
    Type "copyright", "credits" or "license" for more information.
    
    IPython 2.1.0 -- An enhanced Interactive Python.
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object', use 'object??' for extra details.
    
    In [1]: import numpy as np
    
    In [2]: print np.__version__
    1.8.1
    
    In [3]: exit()


Finally, IPython_ notebook can be launched with the command:

.. code-block:: bash

    $ ipython notebook

This launches a web browser and you should see the IPython_ notebook interface.
You can create a new notebook and work away. To shutdown the server, back at
the terminal where you launched the notebook, type **cntrl-C** and then **y**
when prompted:

.. code-block:: bash

    Shutdown this notebook server (y/[n])? y
    2014-06-04 16:29:04.033 [NotebookApp] CRITICAL | Shutdown confirmed
    2014-06-04 16:29:04.033 [NotebookApp] Shutting down kernels

That's it, you're now an IPython_ notebook user!

pygraphviz_
-----------

pygraphviz_ is a Python interface to the graphviz_ visualization code that can
be used by itself but is also employed by networkx_ and other packages.  Be
sure that graphviz_ and its developer libraries are installed (see Ubuntu
Dependencies above) and install pygraphviz_ using:

.. code-block:: bash

    $ pip install --user pygraphviz

Get install information from pip_:

.. code-block:: bash

    $ pip show pygraphviz
    ---
    Name: pygraphviz
    Version: 1.2
    Location: /home/cstrelioff/.local/lib/python2.7/site-packages
    Requires: 

Also, try:

.. code-block:: python

    Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
    [GCC 4.8.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import pygraphviz
    >>> print pygraphviz.__version__
    1.2
    >>> exit()

networkx_
---------

networkx_ is a Python package for building, analyzing, and visualizing
graphs/networks. There are a variety of dependencies, all of which we have
installed above.  So, install with:

.. code-block:: bash

    $ pip install --user networkx

Get install information from pip_:

.. code-block:: bash

    $ pip show networkx
    ---
    Name: networkx
    Version: 1.8.1
    Location: /home/cstrelioff/.local/lib/python2.7/site-packages
    Requires: 

Try a simple example:

.. code-block:: python

    Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
    [GCC 4.8.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import networkx as nx
    >>> G = nx.Graph()
    >>> G.add_edge(1,2)
    >>> G.add_edge(2,3)
    >>> import matplotlib.pyplot as plt
    >>> nx.draw(G)
    >>> plt.show()
    >>> exit()

With matplotlib_ and pygraphviz_ installed (see above), this code should create
a very simple graph and show it in a new window when ``plt.show()`` is
executed.

pandas_
-------

pandas_ is a Python packaged focused on data -- reading, writing, manipulating,
etc. There are a variety of `pandas dependencies`_: required, recommended and 
optional.  We'll focus on the first two categories.

The required dependencies are numpy_ (installed above), **python-dateutil**
(installed above with matplotlib_), and **pytz** (we will let pip_ install with 
pandas_). However, let's install the recommended dependencies:

* numexpr_

.. code-block:: bash

    $ pip install --user numexpr

After install we get:

.. code-block:: bash

    $ pip show numexpr
    ---
    Name: numexpr
    Version: 2.4
    Location: /home/cstrelioff/.local/lib/python2.7/site-packages
    Requires: numpy

* bottleneck_

.. code-block:: bash

    $ pip install --user Bottleneck

After install we get:

.. code-block:: bash

    $ pip show Bottleneck
    ---
    Name: Bottleneck
    Version: 0.8.0
    Location: /home/cstrelioff/.local/lib/python2.7/site-packages
    Requires: 

We can also import both packages in Python and print the package version to
make sure that basic usage seems okay:

.. code-block:: bash

    $ python -c "import numexpr;print numexpr.__version__"
    2.4
    $ python -c "import bottleneck;print bottleneck.__version__"
    0.8.0

Finally, for pandas_, we install the main package:

.. code-block:: bash

    $ pip install --user pandas

After some downloading and compiling we get (showing that both pandas *and* 
pytz were installed, as expected):

.. code-block:: bash

    Successfully installed pandas pytz
    Cleaning up...

Use pip_ to check the installation information:

.. code-block:: bash

    $ pip show pandas
    ---
    Name: pandas
    Version: 0.14.0
    Location: /home/cstrelioff/.local/lib/python2.7/site-packages
    Requires: python-dateutil, pytz, numpy

**Note**: if you import pandas_, an error about **openpyxl** (a package for
working with Excel 2007 files) will be issued:

.. code-block:: python

    Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
    [GCC 4.8.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import pandas
    /home/cstrelioff/.local/lib/python2.7/site-packages/pandas/io/excel.py:626: UserWarning: Installed openpyxl is not supported at this time. Use >=1.6.1 and <2.0.0.
      .format(openpyxl_compat.start_ver, openpyxl_compat.stop_ver))
    >>> exit()

The error says that **openpyxl** needs to be at least version 1.6.1 and less
than 2.0.0.  *Strange*, this package is listed as optional.  Oh well, let's
install an appropriate version.  If we just use pip_ to install the current
version it will be too high.  So, I installed as follows:

* openpyxl 1.8.6

.. code-block:: bash

    $ pip install --user openpyxl==1.8.6

This install forces the use an appropriate version.  Now, try importing
pandas_ and we get:

.. code-block:: python

    Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
    [GCC 4.8.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import pandas
    >>> print pandas.__version__
    0.14.0
    >>> import openpyxl
    >>> print openpyxl.__version__
    1.8.6
    >>> exit()

Yay(!) we can import pandas_ (and openpyxl) without complaints.

Finally, before leaving pandas_, I will mention that there are a variety of
`optional pandas dependencies`_ that you might want to consider as well. I won't 
consider them in this post.

pymc_
-----

pymc_ is a really nice MCMC package for Python.  I have used it on several
projects with great success.  Installation with pip_ follows the usual format:

.. code-block:: bash

    $ pip install --user pymc

Get install information:

.. code-block:: bash

    $ pip show pymc
    ---
    Name: pymc
    Version: 2.3.2
    Location: /home/cstrelioff/.local/lib/python2.7/site-packages
    Requires: 

Starting Python you should also be able to get:

.. code-block:: python

    Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
    [GCC 4.8.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import pymc
    >>> print pymc.__version__
    2.3.2
    >>> exit()

statsmodels_
------------

statsmodels_ provides some nice statistics methods.  Before installing
statsmodels_ itself, we must install dependencies, which will likely be usesul
in any case: patsy_ and cython_.

* patsy_ : is a package for describing statistical models in R-like format.
  Install with:

.. code-block:: bash

    $ pip install --user patsy

We can see where pip_ installed patsy_:

.. code-block:: bash

    $ pip show patsy
    ---
    Name: patsy
    Version: 0.2.1
    Location: /home/cstrelioff/.local/lib/python2.7/site-packages
    Requires: numpy

and try importing patsy_ in a Python session:

.. code-block:: python

    Python 2.7.6 (default, Mar 22 2014, 22:59:56)
    [GCC 4.8.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import patsy
    >>> print patsy.__version__
    0.2.1
    >>> exit()

* cython_ : allows for wrapping of c++ code. Install with:

.. code-block:: bash

    $ pip install --user Cython

Check with pip_:

.. code-block:: bash

    $ pip show Cython
    ---
    Name: Cython
    Version: 0.20.1
    Location: /home/cstrelioff/.local/lib/python2.7/site-packages
    Requires: 

and importing in a Python session:

.. code-block:: python

    Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
    [GCC 4.8.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import cython
    >>> print cython.__version__
    0.20.1
    >>> exit()

* Finally, install statsmodels_ with pip_:

.. code-block:: bash

    $ pip install --user statsmodels

Show install info with pip_:

.. code-block:: bash

    $ pip show statsmodels
    ---
    Name: statsmodels
    Version: 0.5.0
    Location: /home/cstrelioff/.local/lib/python2.7/site-packages
    Requires: 

and try an import:

.. code-block:: bash

    Python 2.7.6 (default, Mar 22 2014, 22:59:56)
    [GCC 4.8.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import statsmodels
    >>> print statsmodels.__version__
    0.5.0
    >>> exit()

Okay, that's patsy_, cython_ and statsmodels_.

.. _install CMPy:

CMPy_
-----

CMPy_ is a package for Computational Mechanics in Python developed in the
Crutchfield Lab at UC Davis.  Currently the package is developed, using git for
version control, but is not publicly available.  However, I will document the
install here because:

1. It's useful for people at UCD (or collaborating with people at UCD)
2. This is an example of installation of a Python package in a folder on the
   local machine

I start by showing that I have cloned the :ref:`install CMPy` package to the
**~/gitlocal/cmpy/** directory.  You can see the **setup.py** file when I show
the directory contents:

.. code-block:: bash

    $ ls ~/gitlocal/cmpy/
    apps  build  CHANGES.txt  cmpy  data  docs  gallery  LICENSE.txt  MANIFEST.in  old_doc  pylintrc  README.txt  scripts  setup.py  src

We do the install with pip_, using the **-e** switch to show the location of the
package code:
    
.. code-block:: bash

    $ pip install --user -e ~/gitlocal/cmpy/
    Obtaining file:///home/cstrelioff/gitlocal/cmpy
      Running setup.py (path:/home/cstrelioff/gitlocal/cmpy/setup.py) egg_info for package from file:///home/cstrelioff/gitlocal/cmpy
        
    Installing collected packages: CMPy
      Running setup.py develop for CMPy
        
        Creating /home/cstrelioff/.local/lib/python2.7/site-packages/CMPy.egg-link (link to .)
        Adding CMPy 1.0dev to easy-install.pth file
        
        Installed /home/cstrelioff/gitlocal/cmpy
    Successfully installed CMPy
    Cleaning up...

Note that the path to the CMPy_ directory is added to **easy-install.pth**, a
file that Python consults to find CMPy_. Finally, we show the pip_ information:

.. code-block:: bash

    $ pip show cmpy
    ---
    Name: CMPy
    Version: 1.0dev
    Location: /home/cstrelioff/gitlocal/cmpy
    Requires: 

Again, note that the location is **~/gitlocal/cmpy/**, instead of
**~/.local/lib/python2.7/site-packages/**, due to the **-e** tag.  This is why
the addition to the **easy_install.pth** file (above) was needed.

**Edit:** Aug 21st, 2014

A note on updating this local installation is in order.  Recently a change in
code was made that affected underlying *c code* that is incorporated using
cython.  I pulled the repository changes using:

.. code-block:: bash

    $ cd ~/gitlocal/cmpy/
    $ git pull

To try and update the install I did:

.. code-block:: bash

    $ pip install --user -e ~/gitlocal/cmpy/

This ran the ``setup.py`` file but did *not* recompile the modified c code.
To get this to work I had to remove the ``build`` directory, build in place and
install again:

.. code-block:: bash

    $ cd ~/gitlocal/cmpy/
    $ rm -r build/
    $ python setup.py build_ext -i --cython
    $ pip install --user -e ~/gitlocal/cmpy/

Is there a better way to do this? Let me know in the comments below.

.. _install restview:

restview_
---------

restview_ is a Python package that processes reStructuredText_ and launches a
web browser for viewing. Each time the browser is refreshed, the underlying
**rst** document will be re-processed and displayed-- very nice for working on
Python docmentation or any **rst** document. Installation goes as usual:

.. code-block:: bash

    $ pip install --user restview

We can see what was installed:

.. code-block:: bash

    $ pip show restview
    ---
    Name: restview
    Version: 2.0.5
    Location: /home/cstrelioff/.local/lib/python2.7/site-packages
    Requires: docutils, pygments

As you can see from above, **docutils** and **pygments** will be installed if
they are not already installed.

To process an **rst** document named **test.rst** type:

.. code-block:: bash

    $ restview test.rst

Check restview_ for more examples.

.. _install tinkerer:

tinkerer_
---------

tinkerer_ is a blogging environment for Pythonistas that is built on Sphinx_,
a Python documentation tool. Blog entries are written in reStructuredText_ and
rendered as static html.  Of course, this is also the tool I use for this blog.
Before moving to our usual pip_ install, we have to take care of some
`Ubuntu 14.04 Python dependencies`_.  Assuming these requirements are available,
tinkerer_ is installed with the usual:

.. code-block:: bash

    $ pip install --user tinkerer

We can check the install information with:

.. code-block:: bash

    $ pip show tinkerer
    ---
    Name: Tinkerer
    Version: 1.4.2
    Location: /home/cstrelioff/.local/lib/python2.7/site-packages
    Requires: Jinja2, Sphinx, Babel, pyquery

Note that requirements Jinja2_, Sphinx_, Babel_ and pyquery_ are also installed
automatically.  A quick start to getting a blog up and running (at least the
generation of posts, pages and generating the html output) is available 
`here <http://tinkerer.me/pages/documentation.html>`_.

.. _install Pweave:

Pweave_
-------

Pweave_ is a tool for literate programming with Python. This tool allows me to
write blog posts about Python using a **.Pnw** file that contains
reStructuredText_, along with special Pweave_ commands, and have the Python
code evaluated and output included in the **.rst** output file--
`see the example here <http://mpastell.com/pweave/examples.html>`_. This is a
really nice tool to avoid typos in code and to make sure that what you're
talking about actually works! I should note that IPython_ notebooks can also do
this by exporting to reStructuredText_. In any case, I will trying out both of
these tools for future posts.

The install of Pweave_ goes as usual:

.. code-block:: bash

    $ pip install --user Pweave

Check the install with:

.. code-block:: bash

    $ pip show Pweave
    ---
    Name: Pweave
    Version: 0.21.2
    Location: /home/cstrelioff/.local/lib/python2.7/site-packages
    Requires: 

scikit-learn_
-------------

scikit-learn_ is the probably the most well-known and feature-complete package
for machine learning tasks in Python.  There are a number of dependencies that
need to be installed (numpy_, scipy_, python-dev, etc see `scikit-learn
installation`_ for more information) that have already been installed above. 
So, we install using pip_, as usual:

.. code-block:: bash

    $ pip install --user scikit-learn

Then we can check the installed version and location using:

.. code-block:: bash

    $ pip show scikit-learn
    ---
    Name: scikit-learn
    Version: 0.15.1
    Location: /home/cstrelioff/.local/lib/python2.7/site-packages
    Requires: 

That's it, machine-learn away!

.. _numpy: http://docs.scipy.org/doc/numpy/reference/
.. _scipy: http://docs.scipy.org/doc/scipy/reference/ 
.. _matplotlib: http://matplotlib.org/
.. _sympy: http://docs.sympy.org/latest/index.html
.. _sympy tutorial: http://docs.sympy.org/latest/tutorial/intro.html#a-more-interesting-example
.. _IPython: http://ipython.org/
.. _scikit-learn: http://scikit-learn.org/stable/index.html
.. _scikit-learn installation: http://scikit-learn.org/stable/install.html
.. _pygraphviz: http://pygraphviz.github.io/documentation/latest/
.. _graphviz: http://www.graphviz.org/
.. _networkx: http://networkx.github.io/
.. _pandas: http://pandas.pydata.org/index.html
.. _pandas dependencies: http://pandas.pydata.org/pandas-docs/stable/install.html#dependencies
.. _optional pandas dependencies: http://pandas.pydata.org/pandas-docs/stable/install.html#optional-dependencies
.. _numexpr: https://github.com/pydata/numexpr
.. _bottleneck: http://berkeleyanalytics.com/bottleneck/index.html
.. _pymc: http://pymcmc.readthedocs.org/en/latest/index.html
.. _statsmodels: http://statsmodels.sourceforge.net/index.html
.. _patsy: http://patsy.readthedocs.org/en/latest/index.html
.. _cython: http://cython.org/ 
.. _CMPy: http://cmpy.csc.ucdavis.edu/index.html
.. _restview: https://pypi.python.org/pypi/restview
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _tinkerer: http://tinkerer.me/
.. _Sphinx: http://sphinx-doc.org/
.. _Jinja2: http://jinja.pocoo.org/
.. _Babel: http://babel.pocoo.org/
.. _pyquery: http://pyquery.readthedocs.org/en/latest/
.. _Pweave: http://mpastell.com/pweave/

.. _pip: http://pip.readthedocs.org/en/latest/index.html
.. _installing pip: http://pip.readthedocs.org/en/latest/installing.html
.. _virtualenv: http://virtualenv.readthedocs.org/en/latest/index.html 

.. author:: default
.. categories:: none
.. tags:: python 2.7, ubuntu 14.04, python, my ubuntu setup, pip, virtualenv, numpy, scipy, matplotlib, sympy, ipython, pygraphviz, networkx, pandas, numexpr, bottleneck, openpyxl, pymc, statsmodels, patsy, cython, cmpy, restview, tinkerer, pweave, scikit-learn

.. comments::

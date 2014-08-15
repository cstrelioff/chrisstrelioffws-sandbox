Install R on Ubuntu 14.04
=========================

In this post I will go over installing R on Ubuntu 14.04 following the
`installation instructions at cran`_. I will also cover installing the packages
required to do the *Topics in machine learning* assignment for
`Coursera's Introduction to Data Science`_.

.. more::

As it turns out, not much has changed from the post I wrote to
`install R on Ubuntu 12.04`_ back in 2012.  First we add the cran repository we
want to use for getting our R updates.  I use the stats repository at UCLA with
the following command:

.. code-block:: bash

    $ sudo add-apt-repository "deb http://cran.stat.ucla.edu/bin/linux/ubuntu trusty/"

The use of *trusty* in the address above indicates that we want to install for
Ubuntu 14.04.  The archives are signed by a key that we should add for secure
apt using:

.. code-block:: bash

    $ gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9
    $ gpg -a --export E084DAB9 | sudo apt-key add -

If you have problems with these commands consult the `installation instructions
at cran`_ for alternatives to the above.

Now that we have the repository setup and the key added we do typical Ubuntu
install commands to install R:

.. code-block:: bash

    $ sudo apt-get update
    $ sudo apt-get install r-base r-base-dev

`r-base-dev` is not required but I suggest installing because it might be
needed to install other R packages later.  This will download and install ~40MB
worth of base packages and install everything.

Once finished with the install, you should be able startup R:

.. code-block:: bash

    $ R

and see something like:

.. code-block:: r

    R version 3.1.1 (2014-07-10) -- "Sock it to Me"
    Copyright (C) 2014 The R Foundation for Statistical Computing
    Platform: x86_64-pc-linux-gnu (64-bit)
    
    R is free software and comes with ABSOLUTELY NO WARRANTY.
    You are welcome to redistribute it under certain conditions.
    Type 'license()' or 'licence()' for distribution details.
    
      Natural language support but running in an English locale
    
      R is a collaborative project with many contributors.
      Type 'contributors()' for more information and
      'citation()' on how to cite R or R packages in publications.
    
      Type 'demo()' for some demos, 'help()' for on-line help, or
      'help.start()' for an HTML browser interface to help.
      Type 'q()' to quit R.
    
      > quit()
      Save workspace image? [y/n/c]: n

Installing R packages
---------------------

The above installation provides the following packages::

    r-cran-boot
    r-cran-class
    r-cran-cluster
    r-cran-codetools
    r-cran-foreign
    r-cran-kernsmooth
    r-cran-lattice
    r-cran-mass
    r-cran-matrix
    r-cran-mgcv
    r-cran-nlme
    r-cran-nnet
    r-cran-rpart
    r-cran-spatial
    r-cran-survival
    r-cran-rodbc

These will be automatically update, like normal Ubuntu updates, whenever new
versions are available at cran.

If we want other (less standard) packages we have to install and update them by
ourselves.  The basic process is as follows:

* Start R using ``sudo``

.. code-block:: bash

    $ sudo R

* To install a package called *packagename* the command would be:

.. code-block:: r

    > install.packages('packagename', dep = TRUE)

**Note:** the quote around *packagename* are required. Updating packages is
accomplished using:

.. code-block:: bash

    $ sudo R

and

.. code-block:: r

    > update.packages()

Example
-------

Finally, as an example of the above, I'll install the packages required for the
*Topics in machine learning* assignment in `Coursera's Introduction to Data
Science`_.  The needed packages are: caret_, rpart_, tree_, randomForest_,
e1071_ and ggplot2_.

First, make sure that you have ``gcc`` and ``gfortran`` available (many will
already have these installed) using:

.. code-block:: bash

    $ sudo apt-get install gcc gfortran

Next, following the approach outlined above, we start R with ``sudo``

.. code-block:: bash

    $ sudo R

and then start installing (some of these download and compile a fair amount of
code and data -- be patient):

.. code-block:: r

    > install.packages('caret', dep = TRUE)
    > install.packages('rpart', dep = TRUE)
    > install.packages('tree', dep = TRUE)
    > install.packages('randomForest', dep = TRUE)
    > install.packages('e1071', dep = TRUE)
    > install.packages('ggplot2', dep = TRUE)

That's it, we are ready to go!

.. _installation instructions at cran: http://cran.r-project.org/bin/linux/ubuntu/README.html
.. _Coursera's Introduction to Data Science: https://www.coursera.org/course/datasci
.. _install R on Ubuntu 12.04: http://livesoncoffee.wordpress.com/2012/12/09/installing-r-on-ubuntu-12-04/
.. _caret: http://cran.r-project.org/web/packages/caret/index.html
.. _rpart: http://cran.r-project.org/web/packages/rpart/index.html
.. _tree: http://cran.r-project.org/web/packages/tree/index.html 
.. _randomForest: http://cran.r-project.org/web/packages/randomForest/index.html
.. _e1071: http://cran.r-project.org/web/packages/e1071/index.html 
.. _ggplot2: http://cran.r-project.org/web/packages/ggplot2/index.html 

.. author:: default
.. categories:: none
.. tags:: R, my ubuntu setup, caret, rpart, tree, randomForest, e1071, ggplot2
.. comments::

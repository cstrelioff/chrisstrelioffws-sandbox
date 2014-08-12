.. _installing Octave:

Installing Octave on Ubuntu 14.04
=================================

.. author:: default
.. categories:: none 
.. tags:: my ubuntu setup, ubuntu 14.04, octave, machine learning, gnuplot, coursera
.. comments::

I'm taking Andrew Ng's `machine learning class at coursera`_ that started June
17, 2014.  In the Silicon Valley tech world, this seems to be the online course
that many people recommend for machine learning.  The course is taught using
Octave_ or Matlab_. I'll use Octave_ because I'm on Ubuntu and Octave_ is a
gnu project.

.. more::

I will also blog about the topics covered using Python because this is my
language of choice.  However, I will not poster answers to exercises.  Instead
I will discuss the method and how to implement, or use existing tools, in
Python.

First, let's install Octave_ and gnuplot_:

.. code-block:: bash

    $ sudo apt-get install octave gnuplot

Accept all the suggestions (there are **many**) and let the installation
complete. Starting Octave_ from the terminal should look something like this (I
try out the first part of the `Octave simple examples`_ before exiting):

.. code-block:: octave

    $ octave
    GNU Octave, version 3.8.1
    Copyright (C) 2014 John W. Eaton and others.
    This is free software; see the source code for copying conditions.
    There is ABSOLUTELY NO WARRANTY; not even for MERCHANTABILITY or
    FITNESS FOR A PARTICULAR PURPOSE.  For details, type 'warranty'.
    
    Octave was configured for "x86_64-pc-linux-gnu".
    
    Additional information about Octave is available at http://www.octave.org.
    
    Please contribute if you find this software useful.
    For more information, visit http://www.octave.org/get-involved.html
    
    Read http://www.octave.org/bugs.html to learn how to submit bug reports.
    For information about changes from previous versions, type 'news'.
    
    octave:1> A = [ 1, 1, 2; 3, 5, 8; 13, 21, 34 ]
    A =
    
        1    1    2
        3    5    8
       13   21   34
    
    octave:2> B = rand (3, 2);
    octave:3> B
    B =
    
       0.225359   0.115306
       0.548261   0.295556
       0.166765   0.073095 
    
    octave:4> A * B
    ans =
    
        1.10715    0.55705 
        4.75150    2.40846 
       20.11315   10.19090 
    
    octave:5> exit

That's it, Octave_ (version 3.8.1) is ready to go.  The class website has some
Octave_ tutorials.  I also found the `wikibooks Octave tutorial`_, which seems
to cover many of the basics in a concise way.

.. _machine learning class at coursera: https://www.coursera.org/course/ml
.. _Octave: https://www.gnu.org/software/octave/index.html
.. _Matlab: http://www.mathworks.com/products/matlab/
.. _gnuplot: http://www.gnuplot.info/
.. _Octave simple examples: https://www.gnu.org/software/octave/doc/interpreter/Simple-Examples.html#Simple-Examples
.. _wikibooks Octave tutorial: http://en.wikibooks.org/wiki/Octave_Programming_Tutorial

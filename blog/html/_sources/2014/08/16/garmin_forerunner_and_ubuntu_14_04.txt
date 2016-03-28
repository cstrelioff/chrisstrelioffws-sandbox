Garmin forerunner and Ubuntu 14.04
==================================

This post is about getting running data off of a Garmin Forerunner 305 and
uploaded to the Garmin Connect website.  This post follows my previous post on
the `Garmin forerunner and Ubuntu 12.04`_. Basically I will repeat these
previous instructions, making sure that everything can still be done
on Ubuntu 14.04-- the good news is that everything works on 14.04, so read on
if you are interested.

.. more::

* First, we install some dependencies:

.. code-block:: bash

    $ sudo apt-get install garmin-forerunner-tools libxml2-utils

* Second, we grab code from a git repository (do this in a directory where you
  want the code to reside-- I'll do this in ``~/gitlocal/``):

.. code-block:: bash

    $ cd ~/gitlocal/
    $ git clone git@github.com:cstrelioff/garmin-dev.git

**Edit: 2015, Aug 27**

The above :code:`git clone` command uses ssh and will only work if you have a
github account setup and have an ssh key on file.  If you don't and would 
rather not bother setting that up you can

1. Dowload a zip of the repository from the
   `github page <https://github.com/cstrelioff/garmin-dev>`_ and unzip
   on your local computer-- look for the **Download ZIP** button on the right
   side of the page.

2. Use git with https instead of ssh.  This changes the git clone command
   to

.. code-block:: bash

    $ git clone https://github.com/cstrelioff/garmin-dev.git

**End edit**

* Finally we are ready to get data.  I will give one approach -- start by
  making a directory where the data will be saved. For example,

.. code-block:: bash

    $ mkdir ~/GarminData
    $ cd ~/GarminData

Next, we connect the watch to the computer using the usb cable and obtain the
data from the watch:

.. code-block:: bash

    $ garmin_save_runs

**Edit: 2016, Mar 28**

Above corrected to "garmin_save_runs", from "garmin-save-runs", thanks to
comment below.

**End edit**

If there is data on the watch, this command should produce ``*.gmn`` files that
use the directory structure: ``Year/Month/*.gmn``.

Finally, the ``*.gmn`` files need to be converted to ``*.tcx`` for upload to
Garmin Connect. It is probably good to choose a consistent place to do this.
For example, create a directory called ``tcxfiles``:

.. code-block:: bash

    $ mkdir ~/GarminData/tcxfiles
    $ cd ~/GarminData/tcxfiles/

A command to do the conversions has to provide full paths for ``gmn2tcx`` and
the input ``*.gmn`` file. So, try something like this if you've used the
directory structure discussed above:

.. code-block:: bash

    $ ~/gitlocal/garmin-dev/gmn2tcx ~/GarminData/DataFromWatch/Year/Month/file.gmn > run-name.tcx

Be sure to change ``~/GarminData/DataFromWatch/Year/Month/file.gmn`` to
something that makes sense.  If all went well, the file ``run-name.tcx`` (change 
this filename to something sensible as well) will be in your local directory
and ready to upload. Of course, in the short run you'll want to write a script
to automate this process and avoid the typing.

.. _Garmin forerunner and Ubuntu 12.04: http://livesoncoffee.wordpress.com/2013/10/21/garmin-forerunner-and-ubuntu-12-04-updated/

.. author:: default
.. categories:: none
.. tags:: garmin, running
.. comments::

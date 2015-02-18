Install QGIS on Ubuntu 14.04
============================

In this post I will cover my install process for `QGIS`_ on Ubuntu 14.04.
`QGIS`_ is a tool for creating maps and working with geospatial information. The
`official QGIS installation instructions`_ provide three different ways to
install the software. I'll be using the `UbuntuGIS`_ ppa to get access to more
recent versions of the relevant GIS software, including `QGIS`_.

.. more::

The *unstable ppa* seems to be the one to use (I tried the stable ppa, which 
does not seem to work; at least for Ubuntu 14.04).  Before starting, note that
this process downloads about **90MB** of software so a decent connection is
suggested.  The install goes as follows:

.. code:: bash

    $ sudo apt-get install python-software-properties
    $ sudo add-apt-repository ppa:ubuntugis/ubuntugis-unstable
    $ sudo apt-get update
    $ sudo apt-get install qgis python-qgis qgis-plugin-grass

This installed without issues for me.  To get to the `QGIS`_ desktop: 

* Hit the *Super Key* (aka the *Windows Key*) or click on the top button on the
  launcher and search for `QGIS`_. 

* The `QGIS`_ desktop icon should come up-- click the icon and `QGIS`_ should
  start up.

* When the program is running its icon will display on the launcher. **If you
  want the icon to be available on the launcher at all times**, *right-click on
  the icon*, then select *Lock to launcher* and you're good to go.

That's all for now.  As always, leave questions and comments below.

.. _QGIS: http://www2.qgis.org/en/site/index.html
.. _official QGIS installation instructions: http://www2.qgis.org/en/site/forusers/alldownloads.html#ubuntu
.. _UbuntuGIS: https://wiki.ubuntu.com/UbuntuGIS
.. author:: default
.. categories:: none
.. tags:: ubuntu 14.04, gis, qgis, Open Oakland
.. comments::

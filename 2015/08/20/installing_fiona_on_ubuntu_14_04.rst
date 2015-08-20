Installing Fiona on Ubuntu 14.04
================================

This post consists of some quick notes on installing `Fiona`_, a Python
interface to OGR, which is a tool that one might want if working with GIS data
on a regular basis. I'm trying to do things like convert **shapefiles** to
**geojson**-- without much luck until now (see below)-- and this is one of the
tools I'm looking at as part of the solution. If you want to install `Fiona`_
on Ubuntu 14.04 follow along.

.. more::

I'll be following the `Fiona install instructions at github`_, using the
Ubuntu 14.04-specific information.  If you are on Windows, MAC, or another
Linux flavor you should check the page for help with your OS.

So, first we need to install a library that `Fiona`_ wraps:

.. code:: bash

    $ sudo apt-get install libgdal1-dev

Next, I'll use **pip** to install the package as a user:

.. code:: bash

    $ pip install --user fiona

We can get information on the install using **pip show**:

.. code:: bash

    $ pip show fiona
    ---
    Metadata-Version: 1.1
    Name: Fiona
    Version: 1.6.1
    Summary: Fiona reads and writes spatial data files
    Home-page: http://github.com/Toblerity/Fiona
    Author: Sean Gillies
    Author-email: sean.gillies@gmail.com
    License: BSD
    Location: /home/cstrelioff/.local/lib/python2.7/site-packages
    Requires: cligj, click-plugins, six
    Entry-points:
      [console_scripts]
      fio=fiona.fio.main:main_group
      [fiona.fio_commands]
      bounds=fiona.fio.bounds:bounds
      cat=fiona.fio.cat:cat
      collect=fiona.fio.cat:collect
      distrib=fiona.fio.cat:distrib
      dump=fiona.fio.cat:dump
      env=fiona.fio.info:env
      info=fiona.fio.info:info
      insp=fiona.fio.info:insp
      load=fiona.fio.cat:load

Okay, we have installed and are ready to go. I'll use the command-line script,
**fio**, included with the package for a quick demo using the shapefile
exported from `Alameda County School District Boundaries`_.  To start, lets
get information about the file:

.. code:: bash

        $ fio info --indent 2 UnifiedSchool.shp
        {
          "count": 29, 
          "crs": "+datum=NAD83 +lat_0=36.5 +lat_1=37.0666666667 +lat_2=38.4333333333 +lon_0=-120.5 +no_defs +proj=lcc +units=us-ft +x_0=2000000 +y_0=500000.0", 
          "driver": "ESRI Shapefile", 
          "bounds": [
            6028235.836711481, 
            1990996.2444430888, 
            6280437.554092631, 
            2157436.750131786
          ], 
          "schema": {
            "geometry": "Polygon", 
            "properties": {
              "DIST_NAME": "str:50", 
              "DISTRICT_I": "int:10", 
              "Shape_STAr": "float:19.11", 
              "Shape_STLe": "float:19.11"
            }
          }
        }

Finally, I will convert the **shapefile** into a **geojson** for visualizing on
the web using `leafletjs`_:

.. code:: bash

    $ fio dump UnifiedSchool.shp --indent 2 --precision 2 > UnifiedSchool.json

and, checkout the result:

.. code:: bash

    $ head UnifiedSchool.json
    { 
      "features": [
        { 
          "geometry": {
            "coordinates": [
              [ 
                [ 
                  -122.31,
                  37.79
                ],
    
The main thing to notice is that the output has latitude and longitude
values needed for `leafletjs`_ to show the regions correctly.  The original
shapefile did not have this formatting-- very cool! Checkout the `Fiona`_
github page for examples on how to use the package. Also, you can check out
`the resulting map here <http://chrisstrelioff.ws/vizdiv/alameda_school_districts/>`_.
Try clicking on the districts to see the name as well as playing with the
visible layers (upper-right corner of map). As always, comments and questions
are welcome.

.. _Fiona: https://github.com/Toblerity/Fiona 
.. _Fiona install instructions at github: https://github.com/Toblerity/Fiona#installation
.. _Alameda County School District Boundaries: https://data.acgov.org/Education/Unified-School-District-Boundaries/d4tn-s23x
.. _leafletjs: http://leafletjs.com/

.. author:: default
.. categories:: none
.. tags:: ubuntu 14.04, gis, python, shapefile, geojson
.. comments::

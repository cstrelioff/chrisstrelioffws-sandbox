Arduino on Ubuntu 14.04 without the Arduino IDE
===============================================

In this post I will document my setup for working with an Arduino Uno on Ubuntu
14.04. You can learn more about the Arduino at `Arduino.cc`_ if you are
unfamiliar with the microcontroller.  However, **be warned**, I am not going to
use the official Arudino IDE, if you'd like the official setup checkout the
`official Arduino installation instructions`_. Instead I'm going to setup the
basic requirements for writing and pushing code, including libraries and make
files, and use Vim as my editor. So, if you're interested in this approach,
follow along.

.. more::

I'll be using this nice (but outdated) post on jayway--
`jaway post on Ubuntu and Arduino`_-- as my starting point.  Additional
comments by *Havard*, at the end of the post, provide some nice updates,
thanks!

Install
-------

So, let's get started with the repository installs that provide libraries and
make files for Ubuntu (14.04):

.. code:: bash

    $ sudo apt-get install arduino-mk

This will install *arduino-mk* and *arduino-core* along with a bunch of
needed libraries. All of Arduino-specific libraries and documentation is
located in the following set of directories::

    /usr/share/arduino
    /usr/share/doc/arduino-core
    /usr/share/doc/arduino-mk

Check these directories out to see what's included and be sure to try out the
examples:

.. code:: bash

    $ ls -l /usr/share/doc/arduino-core/examples/
    total 44
    drwxr-xr-x  8 root root 4096 Dec  8 12:21 01.Basics
    drwxr-xr-x 11 root root 4096 Dec  8 12:21 02.Digital
    drwxr-xr-x  8 root root 4096 Dec  8 12:21 03.Analog
    drwxr-xr-x 13 root root 4096 Dec  8 12:21 04.Communication
    drwxr-xr-x  8 root root 4096 Dec  8 12:21 05.Control
    drwxr-xr-x  6 root root 4096 Dec  8 12:21 06.Sensors
    drwxr-xr-x  4 root root 4096 Dec  8 12:21 07.Display
    drwxr-xr-x 17 root root 4096 Dec  8 12:21 08.Strings
    drwxr-xr-x  5 root root 4096 Dec  8 12:21 09.USB
    drwxr-xr-x 16 root root 4096 Dec  8 12:21 10.StarterKit
    drwxr-xr-x  2 root root 4096 Dec  8 12:21 ArduinoISP

There are a bunch of things to try out! Note that each of the above is a
directory of examples that can help getting started.

USB access
----------

One of the issues many users seem to have using Arduino with Ubuntu is getting
the usb permissions to work. When the Arduino **is connected**, we can inspect
the properties of the usb port:

.. code:: bash

    $ ls -lah /dev/ttyACM0 
    crw-rw---- 1 root dialout 166, 0 Dec  8 13:24 /dev/ttyACM0

Notice that the *group* is dialout-- we will use that in a second.  However,
when the Arduino **is not connected**, the same command will give an error:

.. code:: bash

    $ ls -lah /dev/ttyACM0 
    ls: cannot access /dev/ttyACM0: No such file or directory

Now, to allow access to the usb port we add our (your) username to the dialout
group-- be sure to **change username** below:

.. code:: bash

   $ sudo adduser username dialout

*Note:* this accomplishes the
same thing as adding the username to the file `/etc/group`, as discussed by
Havard in his/her comments-- also, you'll have to **log off and logon** for the
group changes to be updated.

An example -- blinking light
----------------------------

Document example...

.. _Arduino.cc: https://www.arduino.cc/
.. _official Arduino installation instructions: http://playground.arduino.cc/Linux/Ubuntu
.. _jaway post on Ubuntu and Arduino: http://www.jayway.com/2011/10/08/arduino-on-ubuntu-without-ide/

.. author:: default
.. categories:: none
.. tags:: ubuntu 14.04, arduino, diy
.. comments::

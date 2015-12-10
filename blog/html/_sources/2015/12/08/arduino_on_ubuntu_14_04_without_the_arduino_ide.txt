Arduino on Ubuntu 14.04 without the Arduino IDE
===============================================

In this post I will document my setup for working with an Arduino Uno on Ubuntu
14.04. You can learn more about the Arduino at `Arduino.cc`_ if you are
unfamiliar with the microcontroller.  However, **be warned**, I am not going to
use the official Arudino IDE, if you'd like the official setup checkout the
`official Arduino installation instructions`_. Instead I'm going to setup the
basic requirements for writing and pushing code, including libraries and make
files, and use *vim* as my editor. So, if you're interested in this approach,
follow along.

.. more::

First, I'll make a few comments on why I want to use this setup instead of the
standard Arduino IDE (if these don't make sense to you, you should probably not
use this guide:)

* This setup will use standard c++ coding instead of the Arduino \*.ino
  variant used with Arduino IDE.
  As a result, code will have to be slightly modified from examples you'll find
  at the Arduino website or elsewhere on the web. Header files will have to be
  included, loops made explicit, etc. Also, instead of clicking buttons
  on the Arduino IDE to compile code and push to the Arduino you'll have to use
  **make** files, as in :code:`$ make` and :code:`$ make upload`. So, this
  becomes standard c++ coding with an upload step-- this can be good, or bad,
  depending on your experience.
* The Arduino IDE requires Java 6, an old version of Java, be installed for
  use-- I really don't want to deal with this requirement and I'm very happy
  coding with *vim* and using *make* at the terminal.


Credits
-------

I'll be using this nice (but old--2011!) post on jayway--
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
needed libraries-- say **Y** to all the dependencies. All of Arduino-specific
libraries and documentation is located in the following set of directories
once the install is complete::

    /usr/share/arduino
    /usr/share/doc/arduino-core
    /usr/share/doc/arduino-mk

Check these directories out to see what's included and be sure to try out the
examples (however, as noted above, we'll have to modify the code a bit to work
with our setup-- I'll do an example later):

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

**Finding your port--**
you've connected the Arduino to your computer via usb and can see
that the board is recognized using :code:`lsusb`-- an example looks like:

.. code:: bash

    $ lsusb
    Bus 001 Device 002: ID 8087:8000 Intel Corp.
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 003 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 002 Device 003: ID 174f:14a1 Syntek
    Bus 002 Device 002: ID 8087:07dc Intel Corp.
    Bus 002 Device 004: ID 2341:0043 Arduino SA Uno R3 (CDC ACM)
    Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

Notice the Arduino Uno on the second-to-last line.  Okay, what port is it on?
We need to know the port for uploading code to the Arduino. Often the port is
:code:`/dev/ttyACM0` or something similar-- how do we find this?  The best
method I've found is using a combination of :code:`dmesg` and :code:`grep`--
when the Arduino is connected, try:

.. code:: bash

    $ dmesg | grep Arduino -C 3
    [ 6433.058276] usb 2-2: new full-speed USB device number 4 using xhci_hcd
    [ 6433.077095] usb 2-2: New USB device found, idVendor=2341, idProduct=0043
    [ 6433.077104] usb 2-2: New USB device strings: Mfr=1, Product=2, SerialNumber=220
    [ 6433.077110] usb 2-2: Manufacturer: Arduino (www.arduino.cc)
    [ 6433.077114] usb 2-2: SerialNumber: 75439333335351105031
    [ 6433.077340] usb 2-2: ep 0x82 - rounding interval to 1024 microframes, ep desc says 2040 microframes
    [ 6433.106521] cdc_acm 2-2:1.0: ttyACM0: USB ACM device

Notice the last line in the output, giving :code:`ttyACM0` as the port in my
case-- yours might be different. If you just run :code:`dmesg` there is a ton
of output. This is why I pipe it to :code:`grep`, searching for *Arduino*. The
argument :code:`-C 3` provides *three lines of context*-- you can increase, or
decrease this number to get more/less info if the port is not immediately
obvious. Okay, that's my approach -- **do you know a better way to do this?**--
please leave a comment below!

**dialout group and permissions--**
One of the issues many users seem to have using Arduino with Ubuntu is getting
the usb permissions to work. When the Arduino **is connected**, we can inspect
the properties of the usb port (hopefully found above):

.. code:: bash

    $ ls -l /dev/ttyACM0
    crw-rw---- 1 root dialout 166, 0 Dec  9 11:39 /dev/ttyACM0

Notice that the *group* is dialout-- we will use that in a second.  However,
when the Arduino **is not connected**, the same command will give an error:

.. code:: bash

    $ ls -l /dev/ttyACM0
    ls: cannot access /dev/ttyACM0: No such file or directory


Now, to allow access to the usb port we add our (your) username to the dialout
group-- be sure to **change username** below:

.. code:: bash

   $ sudo adduser username dialout

The above command accomplishes the same thing as adding the username to the
file :code:`/etc/group`, as discussed by Havard in his/her comments.  Also,
you'll have to **logoff and logon** for the group changes to take effect.

Okay, take a deep breath, everything is setup-- let's try implementing the
blinking light example, as detailed in my motivational post.

An example -- blinking light
----------------------------

As an example, let's do the standard blinking led example. We can use pin 13 to
blink an led on the board, so no circuit to build.  In this way we can focus
on the difference between the Arduino \*.ino files and the \*.cc files we'll be
using.  The examples directory, mentioned above, has this example in
:code:`/usr/share/arduino/examples/01.Basics/Blink/Blink.ino` -- replicated
here (with minor formatting):

.. code:: cpp

    //  Blink.ino
    //
    //  Turns on an LED on for one second,
    //  then off for one second, repeatedly.
    //
    //  This example code is in the public domain.

    // Pin 13 has an LED connected on most
    // Arduino boards.
    int led = 13;

    // the setup routine runs once when you press reset
    void setup() {
      // initialize the digital pin as an output.
      pinMode(led, OUTPUT);
    }

    // the loop routine runs over and over
    void loop() {
      // turn the LED on (HIGH is the voltage level)
      digitalWrite(led, HIGH);

      // wait for a second
      delay(1000);

      // turn the LED off by making the voltage LOW
      digitalWrite(led, LOW);

      // wait for a second
      delay(1000);     
    }

The above code can be compiled and uploaded to the Arduino as-is *if you are
using the Arduino IDE*.  However, we are not. So, we modify the above to make
it standard c++ and call the file :code:`main.cc`:

.. code:: cpp

    //  main.cc -- from Blink.ino
    //
    //  Turns on an LED on for one second,
    //  then off for one second, repeatedly.
    //
    //  This example code is in the public domain.
    
    // include Arduino.h header file
    #include <Arduino.h>
    
    // Pin 13 has an LED connected on most
    // Arduino boards.
    int led = 13;
    
    // the setup routine runs once when you press reset
    void setup() {
      // initialize the digital pin as an output.
      pinMode(led, OUTPUT);
    }
    
    // the loop routine runs over and over
    void loop() {
      // turn the LED on (HIGH is the voltage level)
      digitalWrite(led, HIGH);
    
      // wait for a second
      delay(1000);
    
      // turn the LED off by making the voltage LOW
      digitalWrite(led, LOW);
    
      // wait for a second
      delay(1000);     
    }
    
    // main function
    int main(void) {
      // call init()
      init();
    
      // make explicit call to setup()
      setup();
    
      // use a for-loop -- to make loop
      for (;;) {
        loop();
      }
    }

If we compare the two versions there are only a few differences:

* :code:`main.cc` adds the :code:`#include <Arduino.h>` statement
* :code:`main.cc` adds a :code:`main()` function that initializes with a
  call to :code:`init()`, explicitly calls the :code:`setup()` function and
  then uses a never-ending :code:`for` loop to repeatedly call the
  :code:`loop()` function.

All of these changes make a lot of sense to c++ coder. Finaly, a fairly
minimal :code:`makefile` (literally name the file :code:`makefile`) looks like
this::

    ARDMK_DIR = /usr/share/arduino
    ARDUINO_PORT = /dev/ttyACM0
    BOARD_TAG = uno
    include $(ARDMK_DIR)/Arduino.mk

Most of the heavy-lifting is done by :code:`Arduino.mk`, as seen by the
inclusion of this file.  The :code:`BOARD_TAG = uno` is not required because
the default is :code:`uno`-- if you're using another board you'll have to
change this.  The :code:`ARDUINO_PORT` **is important**-- this must be correct
and permissions need to be assigned (as discussed above) for the upload to work.
So, getting ready to compile and upload, we put these two files in a directory,
say::

    blink_pin13/
    ├── main.cc
    └── makefile

To compile open the terminal and navigate to the directory and use make:

.. code:: bash

    $ make

Assuming that everything went well the code can be uploaded to the Arduino
using:

.. code:: bash

   $ make upload

That's it we're Arduino-ing!  Try changing the amount of time that the led is
off/on followed by:

.. code:: bash

   $ make clean
   $ make
   $ make upload

to see the changes.

Finally, all of the code for this example is available at my github account---
see `blinking lights at github`_.

Wrapping Up
-----------

As always-- if you find typos, mistakes, or have suggestions or questions
please leave a comment below. I'd also be interested to find out about
different approaches to setup-- if you have one, leave a comment and/or 
link to your ideas.

.. _Arduino.cc: https://www.arduino.cc/
.. _official Arduino installation instructions: http://playground.arduino.cc/Linux/Ubuntu
.. _jaway post on Ubuntu and Arduino: http://www.jayway.com/2011/10/08/arduino-on-ubuntu-without-ide/
.. _blinking lights at github: https://github.com/cstrelioff/arduino-sketches/tree/master/blink_pin13

.. author:: default
.. categories:: none
.. tags:: ubuntu 14.04, arduino, diy
.. comments::

.. _installing-pysoundfile:

Installing PySoundFile on Ubuntu 14.04
======================================

In this post I will go over installing PySoundFile using **pip** and
**virtualenvwrapper**.  PySoundFile is a utility for reading and writing sound
files of various types, like **wav**, **flac** and **ogg** using the abilities
of the `libsndfile`_ library. Noticeably absent is **mp3** due to the license
issue-- use a tool like (the wonderful) `sox`_ to convert mp3's to a supported
file type. See

* `PySoundFile Docs`_
* `PySoundFile github`_ 

for more details about PySoundFile.

**2015, June 16--** I have new post on installing PySoundFile for use with
Python 3.4-- :ref:`pysoundfile-python3`, check it out. There are also some
updates to package, that affect the Python 2.7.6 install done in this post, so
I'll show how to upgrade below, if you need to do that. **--End edit.**

.. more::

Using **pip** to install Python packages comes with some difficulties-- we have
to worry about all the dependencies.  Of course, the benefit is that we can
install current package versions and software that is not in the Ubuntu
repositories, like PySoundFile. So, the dependencies for PySoundFile are

* `libsndfile`_
* `cffi`_
* `numpy`_

We start by making sure that all of the Python development requirements are
installed using :code:`apt-get` :

.. code:: bash

    $ sudo apt-get install build-essential python-dev

Next, make sure that we have gfortran:

.. code:: bash

    $ sudo apt-get install gfortran

And, linear algebra libraries:

.. code:: bash

    $ sudo apt-get install libatlas-dev liblapack-dev


Next, for the `libsndfile`_ requirement we do

.. code:: bash

    $ sudo apt-get install libsndfile1

Finally, for the Ubuntu-specific installs, we install the `cffi`_ requirements:

.. code:: bash

    $ sudo apt-get install libffi-dev 

Now we get to the Python installs using **pip**.  I will do all of this
in a virtual environment using **virtualenvwrapper**. If you need help getting
these installed, see these posts:

* :ref:`initial python setup` -- use this post to see how to install **pip**
* :ref:`virtualenvs on ubuntu 14.04` -- use this post to install **virtualenv**
  and **virtualenvwrapper** (and see how to use virtual environments)

Assuming everything is in order, we create a virtual environment called
*sounds* (of course, you can call it whatever you like):

.. code:: bash

    $ mkvirtualenv sounds
    New python executable in sounds/bin/python
    Installing setuptools, pip...done.
    (sounds)$ 
    
Next, we install :code:`PySoundFile`, which will also install :code:`cffi`,
:code:`pycparser` (a dependency of :code:`cffi`) and :code:`numpy`-- expect lots
of compiling here:

.. code:: bash

    (sounds)$ pip install PySoundFile
    
    ... lots of compilation ...

    Successfully installed PySoundFile numpy cffi pycparser
    Cleaning up...
    (sounds)$ 

Next, checkout the package information using **pip**

.. code:: bash

    (sounds)$ pip show PySoundFile
    ---
    Name: PySoundFile
    Version: 0.6.0
    Location: /home/cstrelioff/virtenvs/sounds/lib/python2.7/site-packages
    Requires: numpy, cffi

**2016, June 16--** PySoundFile version 0.7 has changed the import name of the
package from :code:`pysoundfile` to :code:`soundfile`, so the code as
originally posted here breaks.  Let's upgrade the package to version 0.7 and
change the code below. To upgrade using pip simply type

.. code:: bash

    (sounds)$ pip install --upgrade PySoundFile

and check the version:

.. code:: bash

	(sounds)$ pip show PySoundFile
	---
	Name: PySoundFile
	Version: 0.7.0
	Location: /home/cstrelioff/virtenvs/sounds/lib/python2.7/site-packages
	Requires: numpy, cffi

**--End edit.**

And, to make sure that it loads in Python let's import and try out a few
things.  First, print out the version, this should agree with the information
from above:



.. code-block:: python

    from __future__ import print_function
    import soundfile as sf
    
    print("PySoundFile version: {}".format(sf.__version__))
    

::

    PySoundFile version: 0.7.0
    
    



Next, let's see what file types we can read and write:


.. code-block:: python

    for key, val in sf.available_formats().items():
        print("{:5s} -- desc: {}".format(key, val))
    

::

    MAT4  -- desc: MAT4 (GNU Octave 2.0 / Matlab 4.2)
    MAT5  -- desc: MAT5 (GNU Octave 2.1 / Matlab 5.0)
    FLAC  -- desc: FLAC (FLAC Lossless Audio Codec)
    SD2   -- desc: SD2 (Sound Designer II)
    AIFF  -- desc: AIFF (Apple/SGI)
    PAF   -- desc: PAF (Ensoniq PARIS)
    CAF   -- desc: CAF (Apple Core Audio File)
    W64   -- desc: W64 (SoundFoundry WAVE 64)
    RAW   -- desc: RAW (header-less)
    PVF   -- desc: PVF (Portable Voice Format)
    NIST  -- desc: WAV (NIST Sphere)
    WVE   -- desc: WVE (Psion Series 3)
    RF64  -- desc: RF64 (RIFF 64)
    XI    -- desc: XI (FastTracker 2)
    MPC2K -- desc: MPC (Akai MPC 2k)
    IRCAM -- desc: SF (Berkeley/IRCAM/CARL)
    AU    -- desc: AU (Sun/NeXT)
    SVX   -- desc: IFF (Amiga IFF/SVX8/SV16)
    WAV   -- desc: WAV (Microsoft)
    SDS   -- desc: SDS (Midi Sample Dump Standard)
    VOC   -- desc: VOC (Creative Labs)
    HTK   -- desc: HTK (HMM Tool Kit)
    AVR   -- desc: AVR (Audio Visual Research)
    OGG   -- desc: OGG (OGG Container format)
    WAVEX -- desc: WAVEX (Microsoft)
    
    



That's pretty good, with all the usual suspects (except for mp3's, for reasons
stated above).  From the `PySoundFile Docs`_, typical read/write goes something
like this:

.. code:: python

	# read an existing wav file
	data, samplerate = sf.read('existing_file.wav')
	
	# write the data to a new ogg file
	sf.write(data, 'new_file.ogg', samplerate=samplerate)


Note that :code:`data` returned by :code:`sf.read()` is already a
:code:`numpy` array, so compute away!

I think that's it for this post.  As always, leave comments and I'll get to them
as soon as I can.

.. _PySoundFile Docs: http://pysoundfile.readthedocs.org/en/ 
.. _PySoundFile github: https://github.com/bastibe/PySoundFile

.. _sox: http://sox.sourceforge.net/ 

.. _libsndfile: http://www.mega-nerd.com/libsndfile/
.. _cffi: http://cffi.readthedocs.org/en/latest/
.. _numpy: http://www.numpy.org/

.. author:: default
.. categories:: none
.. tags:: python, audio, music, sound, PySoundFile
.. comments::

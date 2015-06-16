.. _pysoundfile-python3:

PySoundFile and Python 3.4 on Ubuntu 14.04
==========================================

In a previous post, :ref:`installing-pysoundfile`, I went over installing
PySoundFile on Ubuntu 14.04 using the default version of Python-- that's
version 2.7.6.  In this post I'll cover the use of Python 3.4 in a virtual
environment-- the goal here, at least in the long run, is to write audio
processing (dsp) code in Python that is version 2- and 3-compatible.

.. more::

Dependencies
------------

To start, the :ref:`previous post <installing-pysoundfile>` should be consulted
to make sure that the Ubuntu-specific requirements are fulfilled.  If you've
already setup PySoundFile for Python 2.7.6 as described in that post you are
off to a good start, if not read through all of the :code:`sudo apt-get install`
commands to see if you need to install any libraries, compilers or other
packages. Also, make sure that you have :code:`python3-dev` installed using

.. code:: bash

    $ sudo apt-get install python3-dev


virtualenv
----------

When setting up PySoundFile for Python 2.7.6, we called the virtual environment
**sounds**, so let's call this environment **sounds3**.  To setup the
environment use:

.. code:: bash

    $ mkvirtualenv sounds3 -p /usr/bin/python3

This should create the environment, reflected by a change in prompt to
something similar to :code:`(sounds3)$`. Try the following to make sure that
the basics are setup:

.. code:: bash

    (sounds3)$ python --version
    Python 3.4.0
    (sounds3)$ pip list
    pip (1.5.6)
    setuptools (3.6)

PySoundFile
-----------

Next, we install PySoundFile using pip (this will download a fair number of
packages and do lots of compiling--mainly numpy-- so, be patient):

.. code::

     (sounds3)$ pip install PySoundFile

Now, if we list the packages in our virtual environment we get:

.. code:: bash

    (sounds3)$ pip list
    cffi (1.1.2)
    numpy (1.9.2)
    pip (1.5.6)
    pycparser (2.14)
    PySoundFile (0.7.0)
    setuptools (3.6)

Finally, let's do the same test we did for the Python 2.7.6 install. First,
test the import and version


.. code-block:: python

    from __future__ import print_function
    import soundfile as sf
    
    print("PySoundFile version: {}".format(sf.__version__))
    

::

    PySoundFile version: 0.7.0
    
    



then, print out the supported audio formats:


.. code-block:: python

    for key, val in sf.available_formats().items():
        print("{:5s} -- desc: {}".format(key, val))
    

::

    IRCAM -- desc: SF (Berkeley/IRCAM/CARL)
    WAV   -- desc: WAV (Microsoft)
    AU    -- desc: AU (Sun/NeXT)
    W64   -- desc: W64 (SoundFoundry WAVE 64)
    CAF   -- desc: CAF (Apple Core Audio File)
    SD2   -- desc: SD2 (Sound Designer II)
    WVE   -- desc: WVE (Psion Series 3)
    AVR   -- desc: AVR (Audio Visual Research)
    SDS   -- desc: SDS (Midi Sample Dump Standard)
    RAW   -- desc: RAW (header-less)
    WAVEX -- desc: WAVEX (Microsoft)
    HTK   -- desc: HTK (HMM Tool Kit)
    RF64  -- desc: RF64 (RIFF 64)
    SVX   -- desc: IFF (Amiga IFF/SVX8/SV16)
    MPC2K -- desc: MPC (Akai MPC 2k)
    MAT5  -- desc: MAT5 (GNU Octave 2.1 / Matlab 5.0)
    FLAC  -- desc: FLAC (FLAC Lossless Audio Codec)
    NIST  -- desc: WAV (NIST Sphere)
    OGG   -- desc: OGG (OGG Container format)
    MAT4  -- desc: MAT4 (GNU Octave 2.0 / Matlab 4.2)
    VOC   -- desc: VOC (Creative Labs)
    PAF   -- desc: PAF (Ensoniq PARIS)
    PVF   -- desc: PVF (Portable Voice Format)
    AIFF  -- desc: AIFF (Apple/SGI)
    XI    -- desc: XI (FastTracker 2)
    
    



Okay, that's it.  For more information checkout:

* `PySoundFile Docs`_
* `PySoundFile github`_
* `sox`_ -- for converting your mp3s to supported audio formats.

As always questions, comments, and corrections are welcome.

.. _PySoundFile Docs: http://pysoundfile.readthedocs.org/en/ 
.. _PySoundFile github: https://github.com/bastibe/PySoundFile
.. _sox: http://sox.sourceforge.net/ 

.. author:: default

.. categories:: none
.. tags:: python, python 3.4, audio, music, sound, PySoundFile
.. comments::

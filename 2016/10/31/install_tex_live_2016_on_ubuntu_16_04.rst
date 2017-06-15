.. _texlive 2016 ubuntu 16.04:

Install TeX Live 2016 on Ubuntu 16.04
=====================================

On Ubuntu 14.04 I went through a fairly involved procedure to get the current
TeX Live (TeX Live 2013 at that time) installed because it was not in the
standard repository. However, it seems that there is now a much easier way to
get TeX Live 2016: *J Fernyhough* has put together a `TeX Live 2016 PPA`_ --
kudos to him!

.. more::

update
......

**2017, June** The original ppa used in this post seems to be transitioning to
TeX Live 2017, breaking my setup in the process. So, I will purge this ppa and
try to install the TeX Live 2016 ppa. So, the two options are:

1. If you are installing TeX Live 2016 for the first time on Ubuntu 16.04 *and
   did not use the previous version of this post* (see 'historical reference'
   below), use the **first-time install** section below.
2. If you, like me, installed Tex Live using the :code:`ppa:jonathonf/texlive`
   and are now having problems, use the **switching to new ppa** section.

first-time install
..................

This section assumes you are doing a fresh install of Tex Live 2016 and have
not used older install instructions. Be sure to have a good internet connection
(the install is GBs) and type:

.. code-block:: bash

  $ sudo add-apt-repository ppa:jonathonf/texlive-2016
  $ sudo apt update
  $ sudo apt install texlive-full

That should be it-- a very complete and current install of TeX Live 2016 is
installed.

switching to new ppa
....................

This section assumes that you have previously installed TeX Live 2016 on Ubuntu
16.04 using :code:`ppa:jonathonf/texlive` instead of the ppa used above-- I
did this in the original post-- see the *historical reference* below. If that's
true, this is what I did to update:

**purge ppa--**

First, I will purge :code:`ppa:jonathonf/texlive` following standard
procedures--

.. code-block:: bash

  $ sudo apt install ppa-purge
  $ sudo ppa-purge ppa:jonathonf/texlive

This gave errors...hmm; unmet dependencies.

**new ppa--**

Install :code:`ppa:jonathonf/texlive-2016` as follows:

.. code-block:: bash

  $ sudo add-apt-repository ppa:jonathonf/texlive-2016
  $ sudo apt update
  $ sudo apt install texlive-full

This still results in errors, but we can fix them as follows:

**resolving errors--**

Following the guidance in the error output, try a fix install:

.. code-block:: bash

  $ sudo apt-get -f install

followed by

.. code-block:: bash

  $ sudo apt-get update
  $ sudo apt-get upgrade

This should fix the unmet dependencies issues and running an
:code:`apt-get update` should work without error.

Finally, try the install again:

.. code-block:: bash

  $ sudo apt install texlive-full

and the install should proceed as normal-- again, this is a large (GBs)
install.

historical reference
....................

**Don't do this**, *left for reference*

Given this new PPA the install is very simple-- just add the PPA, update and
install following `How to Install TeX Live 2016 in Ubuntu 16.04, 14.04`_.
However, note that this is a **huge install** (GBs). So, make sure to do try
this when you have access to a decent connection, and run the following at the
terminal:

.. code-block:: bash

  $ sudo add-apt-repository ppa:jonathonf/texlive
  $ sudo apt update
  $ sudo apt install texlive-full

That's it! Much better than the manual procedure I used in the past.

.. _TeX Live 2016 PPA: https://launchpad.net/~jonathonf/+archive/ubuntu/texlive-2016
.. _How to Install TeX Live 2016 in Ubuntu 16.04, 14.04: http://tipsonubuntu.com/2016/09/16/install-tex-live-2016-ubuntu-16-04-14-04/

.. author:: default
.. categories:: none
.. tags:: LaTeX, ubuntu 16.04
.. comments::

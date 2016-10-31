.. _texlive 2016 ubuntu 16.04:

Install TeX Live 2016 on Ubuntu 16.04
=====================================

On Ubuntu 14.04 I went through a fairly involved procedure to get the current
TeX Live (TeX Live 2013 at that time) installed because it was not in the
standard repository. However, it seems that there is now a much easier way to
get TeX Live 2016: *J Fernyhough* has put together a `TeX Live 2016 PPA`_ --
kudos to him!

.. more::

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

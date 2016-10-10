dropbox on Ubuntu 16.04
=======================

This a very brief post on installing `dropbox`_ on Ubuntu 16.04, mainly to 
remind myself how I got it working.  In the end, it's the most straightforward
approach, **but not the one I found at** `dropbox linux install instructions`_.
So, be careful.

.. more::

Turns out the install is a simple apt-get:

.. code-block:: bash

  $ sudo apt-get nautilus-dropbox 

You'll have to enter your `dropbox`_ credentials and restart nautilus, but
everything seems to be working fine.

Kudos to *edwinksl* and *Thanos A* for their answers/suggestions on this
`askubuntu post`_. As noted by Thanos, if you followed the process given at
`dropbox`_ you should delete the :code:`~/.dropbox` and
:code:`~/.dropbox-dist` directories before doing the apt-get install provided
above.

.. _dropbox: https://www.dropbox.com/
.. _dropbox linux install instructions: https://www.dropbox.com/install-linux
.. _askubuntu post: http://askubuntu.com/questions/787138/cant-install-dropbox-after-upgrading-to-16-04-lts


.. author:: default
.. categories:: none
.. tags:: dropbox, ubuntu 16.04
.. comments::

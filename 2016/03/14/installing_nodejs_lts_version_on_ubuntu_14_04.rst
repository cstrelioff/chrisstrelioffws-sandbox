.. _install-node-lts:

Installing nodejs LTS version on Ubuntu 14.04
=============================================

In a previous post, :ref:`install-node-ver1`, I installed nodejs on Ubuntu 14.04
using what were current instructions at the time. Those notes are outdated at
this point so I thought I'd document the current way to install the LTS version
of node.

.. more::

To install we will be following the (very brief) guide at
`debian node install`_ -- this uses a simple curl/bash combination to setup a
PPA for the LTS version of node (currently ver 4.4.0). Installation is as simple
as:

.. code:: bash

    $ curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -
    $ sudo apt-get install -y nodejs

This sets you up for automatic updates of the version 4.2+ LTS version of 
node-- an active LTS through April 2017, according to the
`node LTS schedule`_. Once the install is complete, you can find out versions
of node and npm using:

.. code:: bash

    $ node --version
    v4.4.0
    $ npm --version
    2.14.20

Of course, your versions might be different if you install later.

Geting started
--------------

If you are new to nodejs -- I'm still pretty new -- you should look into 

* `nodeschool`_ is a place to learn about node, with local meetings that you
  can attend if you are lucky. I've been to the `Oakland nodeschool`_ and
  found it really useful.
* Self-directed node lessons are available in the `node workshopper list`_, 
  starting with basic javascript and moving on to more advanced topics ranging
  from Reactjs to the Web Audio API. These are installed using **npm** and
  pretty easy to use. Also, these lessons form the basis for the `nodeschool`_
  meetings, providing the basis for learning all things javascript and node.

That's it for this short post. Please leave comments if you have issues or
other ideas on how to get started learning nodejs-- I'd love to see them!

.. _node workshopper list: http://nodeschool.io/#workshopper-list
.. _Oakland nodeschool: http://nodeschool.io/oakland/
.. _nodeschool: http://nodeschool.io/
.. _node LTS schedule: https://github.com/nodejs/LTS#lts_schedule
.. _debian node install: https://github.com/nodesource/distributions#debinstall

.. author:: default
.. categories:: none
.. tags:: javascript, nodejs, npm
.. comments::

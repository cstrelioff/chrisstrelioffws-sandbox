.. _install-node-lts:

Installing node LTS version on Ubuntu 14.04
===========================================

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

sudo-free global installs
-------------------------

**2016, July**

I'm adding this (I think) really important part to allow for npm
install of packages without sudo -- this means it's in a non-destructive place
that we have to setup. This approach is suggested by the (very nice) npm docs--
`see here <https://docs.npmjs.com/getting-started/fixing-npm-permissions>`_ --
I'll be using "Option 2" described there.  To start, we make a
directory to hold our global installs:

.. code:: bash

    $ mkdir ~/.npm-global

Next, we tell npm about this new location:

.. code:: bash

    $ npm config set prefix '~/.npm-global'

Finally, we have to update our path for bash. The npm docs suggest doing this
in ~/.profile, but I will do this in ~/.bashrc (this is loaded by ~/.profile
on Ubuntu machines). So, in ~/.bashrc add this line (at the end of the file
is fine)

.. code:: bash

    # add path for npm global installs
    export PATH=~/.npm-global/bin:$PATH

I've added the comment so that I/we can remember what this is for (if it isn't
obvious from the name).  Finally, source ~/.bashrc like so

.. code:: bash

    $ source ~/.bashrc

And we should be set; global install without sudo. If you'd like to test it out,
install jshint globally with:

.. code:: bash

    $ npm install -g jshint

You should see that it is using the new location.

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

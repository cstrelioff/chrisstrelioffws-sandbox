Install and setup git on Ubuntu 14.04
=====================================

Here we install and do the most basic setup for git_.  First, install git_ from
the Ubuntu repository:

.. code-block:: bash

    $ sudo apt-get install git

.. more::
    
Next, tell git_ about yourself (*make sure to use your real name and email*):

.. code-block:: bash

    $ git config --global color.ui true
    $ git config --global user.name "Your Name"
    $ git config --global user.email "your.name@email.com"

That's it, you're ready to go.  Also, checkout this  nice `git reference`_.

.. _git: http://git-scm.com/
.. _git reference: http://gitref.org/

.. author:: default
.. categories:: none
.. tags:: git, ubuntu 14.04, my ubuntu setup
.. comments::

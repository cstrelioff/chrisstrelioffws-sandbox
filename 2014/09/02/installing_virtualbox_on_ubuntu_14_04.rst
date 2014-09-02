Installing virtualbox on Ubuntu 14.04
=====================================

In this post I will cover installing Oracle's `virtualbox`_ on Ubuntu 14.04.
This will allow me to run Windows and `tableau`_, a program for putting together
interactive visualizations.  If you are running Ubuntu and taking
`Coursera's introduction to data science`_ class you might find this post useful
as well.  However, having `virtualbox`_ installed and available is always a good
thing for those situations where Win or Mac are the only options.

.. more::

I'll be following the `installation instructions at virtualbox.org`_, so you
can also check there for more information. The first step is to add the
repository for the Ubuntu 14.04 version:

.. code-block:: bash

    $ sudo add-apt-repository "deb http://download.virtualbox.org/virtualbox/debian trusty contrib"

Next, download and add the key for apt-secure using:

.. code-block:: bash

    $ wget -q https://www.virtualbox.org/download/oracle_vbox.asc -O- | sudo apt-key add -

Finally, we update and install using:

.. code-block:: bash

    $ sudo apt-get update
    $ sudo apt-get install virtualbox-4.3

The download and install will take a bit of time because virtualbox is about
70MB. **Note:** this also installs **dkms**, as suggested in the original
instructions. Finally, we want to install the virtualbox extensions. I
downloaded the latest version at this time::

    Oracle_VM_VirtualBox_Extension_Pack-4.3.14-95030.vbox-extpack

and installed from the terminal using (you'll asked for your password if you
don't use sudo):

.. code-block:: bash

    $ VBoxManage extpack install Oracle_VM_VirtualBox_Extension_Pack-4.3.14-95030.vbox-extpack

You can test the extension is installed using:

.. code-block:: bash

    $ VBoxManage list extpacks

The response should be something like::

    Extension Packs: 1
    Pack no. 0:   Oracle VM VirtualBox Extension Pack
    Version:      4.3.14
    Revision:     95030
    Edition:      
    Description:  USB 2.0 Host Controller, Host Webcam, VirtualBox RDP, PXE ROM
    with E1000 support.
    VRDE Module:  VBoxVRDP
    Usable:       true 
    Why unusable: 


That's it, `virtualbox`_ is installed and ready to go.  Just bring up the
*dash* and type ``virtualbox``, then click on the icon.  Of course, you lock it
to the launcher if you like.

At this point you can install windows from an image, official media, or other
source. I'll be using a version of windows 7 that I bought for occasions just
like this.  Checkout the `virtualbox first steps guide`_ for help setting up
your virtual machine and installing the OS.

.. _virtualbox: https://www.virtualbox.org/
.. _installation instructions at virtualbox.org: https://www.virtualbox.org/wiki/Linux_Downloads
.. _tableau: http://www.tableausoftware.com/
.. _Coursera's introduction to data science: https://www.coursera.org/course/datasci
.. _ie virtual machine: https://www.modern.ie/en-us/virtualization-tools#downloads
.. _virtualbox first steps guide: http://www.virtualbox.org/manual/ch01.html

.. author:: default
.. categories:: none
.. tags:: ubuntu 14.04, virtualbox, my ubuntu setup, coursera intro to data science, tableau
.. comments::


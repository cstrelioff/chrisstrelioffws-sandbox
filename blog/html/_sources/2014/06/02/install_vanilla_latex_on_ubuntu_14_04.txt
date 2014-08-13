Install vanilla LaTeX on Ubuntu 14.04
=====================================

In this post I will go through a vanilla installation of Tex Live-- **you may
not want to do this**.  I'm choosing this installation method because of the
ability to stay current with LaTeX updates and greater flexibility.  However,
for most people I would suggest installing the LaTeX setup in Ubuntu 14.04
repositories-- search for ``texlive-full``.

.. more::

I will do the vanilla installation following the very thorough guide provided
here: `vanila LaTeX at stackexchange`_.  The guide is for Ubuntu 12.10 but
I'll be doing this on Ubuntu 14.04. This will install **TeX Live 2013**, which
is scheduled to be replaced by TeX Live 2014 in July 2014.  However, TeX Live
2013 is the current implementation at this point.

First, get the installer:

.. code-block:: bash

    $ wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
    $ tar -xzf install-tl-unx.tar.gz

This will create the directory ``install-tl-***`` where ``***`` will be numbers
(looks like a date to me) that depends on when you try this installation. Next,
change into the directory and start the installer.  For me, this was:

.. code-block:: bash

    $ cd install-tl-20140417
    $ sudo ./install-tl

This will start the installer and you can specify the options you like.  I took
this opportunity to set the default paper size to letter instead of A4.
Once satisfied, press **I** to start the install-- *this will take quite a
while (hours) due to the large size of the distribution*.

Path for LaTeX
--------------

If you type:

.. code-block:: bash

    $ pdflatex --version

at this point Ubuntu will still not know where to find the installation and
suggest that you install something from the repository.  To fix this, we create
a link:

.. code-block:: bash

    $ sudo ln -s /usr/local/texlive/2013/bin/* /opt/texbin

Then, we add the path to our environment file (I'll use vim, but you can use
nano, emacs, etc.):

.. code-block:: bash

    $ sudo vim /etc/environment

Before the edit, I had the following in environment::

    PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games"

which I change, to add our path::

    PATH="/opt/texbin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games"

Now, to get these changes working you have to **logout**.  When you login
again, try the following to make sure that the changes worked:

.. code-block:: bash

    $ which tex
    /opt/texbin/tex

Telling Ubuntu LaTeX is installed
---------------------------------

Now, because we didn't use ``apt-get`` to install Tex Live, Ubuntu needs to be
told that it's installed.  This can be accomplished with the ``equivs`` package
in the Ubuntu repository:

.. code-block:: bash

    $ sudo apt-get install equivs --no-install-recommends
    $ mkdir /tmp/tl-equivs
    $ cd /tmp/tl-equivs
    $ equivs-control texlive-local

This will create the ``texlive-local`` file.  An example of what the contents
of this fill should look like is here: `debian-equivs-2013-ex.txt`_.  I copied
the contents into my ``texlive-local`` and changed the maintainer information
to my details. Finally, we create this fake Debian package and install:

.. code-block:: bash

    $ equivs-build texlive-local
    $ sudo dpkg -i texlive-local_2013-1_all.deb

Updating LaTeX
--------------

The Tex Live manager, **tlmgr**, can be used from the terminal as described in
this post: `vanila LaTeX at stackexchange`_.  However, the full path will have
to used.  For example:

* Update all packages that can be updated:

.. code-block:: bash

    $ sudo /usr/local/texlive/2013/bin/x86_64-linux/tlmgr update --all

* List packages that can be updated:

.. code-block:: bash

    $ sudo /usr/local/texlive/2013/bin/x86_64-linux/tlmgr update --list

If you try either of the above commands at this date (June 2014) you will be
told that TeX is *frozen* and no updates are allowed.  This is done each year
as the new TeX Live release is assembled and tested.

Finally, this install can moved to use TeX Live 2014 when it is released.  See
the notes here: `vanila LaTeX at stackexchange`_.

.. _vanila LaTeX at stackexchange: http://tex.stackexchange.com/a/95373
.. _debian-equivs-2013-ex.txt: http://www.tug.org/texlive/files/debian-equivs-2013-ex.txt

.. author:: default
.. categories:: none
.. tags:: LaTeX, my ubuntu setup
.. comments::

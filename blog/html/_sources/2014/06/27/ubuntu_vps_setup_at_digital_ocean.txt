.. _VPS setup at digitalocean:

Ubuntu VPS setup at digital ocean
=================================

This blog is hosted on an Ubuntu 14.04 VPS at `digital ocean`_. This post is
mainly *a reminder for me* of the tutorials I used to set things up, however
you might find it a helpful guide as well.

.. more::

* `initial server setup`_

As you might expect, this is the place to start after you've created a
*droplet* and received a password from `digital ocean`_.

* `ssh key setup`_

Next, I setup my ssh key using a unique ssh port (call it **XXXX**) and
a non-default identity file **identity.pub**. My command to copy my key
to the server was then of the form:

.. code-block:: bash
    
    $ ssh-copy-id -i ~/.ssh/identity.pub -p XXXX username@xxx.xxx.xxx.xx

Once setup, the ssh command is:

.. code-block:: bash

    $ ssh -i ~/.ssh/identity.pub -p XXXX username@xxx.xxx.xxx.xx

To save myself from typing this every time, I added this identity to my
**~/.ssh/config** file with an entry like:

.. code-block:: bash

    Host           christrelioff.ws 
    HostName       xxx.xxx.xxx.xx                                                 
    Port           XXXX                                                   
    IdentityFile   ~/.ssh/identity
    User           username

This allows me to ssh with the simple command (tab auto-complete works too):

.. code-block:: bash

    $ ssh chrisstrelioff.ws

and the correct port, identity file, etc are used.

* `setup a firewall`_

  Next, I setup a firewall using ufw_. The install is simple:

.. code-block:: bash

    $ sudo apt-get install ufw

Once installed, the status can be seen using the command:

.. code-block:: bash

    $ sudo ufw status

At this point there should be nothing to see-- simply a notification that the
status is inactive.  So, let's set some default policies:

.. code-block:: bash

    $ sudo ufw default deny incoming
    $ sudo ufw default allow outgoing

This denies everything incoming and allows all outgoing by default. Next, we
must allow incoming **ssh**.  By default **ssh** uses port 22 and the command
to allow incoming ssh is

.. code-block:: bash

    $ sudo ufw allow ssh

However, it you've setup **ssh** on a different port (as I have) -- say port
XXXX -- the command becomes:

.. code-block:: bash

    $ sudo ufw allow XXXX/tcp

We'll also allow **www** traffic:

.. code-block:: bash

    $ sudo ufw allow www

Finally, to enable (**be sure that you've setup your ssh access before doing
this!**):

.. code-block:: bash

    $ sudow ufw enable

Now trying the ``$ sudo ufw status`` command should reflect the ports we allowed
above and indicate the firewall is active.  Finally, to disable or reset
**ufw** the commands are

.. code-block:: bash

    $ sudo ufw disable

and

.. code-block:: bash

    $ sudo ufw reset

For more information on **ufw** try: `ufw`_ or `setup a firewall`_.

* `install nginx on ubuntu 14.04`_

  Next, I will install nginx_ for serving web content.  The install is exactly
  as you'd expect:

.. code-block:: bash

    $ sudo apt-get install nginx

nginx_ is active by default when installed. So, open a browser and go to the
IP/url for your VPS to see the default nginx_ welcome page.

To stop, start or restart nginx_ try:

.. code-block:: bash

    $ sudo service nginx stop
    $ sudo service nginx start
    $ sudo service nginx restart

Finally, for the initial setup, let's make sure that nginx_ starts when the
server is rebooted:

.. code-block:: bash

    $ sudo update-rc.d nginx defaults

This command should say that stop/start links for nginx_ already existed.  The
next step is set up for the actual content-- try
`how to setup nginx server blocks on ubuntu 14.04`_.

* **Update the server**

  The server will need to updated at times and this has to be done via the
  terminal.  Fortunately updates are pretty simple.  For typical (minor) updates
  of installed software the following will get things done:

.. code-block:: bash

    $ sudo apt-get update
    $ sudo apt-get upgrade

For major updates (like a kernel upgrade) more has to be done:

.. code-block:: bash

    $ sudo apt-get update
    $ sudo apt-get dist-upgrade

Typically this is followed by a reboot of the server:

.. code-block:: bash

    $ sudo reboot

That's it for all the basic updating needs.


.. _digital ocean: https://www.digitalocean.com/

.. _initial server setup: https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-14-04
.. _ssh key setup: https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys--2
.. _setup a firewall: https://www.digitalocean.com/community/tutorials/how-to-setup-a-firewall-with-ufw-on-an-ubuntu-and-debian-cloud-server
.. _install nginx on ubuntu 14.04: https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-14-04-lts
.. _how to setup nginx server blocks on ubuntu 14.04: https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-14-04-lts

.. _ufw: https://help.ubuntu.com/community/UFW
.. _nginx: http://nginx.org/en/

.. author:: default
.. categories:: none
.. tags:: ubuntu 14.04, VPS, server setup, blog setup
.. comments::

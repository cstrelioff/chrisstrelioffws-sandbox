Migrate ssh keys to new computer
================================

I need to use a set of ssh keys on a new machine. **In general, it is best to
generate new keys instead of copying old keys**, but this is a *temporary
solution*.

.. more::

So, given that disclaimer, I copied the **~/.ssh** folder from the old machine
into a *temp folder* on the new machine.  This avoids copying over anything in
the new machine's **~/.ssh** folder.  Copy all *keyname*, *keyname.pub* files
to **~/.ssh**.  Also, copy the **~/.ssh/config** (if you have one).  Finally,
the new computer needs to add the keys. Do this with command for each key:

.. code-block:: bash

    $ ssh-add keyname

You will be prompted for the password for the key (if any).  Now, try the keys
out.  You should be able to ssh to all of the machines covered by the added
key(s).

Potential Problems
------------------

There can be a variety problems with the above process.  The above worked for
me without modification.  However, I think that file ownership and permissions
can be problematic.  One solution for `ssh permission problems`_ is available
just in case.

.. _ssh permission problems: http://askubuntu.com/questions/134975/copy-ssh-private-keys-to-another-computer


.. author:: default
.. categories:: none
.. tags:: ssh, ssh keys
.. comments::

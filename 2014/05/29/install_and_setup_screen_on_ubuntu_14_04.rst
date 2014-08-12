Install and setup screen_ on Ubuntu 14.04
=========================================

screen_ is a great tool for the terminal, allowing me to have many windows
(sessions) open at the same time-- say *vim* in one, an *ssh* session in
another, etc.  This post documents my basic setup -- if you have
cool/different ideas about how to do this type of thing let me know.

.. more::

First we use apt-get to install Screen from the Ubuntu repository:

.. code-block:: bash

    $ sudo apt-get install screen

That's all you need to get started.  There are many *getting started* tutorials
out there--
`here's one to start  <http://www.mattcutts.com/blog/a-quick-tutorial-on-screen/>`_.

I like to customize my use of screen, so I setup a **.screenrc** file in my
home directory; that is **~/.screenrc**.  The contents can be something like
this (I snagged this example online long ago-- if you have a link/reference I'd
be happy to give credit in the post)::

    # .screenrc

    # GNU Screen - main configuration file
    # All other .screenrc files will source this file to inherit settings.
    
    # Allow bold colors - necessary for some reason
    attrcolor b ".I"
    
    # Tell screen how to set colors. AB = background, AF=foreground
    termcapinfo xterm 'Co#256:AB=\E[48;5;%dm:AF=\E[38;5;%dm'
    
    # Enables use of shift-PgUp and shift-PgDn
    termcapinfo xterm|xterms|xs|rxvt ti@:te@
    
    # Erase background with current bg color
    defbce "on"
    
    # Enable 256 color term
    term xterm-256color
    
    # Cache 30000 lines for scroll back
    defscrollback 30000
    
    hardstatus alwayslastline
    # Very nice tabbed colored hardstatus line
    hardstatus string '%{= Kd} %{= Kd}%-w%{= Kr}[%{= KW}%n %t%{= Kr}]%{= Kd}%+w %-= %{KG} %H%{KW}|%{KY}%101`%{KW}|%D %M %d %Y%{= Kc} %C%A%{-}'

This **.screenrc** file provides a nice status line to keep track of all the
open screens. In addition to this file, I also have a collection of other files
that I use for specific projects. For example, for working on this blog I might
have the file **.screenrc_blog** with the contents::

    # .screenrc_blog

    # main screen setup
    source /home/cstrelioff/.screenrc
    
    chdir /home/cstrelioff
    screen
    title "home"
    
    chdir /home/cstrelioff/MyBlog
    screen
    title "blog"

Using the above file I start screen, creating *home* and *blog* windows at
startup, using the command:

.. code-block:: bash

    $ screen -c .screenrc_blog

As always, if you have questions or comments please let me know.

.. _screen: http://www.gnu.org/software/screen/

.. author:: default
.. categories:: none
.. tags:: screen, ubuntu 14.04, my ubuntu setup
.. comments::

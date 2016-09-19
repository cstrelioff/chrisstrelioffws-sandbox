.. _vim-vundle:

vim and vundle on Ubuntu 16.04
==============================

I have just upgraded to Ubuntu 16.04, the new long-term-stable distribution of
Ubuntu. This means I will be installing all of my trusted computing tools on
this new distribution as well as reconsidering some of my approaches. In this
post I'll go over a new approach to my vim_ setup for Ubuntu 16.04, changing
from pathogen_ to vundle_ plugin management.

.. more::

overview
--------

In a previous post, :ref:`vim-pathogen`, I described installing vim_ and using
pathogen_ to manage vim_ plugins on Ubuntu 14.04. Over the past two years I
have used pathogen_ without trouble and expect the same would be true on
Ubuntu 16.04 -- so, checkout the previous post if you'd like to use pathogen_.

In this post I'll cover using vundle_ to manage my plugins-- this is mainly
out of curiosity to try out a new tool. However, there is one advantage that
I like: the vim_ plugins I'm using are recorded in my **~/.vimrc** file,
making it easy to reinstall plugins on a new machine.  This is a nice benefit
of the vundle_ approach.

vim
---

So let's get started with installing vim_

.. code-block:: bash

  $ sudo apt-get install vim

That's it, now to the plugins.

vundle
------

First up is vundle_, of course, because this has to do all the managing. The
file **~/.vimrc** and the directory **~/.vim** are where all the action
happens.  If you have them, it's good to backup. For example, following this
nice `Digital Ocean Tutorial on vundle`_, one can use:

.. code-block:: bash

  $ if [ -e .vimrc ]; then mv .vimrc .vimrc_bak; fi
  $ if [ -e .vim ]; then mv .vim .vim_bak; fi

Once you are backed up, the vundle_ git repository can be cloned using:

.. code-block:: bash

  $ git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim

Next, create a minimal **~/.vimrc** file to get things started:

.. code-block:: bash

  $ vim ~/.vimrc

This file should contain the following (also checkout the examples at the
vundle_ repository):

.. code-block:: none
  :linenos:

  " ~/.vimrc
  "

  " no vi compat
  set nocompatible
  
  " filetype func off
  filetype off
  
  " initialize vundle
  set rtp+=~/.vim/bundle/Vundle.vim
  
  call vundle#begin()
  " start- all plugins below
  
  Plugin 'VundleVim/Vundle.vim'
  
  " stop - all plugins above
  call vundle#end()
  
  " filetype func on
  filetype plugin indent on

This loads the vundle_ plugin itself and establishes the basic layout of the
**~/.vimrc** file. After the file is saved, relaunch vim_ and run

.. code-block:: none

  :PluginInstall

This process is the same for adding any new plugin using vundle_:

1. Add the repository for the plugin to your **~/.vimrc**. Be sure that
   this addition is in the designated area: lines 15-17 in the example
   above. The addition of the vundle_ repository is an example of the
   correct format:

.. code-block:: none

     Plugin 'VundleVim/Vundle.vim'
     
2. Add configuration information (if there is any) for the plugin at the end
   of the **~/.vimrc**
3. Relaunch vim_ and run :code:`:PluginInstall`, as described above. This will
   run through all the plugins listed and install any that are not setup-- in
   the process, a new tab is opened to describe the process. When done you
   should get a *Done!* in the lower-left corner. Close the tab and you are
   done-- use :code:`:q`.

I'll add the gruvbox_ plugin very explicitly as the next example and then move
to a more abbreviated description of the process.

gruvbox
-------

First, let's get some color-- I like the gruvbox_ dark color scheme. There are
a bunch of other choices out there so don't feel obligated to use my favorite!
More to point, I'll use the installation of gruvbox_ as a detailed example of
adding a plugin using vundle_.

As discussed above, to install the plugin we modify our **~/.vimrc**. We add
the gruvbox_ repository information and add some plugin-specific details at
the end of the file. After the changes, the **~/.vimrc** file looks like:

.. code-block:: none
  :linenos:

  " ~/.vimrc
  "

  " no vi compat
  set nocompatible
  
  " filetype func off
  filetype off
  
  " initialize vundle
  set rtp+=~/.vim/bundle/Vundle.vim
  
  call vundle#begin()
  " start- all plugins below
  
  Plugin 'VundleVim/Vundle.vim'
  Plugin 'morhetz/gruvbox'
  
  " stop - all plugins above
  call vundle#end()
  
  " filetype func on
  filetype plugin indent on

  " set color
  colorscheme gruvbox
  set background=dark
  set colorcolumn=80

In summary, the changes/actions are:

1. [line 17] The gruvbox_ plugin is added
2. [lines 25-28] I've set gruvbox_ as the colorscheme, chosen the dark
   background, and set column 80 as the color column (this makes the column a
   lighter gray by default)
3. Relaunch vim_ and run :code:`:PluginInstall`. After a relaunch of vim_ you
   should have the nice gruvbox_ dark theme working.

lightline
---------

Next, I will install lightline_, a nice status line for vim_. I use the
default settings, but there are a bunch of customizations that can be done--
checkout the lightline_ repository for more information. The changes are:

1. Add the lightline_ plugin

.. code-block:: none
  
  Plugin 'itchyny/lightline.vim'

2. On both Ubuntu 14.04 and 16.04 I've had to add the :code:`laststatus=2` fix
   to get the status line to show properly. At the end of the file, add:

.. code-block:: none
  
  " lightline fix
  set laststatus=2

3. Finally, relaunch vim_ and run :code:`:PluginInstall`.

NERDTree
--------

NERDTree_ is another essential vim_ plugin, providing a nice file browser to
find and open files as well as bookmark directories. The install goes as 
follows:

1. Add the NERDTree_ plugin

.. code-block:: none
  
  Plugin 'scrooloose/nerdtree.git'

2. If you'd like to assign **Cntl-n** to open and close the file browser add 
   the following to the end of your **~/.vimrc**

.. code-block:: none
  
  " NERDTree shortcut
  map <C-n> :NERDTreeToggle<CR>

3. Finally, relaunch vim_ and run :code:`:PluginInstall`.

The bookmark feature in NERDTree still works as I described previously, so
check that post out if you'd like to use that feature-- :ref:`vim-pathogen`.

vim-template
------------

If you'd like to have file templates with vim_ a useful plugin is
vim-template_. Using this tool, starting up vim_ like so:

.. code-block:: bash

  $ vim test.py

will produce a file that looks like (after some config):

.. code-block:: python

  #! /usr/bin/env python
  # -*- coding: utf-8 -*-
  # vim:fenc=utf-8
  #
  # Copyright © 2016 Your Name <Your Email>
  #
  # Distributed under terms of the Your-License license.
  
  """
  
  """

Using the usual vundle_ install process, do the following:

1. Add the vim-template_ plugin

.. code-block:: none
  
  Plugin 'aperezdc/vim-template'

2. Set the template fills for name, email, etc. by adding the following to the
   end of you **~/.vimrc** (of course change to relevant information):

.. code-block:: none

  " Customize the settings for vim-template plugin
  let g:email = "Your Email"
  let g:user = "Your Name"
  let g:license = "Your-License"

3. Finally, relaunch vim_ and run :code:`:PluginInstall`.

jedi-vim
--------

If you are a Python coder, jedi-vim_ is a great plugin allowing for
autocompletion and pulling up documentation inside of vim_. However, this
plugin depends on installing the Python package jedi_. This can be done a
variety of ways, I use pip:

.. code-block:: bash

  $ pip install --user jedi

This installs the most recent version of jedi_. Once this is installed the
vundle_ install of the vim_ plugin goes as usual:

1. Add the jedi-vim_ plugin

.. code-block:: none
  
  Plugin 'davidhalter/jedi-vim'

2. No configuration lines in **~/.vimrc** are needed.
3. Finally, relaunch vim_ and run :code:`:PluginInstall`.

Once this is installed, the two commands I use all the time are:

1. **cntl-space**: attempts to autocomplete
2. **shift-k**: attempts to load documentation into a new vim_ window. This
   must be done in command-mode with the cursor on the function or class of
   interest.

editorconfig
------------

A relatively new addition in my vim_ workflow is editorconfig_, which lets the
user store editor configurations like the size of indent, whether to use tab
or space, etc.  These configurations files can be set globally and
per-project-- also, the settings can be used by a bunch of editors, not just
vim_.  You should checkout the editorconfig_ site to learn more and choose your
settings.

The vim install is:

1. Add the editorconfig_ plugin

.. code-block:: none
  
  Plugin 'editorconfig/editorconfig-vim'

2. The are no settings in **~/.vimrc**, but my global configuration is
   contained in a file, **~/.editorconfig** (at time of this post):

.. code-block:: none

  # EditorConfig is awesome
  # http://EditorConfig.org
  root = true
  
  # defaults
  [*]
  indent_style = space
  indent_size = 2
  end_of_line = lf
  charset = utf-8
  insert_final_newline = true
  trim_trailing_whitespace = true
  
  # md
  trim_trailing_whitespace = false
  
  # py
  [*.py]
  indent_size = 4
  
  # Tab indentation (no size specified)
  [Makefile]
  indent_style = tab
  

3. Relaunch vim_ and run :code:`:PluginInstall`.

That's it
---------

So, that's it for my (self-) documentation of getting started with vundle_ on
Ubuntu 16.04.  Hopefully those who find this post will find it helpfull-- I
know I'll look back at it when I have to upgrade to Ubuntu 18.04 in a couple
of years.

If you find typos or have a question please leave comments below. I'll do my
best to respond in a timely manner. I would also love to read about other
useful plugins or different approaches to what I've done-- again, leave a
note below.


.. _vim: http://www.vim.org/ 
.. _vim tutorials: http://vim.begin-site.org/tutorials/
.. _Digital Ocean Tutorial on vundle: https://www.digitalocean.com/community/tutorials/how-to-use-vundle-to-manage-vim-plugins-on-a-linux-vps 
.. _pathogen: https://github.com/tpope/vim-pathogen
.. _vundle: https://github.com/VundleVim/Vundle.vim

.. _gruvbox: https://github.com/morhetz/gruvbox
.. _lightline: https://github.com/itchyny/lightline.vim
.. _editorconfig: https://github.com/editorconfig/editorconfig-vim
.. _NERDTree: https://github.com/scrooloose/nerdtree
.. _Tagbar: http://majutsushi.github.io/tagbar/
.. _jedi-vim: https://github.com/davidhalter/jedi-vim
.. _jedi: https://github.com/davidhalter/jedi
.. _vim-template: https://github.com/aperezdc/vim-template

.. author:: default
.. categories:: none
.. tags:: vim, ubuntu 16.04, vundle
.. comments::

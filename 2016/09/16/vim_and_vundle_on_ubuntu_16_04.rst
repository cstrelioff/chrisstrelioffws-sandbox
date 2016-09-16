.. _vim-vundle:

vim and vundle on Ubuntu 16.04
==============================

I have just upgraded to Ubuntu 16.04, the new long-term-stable distribution of
Ubuntu. This means I will be installing all of my trusted computing tools on
this new distribution and reconsidering some of my approaches. In this post
I'll go over my *slightly modified* vim_ setup for Ubuntu 16.04.

.. more::

In a previous post, :ref:`vim-pathogen`, I described installing vim_ and using
pathogen_ to manage vim plugins on Ubuntu 14.04. In the past two years I used
pathogen_ without trouble and expect the same would be true on Ubunut 16.04 --
so, checkout the previous post if you'd like to use pathogen_.

In this post I'll cover using vundle_ to manage my plugins-- this is mainly
out of curiousity to try out a new tool.

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

Once you are backed up, the vundle git repository can be cloned using:

.. code-block:: bash

  $ git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim

Next, create a minimal **~/.vimrc** file to get things started:

.. code-block:: bash

  $ vim ~/.vimrc

This file should contain the following (also checkout the examples at the
vundle_ repository):

.. code-block:: none
  :linenos:

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

This loads the vundle_ plugin itself and establishes the basic format of the
**~/.vimrc** file.  Write and close the file using-- :code:`:wq`. Finally,
relaunch vim_ and run-- :code:`:PluginInstall`.

The key line, as far as adding new plugins to vim_ using vundle_ is line 13.
Lines like this tell vundle_ what git repository to grab and install.  Let's
try this out with my starter set of plugins.

gruvbox
-------

First, let's get some color-- I like the gruvbox_ dark color scheme. There are
a bunch of other choices out there so don't feel obligated to use my favorite!
More to point, to install the plugin we modify our **~/.vimrc** to look like
this:

.. code-block:: none
  :linenos:

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

I've made two additions:

1. [line 14] The gruvbox_ plugin is added
2. [lines 22-25] I've set gruvbox_ as the colorscheme, chosen the dark
   background, and set column 80 as the color column (this makes the column a
   lighter gray be default)

With these changes, write the file and quit-- :code:`:wq`. Relaunch vim_ and
run-- :code:`:PluginInstall`. After a relaunch of vim_ you should have the nice
gruvbox_ dark theme working.

lightline
---------

Next let's install lightline_, a nice statusline for vim_. As with gruvbox_,
the addition is simple--

.. code-block:: none
  :linenos:

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
  Plugin 'itchyny/lightline.vim'
  
  " stop - all plugins above
  call vundle#end()
  
  " filetype func on
  filetype plugin indent on

  " set color
  colorscheme gruvbox
  set background=dark
  set colorcolumn=80

  " lightline fix
  set laststatus=2

The changes are

1. [line 15] Add the lightline_ plugin
2. [lines 28-29] On both Ubuntu 14.04 and 16.04 I've had to add the
   laststatus=2 fix

Finally, write and quit, then run :code:`PluginInstall` as before.



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
.. _exuberant ctags: http://ctags.sourceforge.net/
.. _jedi-vim: https://github.com/davidhalter/jedi-vim
.. _jedi: https://github.com/davidhalter/jedi
.. _vim-template: https://github.com/aperezdc/vim-template

.. author:: default
.. categories:: none
.. tags:: vim, ubuntu 16.04, vundle
.. comments::

.. _vim-pathogen:

Install and setup vim on Ubuntu 14.04
=====================================

**<note>**
I have upgraded to Ubuntu 16.04 and wrote another post about setting up vim_,
this time using vundle instead of pathogen.  Checkout the new post--
:ref:`vim-vundle` -- if that sounds interesting to you.
**</note>**

**Vim** is a powerful editor that can be used on your laptop/desktop and is
also typically found of any Linux server you might encounter.  As a result, I
started using **vim** as my main editor.  The Ubuntu install is simple:

.. code-block:: bash

    $ sudo apt-get install vim

.. more::
    
That's it, you're ready to edit.  A good place to start if you need to learn
more about **vim** is the main website: vim_ . Also be sure to check out the
`vim tutorials`_. 

Pathogen
--------

My next step is to add a variety of **vim plugins** that make (my) life easier.
To do this I use pathogen_  a
wonderful vim package manager. Installation is accomplished with the following
lines:

.. code-block:: bash

    $ mkdir -p ~/.vim/autoload ~/.vim/bundle;
    $ curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim

If you don't have curl installed, use:

.. code-block:: bash

    $ sudo apt-get install curl

and try the second line again. Finally, if you don't have a **~/.vimrc** file
create the following minimal example::

    " contents of minimal .vimrc
    execute pathogen#infect()
    syntax on
    filetype plugin indent on

NERDTree
--------

NERDTree_  is a plugin the provides a nice file browser with bookmarks. With
pathogen_ available, getting NERDTree_ installed is as simple as:

.. code-block:: bash

    $ cd ~/.vim/bundle
    $ git clone https://github.com/scrooloose/nerdtree.git

After installing, start vim_ and type::

    :NERDTreeToggle
   
to *toggle* the file browser open or closed. Use up and down arrows to select
files and press **enter** to open file in current tab.  To open in a *new tab*,
select the file and press **t**.

To bookmark, select a directory and type::

    :Bookmark bookmarkname

to assign *bookmarkname* to the desired directory.  To toggle the bookmarks
open or closed (while in the NERDTree window) press **shift-b**. Finally, to
open a bookmark, select the bookmark using up/down arrows and press **enter**
when the desired bookmark is highlighted.

Tagbar
------

Tagbar_  does a nice job of showing code
outlines-- class, methods, etc and allows for jumping to different parts of the
code using the outline.  I've mainly used this with Python, where the results are
very nice.

First, we have to install `exuberant ctags`_ , which Tagbar_ uses to do its
parsing. Luckily, there is version in the Ubuntu repository:

.. code-block:: bash

    $ sudo apt-get install exuberant-ctags

Next, install the vim_ plugin using pathogen_, as before:

.. code-block:: bash

    $ cd ~/.vim/bundle
    $ git clone git://github.com/majutsushi/tagbar

Thanks to pathogen, we can now start vim_ and type::

    :TagbarToggle

to toggle the code outline open or closed.  To get to the code outline window
press **Cntrl-w** and then **l**  -- this is a general vim command to move to
the *right* window.  Use up and down arrows to move through the code outline.
When the desired class or function is highlighted press **enter** and vim will
jump to the desired code.  This is very nice for larger files!

jedi-vim
--------

Next we install the jedi-vim_ plugin which allows for auto-complete and
documentation search for Python projects.  First, we install the Python package
jedi_

.. code-block:: bash

    $ pip install --user jedi

I use this command assuming that you are installing all python packages as a
user.  Otherwise you will have install with ``$ sudo pip install jedi`` (global
install), or activate the desired virtual environment and use
``$ pip install jedi``.

Finally, use pathogen_ to install jedi-vim in the usual way:

.. code-block:: bash

    $ cd ~/.vim/bundle/
    $ git clone https://github.com/davidhalter/jedi-vim.git

The two command I use most with jedi are:

* **cntrl-space** : auto-complete
* **shift-k** : get documentation (must be in command-mode and put cursor on
  function of class of interest)

vim-template
------------

vim-template_  is a plugin that provides nice file templates for new files.
Using pathogen_ the installation is simple:

.. code-block:: bash

    $ cd ~/.vim/bundle
    $ git clone git://github.com/aperezdc/vim-template.git

Now, try:

.. code-block:: bash

    $ vim test.py

or,

.. code-block:: bash

    $ vim test.sh

to see the standard templates for Python files and bash scripts, respectively.

There are a variety of customizations that can be made (see the link above),
but I like to add the following defaults to my **.~/vimrc** file::

    " Customize the settings for vim-template plugin                               
    let g:email = "desiredemail@gmail.com"
    let g:user = "Desired Name"                                        
    let g:license = "Desired License"


That's it for my basic vim_ and vim-plugins setup.  Questions and comments are
always welcome.

.. _vim: http://www.vim.org/ 
.. _vim tutorials: http://vim.begin-site.org/tutorials/
.. _pathogen: https://github.com/tpope/vim-pathogen
.. _NERDTree: https://github.com/scrooloose/nerdtree
.. _Tagbar: http://majutsushi.github.io/tagbar/
.. _exuberant ctags: http://ctags.sourceforge.net/
.. _jedi-vim: https://github.com/davidhalter/jedi-vim
.. _jedi: https://github.com/davidhalter/jedi
.. _vim-template: https://github.com/aperezdc/vim-template

.. author:: default
.. categories:: none
.. tags:: vim, ubuntu 14.04, my ubuntu setup
.. comments::

.. _upgrade-meteor-1.3:

Upgrading to Meteor 1.3 on Ubuntu 14.04
=======================================

In a recent post, :ref:`install-meteor`, I documented the install process for
Meteor -- at that time the current version was 1.2.1.  Well, the new version --
1.3 -- is out and I will briefly document the upgrade process and provide some
links to new guides and tutorials that the MDG (Meteor Development Group)
has released.

.. more::

New Install
-----------

If you are installing Meteor for the first time, the process has not changed:

.. code:: bash

    $ curl https://install.meteor.com/ | sh

You can check `Meteor install instructions`_ for the latest. As you'd expect,
checking the version now gets you

.. code:: bash

    $ meteor --version
    Meteor 1.3

Upgrading from 1.2.1 to 1.3
---------------------------

The upgrade is even easier than the install!  Amazingly, a simple (do this
in a directory that *is not* a Meteor project):

.. code:: bash

    $ meteor update

That's it -- you don't even have to use curl!  If you already running version
1.3 (and didn't know it) you'll be told you're running the latest version. So,
no worries about running the update command.

If you have already been working with Meteor, old projects can be updated by
running :code:`meteor update` in the project directory; something like this:

.. code:: bash

    $ cd project-directory
    $ meteor update

I have not tried this yet and do not know what types of changes happen when 
you update a project -- **so, be careful!** I would suggest a backup of the
project -- *as always* -- before trying!

Changes in version 1.3
----------------------

This new version has quite a few changes in the way Meteor projects work -- I 
won't attempt to describe them here -- check out the `Metero 1.3 announcement`_
for more details.

Briefly, for beginner Meteor developers like myself, the changes are quite
dramatic and will take some getting used to.  For example, the start project
setup is more complex -- this change makes sense to me because the directory
structure is similar to the one would create as a project developed. To see
this, create a *test-project*:

.. code:: bash

    $ meteor create test-project
    Created a new Meteor app in 'test-project'.
    
    To run your new app:
      cd test-project
      meteor
    
    If you are new to Meteor, try some of the learning resources here:
      https://www.meteor.com/learn

This is the same as before. However, looking at the files created, we see the
following:

.. code:: bash

    $ cd test-project/
    $ tree .
    .
    ├── client
    │   ├── main.css
    │   ├── main.html
    │   └── main.js
    ├── package.json
    └── server
        └── main.js
    
    2 directories, 5 files

The project structure already has *client* and *server* directories -- things
that were previously created by the developer. In addition, there is also a
*package.json* file, reflecting the much tight integration with npm. Finally,
for this post, if we look at the one of the files -- *server/main.js* in this
case -- we see more modern, ES2015 code:

.. code-block:: JavaScript

    import { Meteor } from 'meteor/meteor';
    
    Meteor.startup(() => {
      // code to run on server at startup
    });

In particular, notice the explicit import of Meteor and the use of an arrow
function.

Further information on this version of Meteor is pretty limited at this point. 
Resources like the `Discover Meteor book`_ and the
`Coursera Meteor specialization`_ will be referencing the previous version of
Meteor -- however, that might change quickly! For now, check out the nice
tutorials (choose blaze-, angular- or react-flavored):

* `Meteor Blaze tutorial`_ -- build a todo list using version 1.3 and the
  default blaze templates
* `Meteor Angular tutorial`_ -- build a todo list using version 1.3 and
  Angular
* `Meteor React tutorial`_ -- build a todo list using version 1.3 and
  React

If you don't know the difference I'd suggest starting with default Blaze
templates, as they are pretty straightforward. Also, the
`Official Meteor Guide`_ has been expanded and looks really useful; you should
check it out.

Okay, that's it.  As always, comments and corrections are welcome -- just be 
nice.

.. _Meteor install instructions: https://www.meteor.com/install 
.. _Meteor Blaze tutorial: https://www.meteor.com/tutorials/blaze/creating-an-app
.. _Meteor Angular tutorial: https://www.meteor.com/tutorials/angular/creating-an-app
.. _Meteor React tutorial: https://www.meteor.com/tutorials/react/creating-an-app 
.. _Official Meteor Guide: http://guide.meteor.com/

.. _Metero 1.3 announcement: http://info.meteor.com/blog/announcing-meteor-1.3

.. _Discover Meteor book: https://book.discovermeteor.com/
.. _Coursera Meteor specialization: https://www.coursera.org/specializations/website-development

.. author:: default
.. categories:: none
.. tags:: javascript, meteor, nodejs, MongoDB, Ubuntu 14.04
.. comments::

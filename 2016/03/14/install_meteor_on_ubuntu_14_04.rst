.. _install-meteor:

Install Meteor on Ubuntu 14.04
==============================

**[Edit] 2016, Mar 30**
Verision 1.3 of Meteor is now out -- this installation instructions are still
pretty much the same as below. If you'd like the updated install/upgrade
instructions checkout :ref:`upgrade-meteor-1.3`.
**[/Edit]**

I've been spending a lot of time working with Meteor recently.  This framework
uses javascript and MongoDB to create a full stack solution that is pretty
easy to use. The installation is simple and painless on Ubuntu 14.04, but I'll
document my process here for reference and provide some links for learning more
about Meteor.

.. more::

I will be following the official `Meteor install instructions`_. It is worth
noting that Meteor installs its own versions of node and MongoDB -- these will
not clash with node and MongoDB if you have already them installed. This also
means that you *do not need* to install node and MongoDB before Meteor.

The install procedure is a simple:

.. code:: bash

    $ sudo curl https://install.meteor.com/ | sh

Once installed, you can check the version:

.. code:: bash

   $ meteor --version
   Meteor 1.2.1

Wow, it's that simple!

Getting started
---------------

The `Meteor tutorial`_ available at meteor.com is really quite good.  So, this
is a nice place to start. To give you a flavor, open the terminal and cd to
a good location, then create a project:

.. code:: bash

    $ meteor create simple-todos
    Created a new Meteor app in 'simple-todos'.
    
    To run your new app:
      cd simple-todos
      meteor
    
    If you are new to Meteor, try some of the learning resources here:
      https://www.meteor.com/learn

This create the project, *simple-todos*, and tells you what to do next:

.. code:: bash

    $ cd simple-todos/
    $ meteor
    [[[[[ ~/Sandbox/meteor-play/simple-todos ]]]]]
    
    => Started proxy.
    => Started MongoDB.
    => Started your app.
    
    => App running at: http://localhost:3000/

If you open your browser at localhost, port 3000, the default meteor
application will be running and you should be able to click a button to
increment a counter -- you stop the server by doing a **control-c** back at
the terminal.

To learn more, continue on with the `Meteor tutorial`_, it really is quite good
and covers all, or most of, the basics.  Other resources that I have been using
and found to be useful are (not free, but not too $$) --

* `Discover Meteor book`_ -- covers similar material to the tutorial, but in 
  much more depth. The first few chapter are free but the complete book is
  about (USD) $30 at this time.
* `Coursera Meteor specialization`_ -- a series of six courses, from html/css/js
  basics through full Meteor apps. These courses are not free, but Coursera does
  offer financial aid if you need it.  The first courses are basic-- but they
  also might go too fast if you are really an html/css/js beginner. The later
  courses cover lots of material and provide focus if you'd like more than
  books or blog posts. Strangely, the instructors don't monitor the forums and
  there were no teaching-assistants so the students are on their own to figure
  things out -- I wasn't too impressed by this aspect of the non-free courses!

So, that's the install and some places to learn more.  If you have other
resources to share, please leave a note -- I'd love to check it out.  I also
plan on writing more about Meteor in the coming weeks and months. So, check
back!

.. _Meteor install instructions: https://www.meteor.com/install 
.. _Meteor tutorial: https://www.meteor.com/tutorials/blaze/creating-an-app
.. _Discover Meteor book: https://book.discovermeteor.com/
.. _Coursera Meteor specialization: https://www.coursera.org/specializations/website-development


.. author:: default
.. categories:: none
.. tags:: javascript, meteor, nodejs, MongoDB, Ubuntu 14.04
.. comments::

Installing Node.js and npm on Ubuntu 14.04
==========================================

I've decided to start being systematic about learning *javascript*, with a
focus on getting good with `d3js`_.  I'll be installing `nodejs`_ and npm (node
package manager) as a way to get access to a javascript console and, for later,
a powerful javascript environment. As always, *constructive* comments and
questions are welcome and much appreciated.

.. more::

I'll be using the instructions at the `nodejs github wiki`_ that allows for the
use, and updating, of more current versions of nodejs and npm.  It is worth
noting that both nodejs and npm are in the Ubuntu repository and can be
installed with the usual :code:`sudo apt-get install`.  However, installing
this way leaves the user stuck with older versions of the relevant software.

So, following the `nodejs github wiki`_, the install is as simple as:

.. code:: bash

    $ curl -sL https://deb.nodesource.com/setup | sudo bash -
    $ sudo apt-get install -y nodejs

That's it, we're done. A check of the nodejs version gets:

.. code:: bash

    $ node --version
    v0.10.35

and, for npm:

.. code:: bash

    $ npm --version
    1.4.28

Finally, some examples of how *I will use* nodejs to learn javascript.
**First**, I can use the console by starting node with no arguments:

.. code:: bash

    $ node

Next, print *Hello world!* and exit:

.. code:: javascript

    > console.log("Hello world!")
    Hello word!
    undefined
    > process.exit()

This provides access to the javascript console and makes it possible for me
to try out simple commands.

**Second**, for longer chunks of code it is nice to be able to execute a file
from the command line, just like I would with *bash* or *Python*. To do this,
create the file **helloworld.js** with the following code:

.. code:: javascript

    #! /usr/bin/env node
    // helloworld.js
    
    console.log("Hello World!")

Notice that I've added a *shebang* to the top of the file that uses *node* to
execute the file.  Next, make the file executable:

.. code:: bash

    $ chmod u+x helloworld.js

Then, execute the file from the bash prompt:

.. code:: bash

    $ ./helloworld.js
    Hello World!

Of course, you can also skip making the file executable and call node directly:

.. code:: bash

    $ node helloworld.js
    Hello World!

Either way, using this second setup makes it much easier (at least for me) to
work with larger and more complex javascript code-- very cool. If you are
looking for more examples, starting at the level above and moving to more
advanced material try of this `beginners nodejs post`_.

If you know of good (online) learning resources for *javascript*, *node* and/or
*d3* please leave comments for everyone that reads the post-- thanks!

.. _beginners nodejs post: http://blog.modulus.io/absolute-beginners-guide-to-nodejs
.. _nodejs: https://github.com/joyent/node/
.. _nodejs github wiki: https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager 
.. _d3js: http://d3js.org/

.. author:: default
.. categories:: none
.. tags:: javascript, nodejs, npm, d3
.. comments::

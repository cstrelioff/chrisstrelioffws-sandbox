ES2015 using Node, Babel and Webpack
====================================

In this post I will cover setting up a project that uses ES2015/ES6 -- modern
JavaScript-- that will still work in current web browsers that need ES5. The
trick is to use `Babel`_ to *transpile* ES2015/ES6 code to ES5, which can run
on current browsers. Why do this? Well, ES2015/ES6 is the future of JavaScript
and I'd like to start using it now.

.. more::

All readers should be aware that **I am not an expert**. This post is as much
for me to remember what I did as to inform others on what to do. So, let me
know if you have better ways to do this or you find mistakes -- please use the
comments at the end of the post.

To get started, I would like to credit posts by others that really
helped me sort this out (however, all mistakes are my own). I will be using a
combination or re-mix of the following two sources:

1. `Understanding JavaScript Modules: Bundling & Transpiling (by Mark Brown)
   <https://www.sitepoint.com/javascript-modules-bundling-transpiling/>`_
   -- this covers a lot of ground, including the topics here. I found it very
   useful but it's definitely not for the beginner.
2. `Introduction to Webpack: Part 1 (by Stuart Memo)
   <http://code.tutsplus.com/tutorials/introduction-to-webpack-part-1--cms-25791>`_
   and
   `Introduction to Webpack: Part 2 (by Stuart Memo)
   <http://code.tutsplus.com/tutorials/introduction-to-webpack-part-2--cms-25911>`_
   -- these posts are at more basic level and are focused on using webpack. In
   particular, the first part is a very nice reference for the topics covered
   here.

So, credit to both authors, Mark Brown and Stuart Memo, for the original source
material as well as motivation!!!

node and npm
------------

In a previous post, :ref:`install-node-lts`, I covered installing node and the
node package manager (npm) on Ubuntu 14.04. I will be using these tools to drive
everything so you should look at the post if you do not have them installed. For
reference, at the time of this post I have:

.. code:: bash

    $ node --version
    v4.4.7
    $ npm --version
    2.15.8

You should have similar versions, or higher. Next, I will install two packages
globally: `webpack`_ and `live-server`_:

.. code:: bash

    $ npm install -g live-server webpack

If this command complains about permission issues, try setting up a sudo-free
location for global installs of npm packages.  I've added a section to
:ref:`install-node-lts` that covers how to do this on Ubuntu 14.04.

project setup
-------------

Next, I will create a project directory and use npm to create a
:code:`package.json` file

.. code:: bash

    $ mkdir es2015-project
    $ cd es2015-project/
    $ npm init -y

Using the -y tag forces the defaults to be used for :code:`package.json`
and the resulting file looks something like this:

.. code-block:: JavaScript

   {
     "name": "es2015-project",
     "version": "1.0.0",
     "description": "",
     "main": "index.js",
     "scripts": {
       "test": "echo \"Error: no test specified\" && exit 1"
     },
     "keywords": [],
     "author": "",
     "license": "ISC"
   }

Of course, you can init without this flag or change the file after-the-fact to
your liking. Next, I create some directories and files that will be filled
with code:

.. code:: bash

    $ mkdir src
    $ touch src/{main,lib}.js index.html

If I use tree to show the project layout at this point it looks like this:

.. code:: bash

   $ tree .
   .
   ├── index.html
   ├── package.json
   └── src
       ├── lib.js
       └── main.js
   
   1 directory, 4 files

index.html
----------

First, I setup an index.html file that will be used to load the resulting code
and do some simple calculations (this is motivated by the Mark Brown's example;
see link above):

.. code-block:: html

    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="utf-8">
      <title>es2015-project</title>
    </head>
    <body>
      <h1>Results</h1>

      <p>timesTwo(2) = <em id="result1"></em></p>
      <p>addFive(2) = <em id="result2"></em></p>

      <script src="bundle.js"></script>
    </body>
    </html>

As you can see, I left the two results empty-- look for the *em* tags in the
above html. These will be filled with our fantastic ES2015/ES6 code below.

At this point I fire up live-server, installed above, to watch the index.html
file, as well as others, that I have created:

.. code-block:: bash

    $ live-server

This will load index.html in the default system browser-- of course, the
answers will not be there because the code still needs to be written.

**Note:**
To be clear, make sure that you are in the root project directory, where the
index.html file is located, when running the live-server command. It also
helpful to start this up in another terminal so that the messages from
live-server can be monitored/ignored and it is easy to shutdown (use
control-c). Or, if you use tmux or screen, open a new window and start
live-server there.

lib.js and main.js
------------------

Next, we create out ES2015/ES6 code in two files so that we can illustrate
import and export. First, let's create lib.js (again, motivated by original
code from Mark Brown's post; link above):

.. code-block:: JavaScript

    // lib.js
    const timesTwo = (number) => number * 2
    const addFive = (number) => number + 5
    
    export {
      timesTwo,
      addFive
    }

and then, main.js that uses the functions defined in lib.js and changes the 
contents of index.html

.. code-block:: JavaScript

    // main.js
    import {timesTwo, addFive} from './lib.js'
    
    document.getElementById('result1').textContent = timesTwo(2)
    document.getElementById('result2').textContent = addFive(2)


Okay, that's our ES2015/ES6 code, but we still need to use `Babel`_ to
transpile the code and `webpack`_ to create the bundle.js file.

babel and webpack
-----------------

Next, we install the babel requirements for our project using npm:

.. code-block:: bash

    $ npm install --save-dev babel-loader babel-core babel-preset-es2015  

The install command, with the --save-dev switch, will install the babel-related
code locally (in the node_modules directory) and save the requirements in the
packages.json file.

Next, we create a file called webpack.config.js that will use `Babel`_ to
transpile and create the bundle.js that is imported and used by index.html.
The contents are (this is motivated by Stuart Memo's post; links above):

.. code-block:: JavaScript

    // webpack.config.js
    module.exports = {
      entry: './src/main.js',
      output: {
        filename: 'bundle.js'
      },
      module: {
        loaders: [
          {
            test: /\.js$/,
            exclude: /node_modules/,
            loader: 'babel',
            query: {
              presets: ['es2015']
            }
          }
        ]
      }
    };

Finally, we call webpack in the project root directory -- the same level as the
webpack.config.js, index.html and package.json files. To be concrete, the
project looks like this:

.. code:: bash

    ├── node_modules
    │   ├── babel-core
    │   ├── babel-loader
    │   ├── babel-preset-es2015
    │   └── webpack
    ├── src
    │   ├── lib.js
    │   └── main.js
    ├── index.html
    ├── package.json
    └── webpack.config.js
    
Hopefully that's clear.  Now run webpack, the result should look something like
this:

.. code:: bash

    $ webpack
    Hash: 33586f23235394783d03
    Version: webpack 1.13.1
    Time: 3413ms
        Asset     Size  Chunks             Chunk Names
    bundle.js  1.99 kB       0  [emitted]  main
        + 2 hidden modules

Now the index.html page, being displayed and updated with live-server, should
show calculated values inserted into the page-- very cool.

adding npm packages
-------------------

As a final example, again motivated by Mark Brown's post, I will install
lodash and use that do the sum in addFive. The point of this is mainly
to show that it is possible -- also very useful! It turns out that I have
already done most of the hard work. First, I install lodash:

.. code:: bash

    $ npm install --save-dev lodash

Next, I modify the lib.js to use lodash, as below:

.. code-block:: JavaScript

    // lib.js
    import sum from 'lodash/sum'
    
    const timesTwo = (number) => number * 2
    const addFive = (number) => sum([number, 5])
    
    export {
      timesTwo,
      addFive
    }

Notice that I only make two small changes:

1. import sum from lodash
2. change the addFive function to use sum

Otherwise, there are no changes. To make this live, we need to run webpack
again to transpile to ES5 and live-server will automatically refresh the new
code:

.. code:: bash

    $ webpack
    Hash: 733b2ca4f2f0c808b86e
    Version: webpack 1.13.1
    Time: 3619ms
        Asset     Size  Chunks             Chunk Names
    bundle.js  3.91 kB       0  [emitted]  main
        + 5 hidden modules


That's it -- I'm coding in ES2015/ES6 and running it in the browser.  Try it out
and see what you think. Also, don't forget to checkout the motivating posts by
Mark Brown and Stuart Memo -- links at the top of the post.

.. _Babel: https://babeljs.io/
.. _webpack: https://webpack.github.io/
.. _live-server: https://www.npmjs.com/package/live-server 

.. author:: default
.. categories:: none
.. tags:: javascript, npm, nodejs, babel, webpack
.. comments::

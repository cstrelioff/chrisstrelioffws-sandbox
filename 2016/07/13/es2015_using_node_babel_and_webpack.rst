ES2015 using Node, Babel and Webpack
====================================

In this post I will cover setting up a project that uses ES2015-- modern
JavaScript-- that will still work in current web browsers.  The trick here
is to use `Babel`_ to *transpile* ES2015 code into something that can run
on current browsers. Why do this? Well, ES2015 is the future of JavaScript and
I'd like to start using it now. All readers should be aware that **I 
am not an expert**. This post is as much for me to remember what I did as to
inform others on what to do. So, let me know if you have better ways to do this
or you find mistakes in the comments at the end of the post.

.. more::

First, to get started, I would like to credit posts by others that really
helped me sort this out (however, all mistakes are my own). You should check
there out as well:

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

**I will be re-tooling the examples from both of the above authors**. So,
credit to both authors for original source material as well as motivation!!!

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
globally: `webpack`_ and `live-server`_. On Ubuntu global installs require
admin permissions, so we install with:

.. code:: bash

    $ sudo npm install -g live-server webpack


project setup
-------------

Next, I will create a project directory and use npm to create a
:code:`package.json` file

.. code:: bash

    $ mkdir es2015-project
    $ cd es2015-project/
    $ npm init -y

Using the **-y** tag forces the defaults to be used for :code:`package.json`
and the resulting file looks something like this::

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

Next, we create some directories and files that we will fill with code:

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
      <title>es2015-proejct</title>
    </head>
    <body>
      <h1>Results</h1>

      <p>timesTwo(2) = <em id="result1"></em></p>
      <p>addFive(2) = <em id="result2"></em></p>

      <script src="bundle.js"></script>
    </body>
    </html>

As you can see, I left the two results empty. These will filled in with our
fantastic code.  At this point I/you/we can fire-up live-server, installed
above, to watch the index.html file we have created:

.. code-block:: bash

    $ live-server

To be clear, make sure you are in the root project directory where the
index.html file is located.

lib.js and main.js
------------------

Next, we create out es2015 code in two files so that we can illustrate import
and export of code. First, let's create lib.js (again, original code from
Mark Brown's post; link above):

.. code-block:: JavaScript

    // lib.js
    const timesTwo = (number)=> number * 2
    const addFive = (number)=> number + 5
    
    export {
      timesTwo,
      addFive
    }

and then, main.js that uses the functions defined in lib.js and changes the 
contents of index.html

.. code-block:: JavaScript

    // main.js
    const lib = require('./lib.js');
    
    // set html text using lib.js functions
    document.getElementById('result1').textContent = lib.timesTwo(2);
    document.getElementById('result2').textContent = lib.addFive(2);

Okay, that's our ES2105 code, but we still need to use `Babel`_ to transpile the
code and webpack to create the bundle.js file.

babel and webpack
-----------------

Next, we install the babel requirements for our project using npm:

.. code-block:: bash

    $ npm install --save-dev babel-loader babel-core babel-preset-es2015  

The **--save-dev** will install the babel-related code locally, saving the
requirements in the packages.json file.

Next, we create a file called webpack.config.js that will use babel to
transpile and create the bundle.js that is imported and used by index.html.
The contents are:

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
webpack.config.js file. To be concrete, the project looks like this:

.. code:: bash

    $ tree . -L 2
    .
    ├── index.html
    ├── node_modules
    │   ├── babel-core
    │   ├── babel-loader
    │   ├── babel-preset-es2015
    │   └── webpack
    ├── package.json
    ├── src
    │   ├── lib.js
    │   └── main.js
    └── webpack.config.js
    
    6 directories, 5 files

and if you do an **ls** in the root directory is should look like this:

.. code:: bash

    $ ls
    index.html  node_modules/  package.json  src/  webpack.config.js

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

Finally, for this first part, we can use **live-server** to load index.html in
the default browswer:

.. code:: bash

    $ live-server

The page should show with the calculated values inserted into the page.

adding npm packages
-------------------

As a final example, again motivated by Mark Brown's post, let's import
**lodash** and use that do the sum in **addFive**. The point of this is mainly
to show that it is possible -- also very useful!



.. _Babel: https://babeljs.io/
.. _webpack: https://webpack.github.io/
.. _live-server: https://www.npmjs.com/package/live-server 

.. author:: default
.. categories:: none
.. tags:: javascript, npm, nodejs, babel, webpack
.. comments::

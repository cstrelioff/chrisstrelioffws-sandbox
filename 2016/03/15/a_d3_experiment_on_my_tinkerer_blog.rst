A d3 experiment on my Tinkerer blog
===================================

This blog uses `Tinkerer`_, which is based on the `Sphinx`_ documentation
framework, to create static html pages from rest (rst) markup. If you are
familiar with the Python world you've probably created documentation using
Sphinx, or at the very least, you have read documenation created in Sphinx. 
Because the setup is Python-focused, it is not straightforward to write posts
that employ javascript libraries like `d3`_. This post describes my method for
doing javascript examples in `Tinkerer`_ blog posts or Sphinx docs, as well as
how to do some `d3`_.

.. more::

Raw javascript
--------------

First, let's consider a simple javascript example without using `d3`_. I will
create a html-div as well as two buttons that use javascript to insert some
text.  In the rst markup the div and buttons are created using

.. code-block:: rst

    .. raw:: html

        <div id="js_ex"
             style="padding: 20px 0px;">

          <p id="js_ex_text"
             style="padding: 10px; background: #111; color: #eee;">
             -- click write and clear ---
          </p>

          <button id="js_ex_write">
           write
          </button>
          <button id="js_ex_clear">
           clear
          </button>
        </div>

The result of the above code is shown below:

.. raw:: html

    <div id="js_ex"
         style="padding: 20px 0px;">

      <p id="js_ex_text"
         style="padding: 10px; background: #111; color: #eee;">
         -- click write and clear ---
      </p>

      <button id="js_ex_write">
       write
      </button>
      <button id="js_ex_clear">
       clear
      </button>
    </div>

The :code:`raw:: html` tag in the rst markup makes Tinkerer/Sphinx insert the
html into the document. Next, we can use javascript to change the text using
some click events. In the rst document I have:

.. code-block:: rst

    .. raw:: html
    
        <script type='text/javascript'>
          p = document.getElementById('js_ex_text');

          buttonWrite = document.getElementById('js_ex_write');
          buttonWrite.onclick = function() {
            p.innerHTML = 'Hello <strong>js</strong> world!';
          };

          buttonClear = document.getElementById('js_ex_clear');
          buttonClear.onclick = function() {
            p.innerHTML = ' -- nothing here, click write --';
          };
        </script>

Notice that the :code:`raw:: html` tag is used again and the javascript is
surrounded by the :code:`<script></script>` tags -- just as you would have to
do in normal, inline html markup.

Okay, now let's integrate some `d3`_ into a `Tinkerer`_ post or `Sphinx`_
document.

.. raw:: html

    <script type='text/javascript'>
      // get p and initialize for first load
      p = document.getElementById('js_ex_text');
      p.innerHTML = '-- click write and clear --';

      buttonWrite = document.getElementById('js_ex_write');
      buttonWrite.onclick = function() {
        p.innerHTML = 'Hello <strong>js</strong> world!';
      };

      buttonClear = document.getElementById('js_ex_clear');
      buttonClear.onclick = function() {
        p.innerHTML = ' -- nothing here, click write --';
      };
    </script>


Using d3
--------

**Linking d3**

The first step in using `d3`_ is to link to the library. I'm sure there are a
variety of ways to do this, but I chose to link to the library on all pages --
if you have a slick way to link per page/post please leave a comment below!

Given this choice, there is a standard way to add external javascript files --
see `Enabling Google Analytics`_ for an example of adding google analytics js
to a `Tinkerer`_ blog. In my case, I added *d3.min.js* (you can get the latest
version here: `d3 at github`_) to the *_static* directory and modified the
*page.html* template in my theme -- see `page template example`_ -- to include
the following::

    {%- extends "layout.html" -%}

    {% set script_files = script_files + ["_static/d3.min.js"] %}

This tells `Tinkerer`_ to link the *d3.min.js* in the header of each page. If
you are not working with a theme, create a directory *_templates* and add the 
file *page.html* with the above content. The organization would be something
like this (where *conf.py* and *master.rst* are in the base directory of the
blog):: 

    ├── conf.py
    ├── master.rst
    ├── _static
    │   ├── d3.min.js
    ├── _templates
        ├── page.html
     

That should work as well.

**Using d3 in a post**

Finally, here's a little experiment using `d3`_ that is motivated by the
classic `three little circles`_ example.  As with the simple javascript
example we have to setup an html-div that will be used:

.. code-block:: rst

    .. raw:: html
    
       <div id='vizdiv' style="padding: 20px 0px;">
       </div>

Let's put it here:

.. raw:: html

    <div id='vizdiv' style="padding: 20px 0px;">
    </div>

Next, we use the following `d3`_ code to draw some circles using data:

.. code-block:: JavaScript

   var data = [{r: 5, cy: 100, cx: 100},
               {r: 10, cy: 100, cx: 200},
               {r: 15, cy: 100, cx: 300}];

   var root = d3.select('#vizdiv').append('svg')
       .attr('width', 400)
       .attr('height', 200);
   
   root.selectAll('circle')
       .data(data).enter()
     .append('circle')
       .attr('r', function(d) {return d.r;})
       .attr('cx', function(d) {return d.cx;})
       .attr('cy', function(d) {return d.cy;})
       .attr('fill', 'steelblue');

In the rst markup for the post, this actually has to look like this:

.. code-block:: rst

    .. raw:: html
    
       <script type='text/javascript'>
       var data = [{r: 5, cy: 100, cx: 100},
                   {r: 10, cy: 100, cx: 200},
                   {r: 15, cy: 100, cx: 300}];

       var root = d3.select('#vizdiv').append('svg')
           .attr('width', 400)
           .attr('height', 200);
       
       root.selectAll('circle')
           .data(data).enter()
         .append('circle')
           .attr('r', function(d) {return d.r;})
           .attr('cx', function(d) {return d.cx;})
           .attr('cy', function(d) {return d.cy;})
           .attr('fill', 'steelblue');
       </script>

Notice that we have to use :code:`raw:: html` and the :code:`<script></script>`
tags!

.. raw:: html

   <script type='text/javascript'>
   var data = [{r: 5, cy: 100, cx: 100},
               {r: 10, cy: 100, cx: 200},
               {r: 15, cy: 100, cx: 300}];

   var root = d3.select('#vizdiv').append('svg')
       .attr('width', 400)
       .attr('height', 200);
   
   root.selectAll('circle')
       .data(data).enter()
     .append('circle')
       .attr('r', function(d) {return d.r;})
       .attr('cx', function(d) {return d.cx;})
       .attr('cy', function(d) {return d.cy;})
       .attr('fill', 'steelblue');
   </script>

Okay, that's it.  Now I'm setup to talk more about javascript and d3 on the 
blog -- very nice! If you have other ways to do this, again, please leave 
a comment!

.. _Tinkerer: http://tinkerer.me/
.. _Sphinx: http://www.sphinx-doc.org/en/stable/
.. _d3: https://d3js.org/
.. _Enabling Google Analytics: http://tinkerer.me/doc/more_tinkering.html#enabling-google-analytics
.. _page template example: https://github.com/cstrelioff/chrisstrelioffws-sandbox/blob/master/_themes/ccs_bs3/page.html
.. _d3 at github: https://github.com/mbostock/d3
.. _three little circles: https://bost.ocks.org/mike/circles/

.. author:: default
.. categories:: none
.. tags:: tinkerer, javascript, d3
.. comments::

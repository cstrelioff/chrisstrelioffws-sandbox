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
create a html-div and use javascript to insert some text.  In the rst markup
the div is created using

.. code-block:: rst

    .. raw:: html

        <div id="js_example"></div>

This does not appear on the html page that is created by `Tinkerer`_ or 
`Sphinx`_ (to be clear, it's not visible), but the html element is in the page
to be used --- I'll put it below:

.. raw:: html

    <div id="js_example"></div>

The :code:`raw:: html` tag in the rst markup makes Tinkerer/Sphinx insert the
html, in this case the div with id :code:`js_example`, into the document. Next,
we can use javascript to insert some text. Again, this is hidden in the
resulting html you are looking at, but in the rst document I have:

.. code-block:: rst

    .. raw:: html
    
        <script type='text/javascript'>
          v = document.getElementById('js_example');
          v.innerHTML = '<p class=\'lead\'>' +
                        'Hello <strong>js</strong> world!i' +
                        '</p>';
        </script>

Notice that the :code:`raw:: html` tag is used again and the javascript is
surrounded by the :code:`<script></script>` tags -- just as you would have to
do in normal, inline html markup. You can use the *view source* on your browser
to find the :code:`js_example` div and see there is no text, or you'll have to
take my word that the javascript is doing the writing.

Okay, now let's integrate some `d3`_ into `Tinkerer`_ post or `Sphinx`_
document.

.. raw:: html

    <script type='text/javascript'>
      v = document.getElementById('js_example');
      v.innerHTML = '<p class=\'lead\'>' +
                    'Hello <strong>js</strong> world!' +
                    '</p>';
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
    
       <div id='vizdiv'></div>

Let's put it here:

.. raw:: html

   <div id='vizdiv'></div>

Next, we use the following `d3`_ code to draw some circle using data:

.. code-block:: JavaScript

   var c_data = [{r: 5, cy: 100, cx: 100},
                 {r: 10, cy: 100, cx: 200},
                 {r: 15, cy: 100, cx: 300}];

   var root = d3.select('#vizdiv').append('svg')
       .attr('width', 400)
       .attr('height', 200)
       .style('border', '1px solid black');
   
   root.selectAll('circle')
       .data(c_data).enter()
     .append('circle')
       .attr('r', function(d) {return d.r;})
       .attr('cx', function(d) {return d.cx;})
       .attr('cy', function(d) {return d.cy;})
       .attr('fill', 'steelblue');

In the rst markup for the post, this actually has to look like this:

.. code-block:: rst

    .. raw:: html
    
       <script type='text/javascript'>
       var c_data = [{r: 5, cy: 100, cx: 100},
                     {r: 10, cy: 100, cx: 200},
                     {r: 15, cy: 100, cx: 300}];
    
       var root = d3.select('#vizdiv').append('svg')
           .attr('width', 400)
           .attr('height', 200)
           .style('border', '1px solid black');
       
       root.selectAll('circle')
           .data(c_data).enter()
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
   var c_data = [{r: 5, cy: 100, cx: 100},
                 {r: 10, cy: 100, cx: 200},
                 {r: 15, cy: 100, cx: 300}];

   var root = d3.select('#vizdiv').append('svg')
       .attr('width', 400)
       .attr('height', 200)
       .style('border', '1px solid black');
   
   root.selectAll('circle')
       .data(c_data).enter()
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

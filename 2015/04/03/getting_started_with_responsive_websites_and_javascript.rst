.. _responsive website:

Getting started with responsive websites and JavaScript
=======================================================

In this post I'm going to describe two basic web pages I've been working on: 

* a basic responsive page, and
* a responsive page that uses JavaScript to detect the current size of the 
  screen.

My goal here is to use *basic* HTML, CSS and JavaScript -- no js libraries -- to
help myself learn JavaScript and responsive data visualization techniques. 
That said, I'm not an expert, and the examples should be considered with that
in mind.  Please comment at the end of the post if you have better, or
different, ways of doing the same thing.

.. more::

A basic responsive page
-----------------------

First, credit where credit is due: this page draws directly from the example
website developed in Clarissa Peterson's book `Learning Responsive Web Design`_.
I found this book to very helpful in getting started. So, what does the
resulting responsive page look like? You can see it in action here:
`basic responsive page`_ and all of the code is available in this *gist*:
`gist for basic responsive page`_.  Try *resizing your screen* to see how the
page adapts to large vs small screens.  In particular, for 

* **large screens** the *aside* element should float to the right of the 
  *article* element, whereas for
* **small screens** the *aside* element should be below the *article* element
  and occupy the full width of the screen.
  
How does this work?  If you look at `index.html for the basic responsive page`_,
the code is really pretty simple. All of the magic happens in a few places:

* **viewport:** the meta tag, in the :code:`index.html` header section, sets
  the viewport using sensible values for the width and initial scale.
* **media queries:**  the media query (see lines 58-72), found at the bottom of 
  `main.css for the basic responsive page`_, changes the article, aside and
  footer properties for larger screens-- changing widths, making the aside float
  right, etc. The default properties (for small screens) are set at the top of
  the css file and are *overridden* when the width of the screen is greater than
  the specified 38em.  You can play with this value to change the *breakpoint*,
  the width at which different large-screen style takes effect.  Of course, more
  than one media query is allowed, so the control of layout for different screen
  sizes can be controlled with great specificity.  We'll stick with one media
  query in this case, keeping things simple.

The only other parts to mention, briefly,  are the `reset.css`_ by Eric Meyer --
see `Eric Meyer's reset.css`_ for more information.  Basically, this css file
zeroes-out style settings that are later set in the :code:`main.css` file.
Finally, there is the :code:`fullpage` div, which sets a maximum width and auto
margins. These settings keep the page from getting too wide and centers the
content on large screens, like a big monitor.

So, that's it for the basic responsive page.  Do you have another way to do
things like this?  Please comment below and provide links!


Using JavaScript to find screen and element dimensions
------------------------------------------------------

Next, we add a little JavaScript to figure out how large the screen and various
HTML elements are as the screen is resized.  A live version of the page is
here: `responsive page with js`_-- again, *try resizing the page* to see how
the dimensions of the elements adjust.  All of the code is available in this
`gist for responsive page with js`_.

So, how does this example work?  As you might expect, much of this example is
exactly same as the basic responsive page discussed above.  A JavaScript file,
`main.js for responsive page with js`_, is added with all of the code and is
linked in the `index.html for responsive page with js`_ on line 59.  In
addition, a few :code:`div` elements have been added to the :code:`index.html`
as place-holders for writing the dimensions of the various HTML elements.  For
example, see :code:`<div id="article_info"></div>` (index.html, line 30) and 
:code:`<div id="footer_info"></div>` (index.html, line 44).

Next onto the JavaScript file :code:`main.js`.  There are two functions that do
all of the work:

* :code:`write_dimensions()` (line 9) -- this function takes the name of the
  HTML element, which is assigned to :code:`div_id` in the function, and the
  name of the :code:`div` where the output is going to be written, which is
  assigned to :code:`output_id`.

.. code-block:: javascript

    function write_dimensions(div_id, output_id) {
        var div = document.getElementById(div_id);
        var div_info = document.getElementById(output_id);
    
        var w = Math.round(div.getBoundingClientRect().width * 100)/100;
        var h = Math.round(div.getBoundingClientRect().height * 100)/100;
    
        if (w > 400) {
            div_info.innerHTML = "<p>" + div_id + "-- " + " width: " + w +
                                 " height: " + h + "</p>"; 
        } else {
            div_info.innerHTML = "<p>" + div_id + "--<br>" + " width: " + w +
                                 "<br>height: " + h + "</p>"; 
        }
    }

The first two lines of the function get the HTML elements, and the :code:`w`
and :code:`h` variables are assigned the width and height, respectively.  The
key expressions here are :code:`div.getBoundingClientRect().width` and
:code:`div.getBoundingClientRect().height`, the rest is just rounding to two
decimal places. Finally, if the width is greater than 400px the :code:`div_info`
is assigned output on *one line*. However, if the width is less than or equal
to 400px the output is split onto multiple lines -- see the :code:`<br>`'s. 
This function handles the writing of the dimensions for all elements except the
window.

* :code:`write_window_dimensions()` (line 26) -- this function handles the
  dimensions for the complete window.  The command for getting the window's
  dimensions is slightly different from the generic HTML elements, so I have
  this separate function. The code for the function is:

.. code-block:: javascript

    function write_window_dimensions() {
        var header_info = document.getElementById("window_info");
    
        var width = window.innerWidth;
        var height = window.innerHeight;
    
        if (width > 445) {
            header_info.innerHTML = "<p>window-- width: " + width +
                                    " height: " + height + "</p>";
        } else {
            header_info.innerHTML = "<p>window--<br>width: " + width +
                                    "<br>height: " + height + "</p>";
        }
    
    }

Comparing the above with the previous function-- it should be easy to identify
the different method for getting height and width.  I don't bother passing the
HTML element and div id's here because they are known and only take on one value
that is hard-coded into the function.

With these two function defined, we can call them repeatedly.  First, we call
the function using the :code:`window.onload` (top of :code:`main.js`) to get
the information when the page is first loaded.  Next, we define a
:code:`window.EventListener()` that calls all of the functions whenever the
window is resized. This enables the information about the dimensions to be
updated as the window is resized.

So, that's it for this post.  In the future I'll be using the code to work on
responsive data visualization, which can respond to different screen sizes in
useful ways.  As always, comments are appreciated.

.. _Learning Responsive Web Design: http://shop.oreilly.com/product/0636920029199.do
.. _basic responsive page: http://bl.ocks.org/cstrelioff/raw/a4ed0e527cc7610342ce/
.. _gist for basic responsive page: https://gist.github.com/cstrelioff/a4ed0e527cc7610342ce
.. _index.html for the basic responsive page: https://gist.github.com/cstrelioff/a4ed0e527cc7610342ce#file-index-html
.. _main.css for the basic responsive page: https://gist.github.com/cstrelioff/a4ed0e527cc7610342ce#file-main-css

.. _reset.css: https://gist.github.com/cstrelioff/a4ed0e527cc7610342ce#file-reset-css
.. _Eric Meyer's reset.css: http://meyerweb.com/eric/tools/css/reset/

.. _responsive page with js: http://bl.ocks.org/cstrelioff/raw/15cd767896b0eed7735a/
.. _gist for responsive page with js: https://gist.github.com/cstrelioff/15cd767896b0eed7735a/
.. _main.js for responsive page with js: https://gist.github.com/cstrelioff/15cd767896b0eed7735a#file-main-js
.. _index.html for responsive page with js: https://gist.github.com/cstrelioff/15cd767896b0eed7735a#file-index-html

.. author:: default
.. categories:: none
.. tags:: javascript, html5, css
.. comments::

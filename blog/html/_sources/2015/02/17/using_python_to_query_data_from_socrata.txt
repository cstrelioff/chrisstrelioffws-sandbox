Using Python to query data from Socrata
=======================================

I've started going to `Open Oakland`_ meetings on Tuesday nights.  The group
works on a variety of projects related to making city data more accessible and
usable for Oakland citizens by creating websites, or *apps*.  Check out
`Open Oakland Projects`_ and `Open Oakland Blog`_ for more information on the
types of things going on and come to a meeting if you're interested in helping
out.

.. more::

One of the many tasks involved in getting an *app* up and running is obtaining
the underlying data in some way. In this example, I'll focus on getting
information about trees in Oakland from the Oakland data portal at
`data.oaklandnet.com`_. This portal is *powered by* `Socrata`_, which provides
an API (see `SODA`_) for querying the data-- I'll do this using Python.  To be 
clear this type of query can be done for any data hosted at the data portal, so
adapt away if there is different information that you want from
`data.oaklandnet.com`_, or any other `Socrata`_-powered portal.

Now, let's focus on our specific example: getting information about
`trees in Oakland`_ .  To do this query, we need the url for this specific
dataset. This can be found by clicking on the **Export** button, then the
**SODA API** tab.  The **API Endpoint** has the url that we want::

    https://data.oaklandnet.com/resource/4jcx-enxf.json

which returns data in *json* (JavaScript Object Notation) format. Again, this
url corresponds to *data about trees in Oakland*, nothing else. Other data will
have its own, unique url for queries.

We get the first 5 trees using the :code:`$limit` and :code:`$offset` arguments
to get the desired number of trees and use :code:`$order` to make sure that we
proper paging from later queries for trees 6-10, 11-15, etc.  The
:code:`urllib` encodes the arguments and we use :code:`urllib2` to make the
call to the API.  The raw form of the data is a list of *json* data structures--
the :code:`json` library makes these data into dictionaries in Python (or,
strings that can be turned into dictionaries-- see example). The code below
queries for tree data using the arguments we pass -- these arguments can be
changed to get other information.  The libraries used are available by default,
at least in Python 2.7, so this should be easy for everyone to use.


.. code-block:: python

    from __future__ import print_function
    
    import urllib, urllib2
    import json
    
    def get_trees(args):
        """Get trees using passed arguments."""
    
        api = "https://data.oaklandnet.com/resource/4jcx-enxf.json?"
        try:
            url = api + urllib.urlencode(args)
            data = urllib2.urlopen(url)
            response_data = json.load(data)
            data.close()
        except urllib2.HTTPError, e:
            print("HTTP error: {}".format(e.code))
        except urllib2.URLError, e:
            print("Network error: {}".format(e.reason.args[1]))
    
        return response_data
    
    # make request for first five trees and order by id
    args = {"$order": ":id", "$limit": 5, "$offset": 0}
    five_trees = get_trees(args)
    
    # print out the raw data
    for n, tree in enumerate(five_trees):
        print("-- Tree {}:\n{}".format(n+1, tree), end='\n\n')
    

::

    -- Tree 1:
    {u'location_1': {u'latitude': u'37.80505999961946', u'needs_recoding':
    False, u'human_address':
    u'{"address":"1421","city":"Oakland","state":"Ca","zip":""}',
    u'longitude': u'-122.27301999967312'}, u'wellwidth': u'4',
    u'welllength': u'4', u'stname': {u'needs_recoding': False,
    u'human_address': u'{"address":"FRANK H OGAWA
    PZ","city":"","state":"","zip":""}'}, u'lowwell': u'None',
    u'objectid': u'1', u'pareawidth': u'0', u'species': u'Platanus
    acerifolia'}
    
    -- Tree 2:
    {u'location_1': {u'latitude': u'37.80505999961946', u'needs_recoding':
    False, u'human_address':
    u'{"address":"0","city":"Oakland","state":"Ca","zip":""}',
    u'longitude': u'-122.27301999967312'}, u'wellwidth': u'5',
    u'welllength': u'5', u'stname': {u'needs_recoding': False,
    u'human_address': u'{"address":"11TH
    ST","city":"","state":"","zip":""}'}, u'lowwell': u'None',
    u'objectid': u'2', u'pareawidth': u'0', u'species': u'Platanus
    acerifolia'}
    
    -- Tree 3:
    {u'location_1': {u'latitude': u'37.80505999961946', u'needs_recoding':
    False, u'human_address':
    u'{"address":"561","city":"Oakland","state":"Ca","zip":""}',
    u'longitude': u'-122.27301999967312'}, u'wellwidth': u'3',
    u'welllength': u'3', u'stname': {u'needs_recoding': False,
    u'human_address': u'{"address":"22ND
    ST","city":"","state":"","zip":""}'}, u'lowwell': u'Moderate',
    u'objectid': u'3', u'pareawidth': u'0', u'species': u'Gleditsia
    triacanthos'}
    
    -- Tree 4:
    {u'location_1': {u'latitude': u'37.80505999961946', u'needs_recoding':
    False, u'human_address':
    u'{"address":"3025","city":"Oakland","state":"Ca","zip":""}',
    u'longitude': u'-122.27301999967312'}, u'wellwidth': u'3',
    u'welllength': u'3', u'stname': {u'needs_recoding': False,
    u'human_address':
    u'{"address":"BROADWAY","city":"","state":"","zip":""}'}, u'lowwell':
    u'Low', u'objectid': u'4', u'pareawidth': u'0', u'species': u'Photinia
    sp'}
    
    -- Tree 5:
    {u'location_1': {u'latitude': u'37.80505999961946', u'needs_recoding':
    False, u'human_address':
    u'{"address":"1331","city":"Oakland","state":"Ca","zip":""}',
    u'longitude': u'-122.27301999967312'}, u'wellwidth': u'4',
    u'welllength': u'9', u'stname': {u'needs_recoding': False,
    u'human_address': u'{"address":"HARRISON
    ST","city":"","state":"","zip":""}'}, u'lowwell': u'None',
    u'objectid': u'5', u'pareawidth': u'0', u'species': u'Lophostemon
    confertus'}
    
    
    



We can also extract just the information we want by pulling street number,
street name and tree species from the query data:


.. code-block:: python

    for n, tree in enumerate(five_trees):
        # accessing the fields is fairy complicated
        st_num = eval(tree[u'location_1'][u'human_address'])['address']
        st_name =eval(tree[u'stname'][u'human_address'])['address']
        spec = tree[u'species']
        print("-- Tree {}: {}".format(n+1, spec))
        print("address: {} {}".format(st_num, st_name), end='\n\n')
    

::

    -- Tree 1: Platanus acerifolia
    address: 1421 FRANK H OGAWA PZ
    
    -- Tree 2: Platanus acerifolia
    address: 0 11TH ST
    
    -- Tree 3: Gleditsia triacanthos
    address: 561 22ND ST
    
    -- Tree 4: Photinia sp
    address: 3025 BROADWAY
    
    -- Tree 5: Lophostemon confertus
    address: 1331 HARRISON ST
    
    
    



Notice that I had to do some fairly complicated things to get at the street
number and name. In particular, I had to use :code:`eval` to create a Python
dictionary from a string.  As I did above, I suggest querying a small number of
records and playing around with data returned to get a feel for what is there.

Some final notes:

* The default :code:`$limit` is set to 1,000 records with a maximum of 50,000.
  This means the full tree data set-- which has 38,613 records-- can pulled with
  one query to the api:

.. code:: python

    args2 = {"$limit": 40000, "$offset": 0, "$order": ":id"}
    all_data = get_trees(args2)

* Another Python example using **pandas** and **bokeh**, these are Python
  packages that you would have to install before doing the example, is available
  at `Socrata Python example`_.

* `Socrata`_ has a broader query language that is SQL-like, allowing to more
  complicated queries, call `SoQL`_ (`Socrata`_ query language).  Check the
  links out for more of what is possible.

* The code for this example is available at `this gist`_ as
  :code:`ex004_socrata_api.py`

That's it for this post.  As always, leave comments and corrections in the
comments below.

.. _Open Oakland: https://www.openoakland.org/
.. _Open Oakland Projects: https://www.openoakland.org/projects/
.. _Open Oakland Blog: https://www.openoakland.org/blog/
.. _data.oaklandnet.com: https://data.oaklandnet.com/
.. _trees in Oakland: https://data.oaklandnet.com/Environmental/Oakland-Street-Trees/4jcx-enxf

.. _Socrata Python example: http://dev.socrata.com/consumers/examples/data-visualization-with-python.html
.. _Socrata: http://www.socrata.com/
.. _SODA: http://dev.socrata.com/consumers/getting-started.html
.. _SoQL: http://dev.socrata.com/docs/queries.html
.. _this gist: https://gist.github.com/cstrelioff/aec738d406b1a45f0ed3

.. author:: default
.. categories:: none
.. tags:: python, json, api, Socrata, Open Oakland
.. comments::

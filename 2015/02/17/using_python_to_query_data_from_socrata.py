
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

for n, tree in enumerate(five_trees):
    # accessing the fields is fairy complicated
    st_num = eval(tree[u'location_1'][u'human_address'])['address']
    st_name =eval(tree[u'stname'][u'human_address'])['address'] 
    spec = tree[u'species']
    print("-- Tree {}: {}".format(n+1, spec))
    print("address: {} {}".format(st_num, st_name), end='\n\n')
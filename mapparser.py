# -*- coding: utf-8 -*-
"""
Created on Sun Jul 02 12:56:16 2017

@author: Dell
"""

"""
Parse the OSM file and count the numbers of unique tag
"""

import xml.etree.cElementTree as ET
import pprint


OSMFILE = "ahmedabad_4.osm"

def count_tags(filename):
    tags = {}
    for event, elem in ET.iterparse(filename):
        if elem.tag in tags: 
            tags[elem.tag] += 1
        else:
            tags[elem.tag] = 1
    return tags
    
pprint.pprint(count_tags(OSMFILE))
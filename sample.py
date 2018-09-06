# -*- coding: utf-8 -*-
"""
Created on Sun Jul 02 14:05:09 2017

@author: Dell
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Created on Tue Jul 04 11:28:43 2017

@author: Dell
"""

# Use cElementTree or lxml if too slow



import xml.etree.ElementTree as ET  

OSM_FILE = "ahmedabad_4.osm"  
SAMPLE_FILE = "ahmedabad_sample.osm"

# Parameter: take every k-th top level element
k = 100 

def get_element(osm_file, tags=('node', 'way', 'relation')):
    """Yield element if it is the right type of tag
    Reference:
    http://stackoverflow.com/questions/3095434/inserting-newlines-in-xml-file-generated-via-xml-etree-elementtree-in-python
    """
    context = iter(ET.iterparse(osm_file, events=('start', 'end')))
    _, root = next(context)
    for event, elem in context:
        if event == 'end' and elem.tag in tags:
            yield elem
            root.clear()


with open(SAMPLE_FILE, 'wb') as output:
    output.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    output.write('<osm>\n  ')

    # Write every kth top level element
    for i, element in enumerate(get_element(OSM_FILE)):
        if i % k == 0:
            output.write(ET.tostring(element, encoding='utf-8'))

    output.write('</osm>')
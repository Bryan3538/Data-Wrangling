#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Your task is to use the iterative parsing to process the map file and
find out not only what tags are there, but also how many, to get the
feeling on how much of which data you can expect to have in the map.
Fill out the count_tags function. It should return a dictionary with the 
tag name as the key and number of times this tag can be encountered in 
the map as value.

Note that your code will be tested with a different data file than the 'example.osm'
"""
import xml.etree.cElementTree as ET
import pprint

def count_tags(filename):
        # YOUR CODE HERE
        #this version uses the more efficient method for parsing large files
        tags = {}
        context = ET.iterparse(filename, events=("start", "end"))
        context = iter(context)
        event, root = context.next()

        for event, elem in context:
            if elem.tag in tags:
                tags[elem.tag] += 1
            else:
                tags[elem.tag] = 1
                print "Added tag:\t", elem.tag
            
            root.clear()
        return tags


def test():

    #tags = count_tags('example.osm')
    tags = count_tags('chicago_illinois.osm')
    pprint.pprint(tags)
    # assert tags == {'bounds': 1,
    #                  'member': 3,
    #                  'nd': 4,
    #                  'node': 20,
    #                  'osm': 1,
    #                  'relation': 1,
    #                  'tag': 7,
    #                  'way': 1}

    

if __name__ == "__main__":
    test()


"""
    OUTPUT:
    {'bounds': 2,
     'member': 87,222,
     'nd': 19,188,152,
     'node': 16,267,602,
     'osm': 1,
     'relation': 7,418,
     'tag': 12,673,756,
     'way': 2,278,888}
"""
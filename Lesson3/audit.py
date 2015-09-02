#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a
cleaning idea and then clean it up. In the first exercise we want you to audit
the datatypes that can be found in some particular fields in the dataset.
The possible types of values can be:
- NoneType if the value is a string "NULL" or an empty string ""
- list, if the value starts with "{"
- int, if the value can be cast to int
- float, if the value can be cast to float, but CANNOT be cast to int.
   For example, '3.23e+07' should be considered a float because it can be cast
   as float but int('3.23e+07') will throw a ValueError
- 'str', for all other values

The audit_file function should return a dictionary containing fieldnames and a 
SET of the types that can be found in the field. e.g.
{"field1: set([float, int, str]),
 "field2: set([str]),
  ....
}

All the data initially is a string, so you have to do some checks on the values
first.
"""
import codecs
import csv
import json
import pprint

CITIES = 'cities.csv'

FIELDS = ["name", "timeZone_label", "utcOffset", "homepage", "governmentType_label", "isPartOf_label", "areaCode", "populationTotal", 
          "elevation", "maximumElevation", "minimumElevation", "populationDensity", "wgs84_pos#lat", "wgs84_pos#long", 
          "areaLand", "areaMetro", "areaUrban"]

def audit_file(filename, fields):
    fieldtypes = {}
    for field in FIELDS:
        fieldtypes[field] = set()
    # YOUR CODE HERE
    with open(filename, "r") as f:
      dataset = csv.DictReader(f)
      
      next(dataset)
      next(dataset)
      next(dataset)

      datatype = None
      for row in dataset:
        for field in FIELDS:
          if islist(row[field]):
            datatype = list
          elif isfloat(row[field]):
            datatype = float
          elif isint(row[field]):
            datatype = int
          elif row[field].strip().lower() == "null":
            datatype = type(None)
          else:
            datatype = str

          #if field == "areaLand":
            #print datatype, row[field]

          if not datatype in fieldtypes[field]:
            fieldtypes[field].add(datatype)

    return fieldtypes

def isint(obj):
  try:
    int(obj)
    return True
  except ValueError:
    return False

def isfloat(obj):
  try:
    float(obj)
    return True
  except ValueError:
    return False

def islist(string):
  return string.strip()[0] == "{"



def test():
    fieldtypes = audit_file(CITIES, FIELDS)

    pprint.pprint(fieldtypes)

    assert fieldtypes["areaLand"] == set([type(1.1), type([]), type(None)])
    assert fieldtypes['areaMetro'] == set([type(1.1), type(None)])
    
if __name__ == "__main__":
    test()

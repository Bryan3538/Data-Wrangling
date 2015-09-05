#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with another type of infobox data, audit it, clean it, 
come up with a data model, insert it into a MongoDB and then run some queries against your database.
The set contains data about Arachnid class.
Your task in this exercise is to parse the file, process only the fields that are listed in the
FIELDS dictionary as keys, and return a list of dictionaries of cleaned values. 

The following things should be done:
- keys of the dictionary changed according to the mapping in FIELDS dictionary
- trim out redundant description in parenthesis from the 'rdf-schema#label' field, like "(spider)"
- if 'name' is "NULL" or contains non-alphanumeric characters, set it to the same value as 'label'.
- if a value of a field is "NULL", convert it to None
- if there is a value in 'synonym', it should be converted to an array (list)
  by stripping the "{}" characters and splitting the string on "|". Rest of the cleanup is up to you,
  eg removing "*" prefixes etc. If there is a singular synonym, the value should still be formatted
  in a list.
- strip leading and ending whitespace from all fields, if there is any
- the output structure should be as follows:
{ 'label': 'Argiope',
  'uri': 'http://dbpedia.org/resource/Argiope_(spider)',
  'description': 'The genus Argiope includes rather large and spectacular spiders that often ...',
  'name': 'Argiope',
  'synonym': ["One", "Two"],
  'classification': {
                    'family': 'Orb-weaver spider',
                    'class': 'Arachnid',
                    'phylum': 'Arthropod',
                    'order': 'Spider',
                    'kingdom': 'Animal',
                    'genus': None
                    }
}
  * Note that the value associated with the classification key is a dictionary with
    taxonomic labels.
"""
import codecs
import csv
import json
import pprint
import re

DATAFILE = 'arachnid.csv'
OUTFILE = "arachnid.json"
FIELDS ={'rdf-schema#label': 'label',
         'URI': 'uri',
         'rdf-schema#comment': 'description',
         'synonym': 'synonym',
         'name': 'name',
         'family_label': 'family',
         'class_label': 'class',
         'phylum_label': 'phylum',
         'order_label': 'order',
         'kingdom_label': 'kingdom',
         'genus_label': 'genus'}


def process_file(filename, fields):

    process_fields = fields.keys()
    data = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for i in range(3):
            l = reader.next()

        for line in reader:
          # YOUR CODE HERE
          #clean whitespace and convert to new format
          for field in FIELDS:
            line[field] = line[field].strip()
          #trim redundant description data
          line['rdf-schema#label'] = trim_redundancy(line['rdf-schema#label'])
          #convert NULL to None
          line = null_to_none(line)
          #if name is null or invalid, set it to label
          line['name'] = process_name(line)
          
          #convert synonyms into lists
          if not line['synonym'] == None:
            line['synonym'] = parse_array(line['synonym'])

          arachnid = {
            FIELDS["synonym"]: line["synonym"], 
            FIELDS["name"]: line["name"], 
            "classification": {
                FIELDS["kingdom_label"]: line["kingdom_label"], 
                FIELDS["family_label"]: line["family_label"], 
                FIELDS["order_label"]: line["order_label"], 
                FIELDS["phylum_label"]: line["phylum_label"], 
                FIELDS["genus_label"]: line["genus_label"], 
                FIELDS["class_label"]: line["class_label"]
            }, 
            FIELDS["URI"]: line["URI"], 
            FIELDS["rdf-schema#label"]: line["rdf-schema#label"], 
            FIELDS["rdf-schema#comment"]: line["rdf-schema#comment"]
          }

          data.append(arachnid)
    return data

def trim_redundancy(label):
  if "(" in label and ")" in label:
    label = label[:label.find("(")].strip()

  return label

def null_to_none(dic):
  for field in FIELDS:
    if dic[field].lower() == "null":
      dic[field] = None
  return dic

def process_name(dic):
  if dic['name'] == None or re.match("^[a-zA-Z0-9]*$", dic['name']) == None:
    return dic['rdf-schema#label']
  else:
    return dic['name']

def parse_array(v):
    if (v[0] == "{") and (v[-1] == "}"):
        v = v.lstrip("{")
        v = v.rstrip("}")
        v_array = v.split("|")
        v_array = [i.strip() for i in v_array]
        return v_array
    return [v]

def write_to_file(data, outfile):
  json.dump(data, open(outfile, "wb"))


def test(data):
    print "Your first entry:"
    pprint.pprint(data[0])
    first_entry = {
        "synonym": None, 
        "name": "Argiope", 
        "classification": {
            "kingdom": "Animal", 
            "family": "Orb-weaver spider", 
            "order": "Spider", 
            "phylum": "Arthropod", 
            "genus": None, 
            "class": "Arachnid"
        }, 
        "uri": "http://dbpedia.org/resource/Argiope_(spider)", 
        "label": "Argiope", 
        "description": "The genus Argiope includes rather large and spectacular spiders that often have a strikingly coloured abdomen. These spiders are distributed throughout the world. Most countries in tropical or temperate climates host one or more species that are similar in appearance. The etymology of the name is from a Greek name meaning silver-faced."
    }

    assert len(data) == 76
    assert data[0] == first_entry
    assert data[17]["name"] == "Ogdenia"
    assert data[48]["label"] == "Hydrachnidiae"
    assert data[14]["synonym"] == ["Cyrene Peckham & Peckham"]

    

if __name__ == "__main__":
  data = process_file(DATAFILE, FIELDS)
  test(data)
  write_to_file(data, OUTFILE)
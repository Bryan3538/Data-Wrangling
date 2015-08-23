#!/usr/bin/env python
"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format
"""

import xlrd
import pprint
import os
datafile = "2013_ERCOT_Hourly_Load_Data.xls"

def parse_file(datafile):
   workbook = xlrd.open_workbook(datafile)
   sheet = workbook.sheet_by_index(0)

   data = {
            'maxtime': (0, 0, 0, 0, 0, 0),
            'maxvalue': -1,
            'mintime': (0, 0, 0, 0, 0, 0),
            'minvalue': 9999999,
            'avgcoast': 0
    }

   cv = sheet.col_values(1, start_rowx = 1, end_rowx=None)

   data['maxvalue'] = max(cv)
   data['minvalue'] = min(cv)

   maxpos = cv.index(data['maxvalue']) + 1
   minpos = cv.index(data['minvalue']) + 1

   maxtime = sheet.cell_value(maxpos, 0)
   data['maxtime'] = xlrd.xldate_as_tuple(maxtime, 0)
   mintime = sheet.cell_value(minpos, 0)
   data['mintime'] = xlrd.xldate_as_tuple(mintime, 0)

   data['avgcoast'] = sum(cv) / float(len(cv))

   return data


def test():
    data = parse_file(datafile)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)
    pprint.pprint(data)
    print "Success!"


test()
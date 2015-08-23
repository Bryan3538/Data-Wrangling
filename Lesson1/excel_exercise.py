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
datafile = "2013_ERCOT_Hourly_Load_Data.xls"

def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    coast = 1
    date = 0
    sum = 0
    val = 0

    data = {
            'maxtime': (0, 0, 0, 0, 0, 0),
            'maxvalue': -1,
            'mintime': (0, 0, 0, 0, 0, 0),
            'minvalue': 9999999,
            'avgcoast': 0
    }
    for row in range(1, sheet.nrows):
        val = sheet.cell_value(row, coast)
        sum += val

        #find min
        if val < data['minvalue']:
            data['minvalue'] = val
            data['mintime'] = xlrd.xldate_as_tuple(sheet.cell_value(row, date), 0)
    
        #find max
        if val > data['maxvalue']:
            data['maxvalue'] = val
            data['maxtime'] = xlrd.xldate_as_tuple(sheet.cell_value(row, date), 0)

    data['avgcoast'] = sum / (sheet.nrows - 1)

    return data


def test():
    data = parse_file(datafile)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)
    print "Success!"


test()
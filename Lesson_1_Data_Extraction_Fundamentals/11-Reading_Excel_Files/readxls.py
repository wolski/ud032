#!/usr/bin/env python
"""
Your task is as follows:
- read the provided Excel file
- find and return the min and max values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format
"""

import xlrd
from zipfile import ZipFile
datafile = "2013_ERCOT_Hourly_Load_Data"


def open_zip(datafile):
    fcuk = '{0}.zip'.format(datafile)
    with ZipFile(fcuk, 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):

    data = {
            'maxtime': (0, 0, 0, 0, 0, 0),
            'maxvalue': 0,
            'mintime': (0, 0, 0, 0, 0, 0),
            'minvalue': 0,
            'avgcoast': 0
    }

    data_file = '{0}.xls'.format(datafile)
    workbook = xlrd.open_workbook(data_file)
    sheet = workbook.sheet_by_index(0)

    print(sheet.row_values(0))
    coast = sheet.col_values(1, start_rowx=1, end_rowx=sheet.nrows)
    coastmaxidx = coast.index(max(coast))
    coastminidx = coast.index(min(coast))
    data['maxvalue'] = max(coast)
    data['minvalue'] = min(coast)
    data['avgcoast'] = sum(coast)/len(coast)
    exceltime_max = sheet.cell_value(coastmaxidx + 1, 0)
    data['maxtime'] = xlrd.xldate_as_tuple(exceltime_max, 0)
    exceltime_min = sheet.cell_value(coastminidx + 1, 0)
    data['mintime'] = xlrd.xldate_as_tuple(exceltime_min, 0)


    return data


def test():
    open_zip(datafile)
    data = parse_file(datafile)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)


test()
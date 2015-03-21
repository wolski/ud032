# -*- coding: utf-8 -*-
# Find the time and value of max load for each of the regions
# COAST, EAST, FAR_WEST, NORTH, NORTH_C, SOUTHERN, SOUTH_C, WEST
# and write the result out in a csv file, using pipe character | as the delimiter.
# An example output can be seen in the "example.csv" file.
import xlrd
import os
import csv
from zipfile import ZipFile

datafile = "2013_ERCOT_Hourly_Load_Data.xls"

outfile = "2013_Max_Loads.csv"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def getMax(timecol, region):
    data = {}
    coastmaxidx = region.index(max(region))
    data['maxvalue'] = max(region)
    exceltime_max = timecol[coastmaxidx]
    data['maxtime'] = list(xlrd.xldate_as_tuple(exceltime_max, 0))[:4]
    return data

def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    time = sheet.col_values(0, start_rowx=1, end_rowx=sheet.nrows)

    res = []
    regions = ['COAST', 'EAST', 'FAR_WEST', 'NORTH', 'NORTH_C', 'SOUTHERN', 'SOUTH_C', 'WEST']
    for i in range(1, len(sheet.row_values(0))):
        print(i)

        region_name = sheet.col_values(i, 0, 1)
        region_name = region_name[0].encode('UTF8')
        if region_name in regions:
            region_data = sheet.col_values(i, start_rowx=1, end_rowx=sheet.nrows)
            data = getMax(time, region_data)
            rest = []
            rest.append( region_name)
            rest += data['maxtime']
            rest.append(data['maxvalue'])
            res.append(rest)
    return res


def save_file(data, filename):
    header = "Station|Year|Month|Day|Hour|Max Load\n"
    with open(filename, 'wb') as csvfile:
        csvfile.write(header)
        spamwriter = csv.writer(csvfile, delimiter='|')
        for row in data:
            spamwriter.writerow(row)

    
def test():
    open_zip(datafile)
    data = parse_file(datafile)
    save_file(data, outfile)

    number_of_rows = 0
    stations = []

    ans = {'FAR_WEST': {'Max Load': '2281.2722140000024',
                        'Year': '2013',
                        'Month': '6',
                        'Day': '26',
                        'Hour': '17'}}
    correct_stations = ['COAST', 'EAST', 'FAR_WEST', 'NORTH',
                        'NORTH_C', 'SOUTHERN', 'SOUTH_C', 'WEST']
    fields = ['Year', 'Month', 'Day', 'Hour', 'Max Load']

    with open(outfile) as of:
        csvfile = csv.DictReader(of, delimiter="|")
        for line in csvfile:
            station = line['Station']
            if station == 'FAR_WEST':
                for field in fields:
                    # Check if 'Max Load' is within .1 of answer
                    if field == 'Max Load':
                        max_answer = round(float(ans[station][field]), 1)
                        max_line = round(float(line[field]), 1)
                        assert max_answer == max_line

                    # Otherwise check for equality
                    else:
                        assert ans[station][field] == line[field]

            number_of_rows += 1
            stations.append(station)

        # Output should be 8 lines not including header
        assert number_of_rows == 8

        # Check Station Names
        assert set(stations) == set(correct_stations)


if __name__ == "__main__":
    test()
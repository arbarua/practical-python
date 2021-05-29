# fileparse.py
#
# Exercise 3.3
# fileparse.py
import csv

def parse_csv(filename, select=None, types=None, has_headers = True):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)
        
        if has_headers:
        # Read the file headers
             headers = next(rows)

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
             if select:
                 indices = [headers.index(colname) for colname in select]
                 headers = select
             else:
                 indices = []

        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            if types:
                if has_headers:
                    row = [func(val) for func, val in zip(types, row) ]
                    record = dict(zip(headers, row))
                    records.append(record)
                else:
                    row = [func(val) for func, val in zip(types, row)]
                    records.append(tuple(row))

    return records

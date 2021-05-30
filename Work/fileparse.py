# fileparse.py
#
# Exercise 3.3
# fileparse.py
import csv

def parse_csv(filename, select=None, types=None, has_headers = True, delimiter = None, silence_errors = False):
    '''
    Parse a CSV file into a list of records
    '''
    if select and has_headers == False:
        raise RuntimeError('select argument requires column headers')
    with open(filename) as f:
        if delimiter:
            rows = csv.reader(f, delimiter = delimiter)
        else:
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
        for row_no, row in enumerate(rows, start = 1):
            if not row:    # Skip rows with no data
                continue
            if types:
                if has_headers:
                    try:
                        row = [func(val) for func, val in zip(types, row) ]
                    except ValueError as e:
                        if not silence_errors:
                            print(f"Row {row_no}: Couldn't convert {row}")
                            print(f"Row {row_no}: Reason {e}")
                        continue
                    record = dict(zip(headers, row))
                    records.append(record)
                else:
                    row = [func(val) for func, val in zip(types, row)]
                    records.append(tuple(row))

    return records

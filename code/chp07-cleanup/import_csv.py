import pprint
from csv import DictReader

data_rdr = DictReader(open('../../data/unicef/mn.csv', 'rb'))
header_rdr = DictReader(open('../../data/unicef/mn_headers.csv', 'rb'))

data_rows = [d for d in data_rdr]
header_rows = [h for h in header_rdr]
new_rows = []

for data_dict in data_rows:
    new_row = {}
    for d_key, d_value in data_dict.items():
        for header_dict in header_rows:
            if d_key in header_dict.values():
                new_row[header_dict.get('Label')] = d_value
    new_rows.append(new_row)

pprint.pprint(new_rows[0])

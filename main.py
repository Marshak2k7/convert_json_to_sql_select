import json
import argparse

request = ''
parser = argparse.ArgumentParser()
parser.add_argument('-f', default=None, help='Path to file or filename')
parser.add_argument('-s', default=None, help='Json input')
all_parsers = parser.parse_args()


def json_parse():
    if all_parsers.f:
        filename_r = all_parsers.f
        f = open(filename_r, 'r', encoding='utf-8')
    elif all_parsers.s:
        f = open('queries.json', 'w')
        f.write(all_parsers.s)
        f = open('queries.json', 'r')
    original_file = json.load(f)
    queries = original_file['queries']
    query_type = str(original_file['query_type']).upper()
    for query in queries:
        global request
        request += (query_type + ' ' + '"' + query.get('field') + '"' + ' FROM ' + '"' + query.get(
            'schema') + '"' + '.' + '"' + query.get('table') + '"' + ';' + '\n')
    write_in_file()


def write_in_file():
    with open('sql_request.txt', 'w') as file:
        file.write(request)


json_parse()

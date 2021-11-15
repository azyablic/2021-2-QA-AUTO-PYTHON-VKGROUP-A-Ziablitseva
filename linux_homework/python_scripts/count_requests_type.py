import argparse
import json

parser = argparse.ArgumentParser()

parser.add_argument('--json', action='store_true')

args = parser.parse_args()

requests = open('../access.log', 'r')
requests = [request.split() for request in requests]

dict = {}
for request in requests:
    request_type = request[5].replace('"', '')
    if request_type in dict:
        dict[request_type] += 1
    else:
        dict[request_type] = 1

file = f'count_requests_type.{"json" if args.json else "txt"}'
with open(file, 'w') as f:
    if args.json:
        json.dump(dict, f)
    else:
        f.write('Общее количество запросов по типу\n')
        for request_type, count in dict.items():
            f.write(f'{request_type} - {count}')
            f.write('\n')

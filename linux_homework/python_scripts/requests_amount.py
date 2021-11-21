import argparse
import json

parser = argparse.ArgumentParser()

parser.add_argument('--json', action='store_true')

args = parser.parse_args()

requests = open('../access.log', 'r')
requests = [request.split() for request in requests]

requests_amount = len(requests)

file = f'requests_amount.{"json" if args.json else "txt"}'
with open(file, 'w') as f:
    if args.json:
        json.dump({'Requests amount': requests_amount}, f)
    else:
        f.write('Общее количество запросов\n')
        f.write(str(requests_amount))

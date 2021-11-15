import argparse
import json

parser = argparse.ArgumentParser()

parser.add_argument('--json', action='store_true')

args = parser.parse_args()

requests = open('../access.log', 'r')
requests = [request.split() for request in requests]

dict = {}
for request in requests:
    url = request[6]
    if url in dict:
        dict[url] += 1
    else:
        dict[url] = 1
sorted_tuples = sorted(dict.items(), key=lambda item: item[1], reverse=True)
sorted_dict = {k: v for k, v in sorted_tuples[:10]}

file = f'count_top_requests.{"json" if args.json else "txt"}'
with open(file, 'w') as f:
    if args.json:
        json.dump(sorted_dict, f)
    else:
        f.write('Топ 10 самых частых запросов\n')
        for ip, count in sorted_dict.items():
            f.write(f'{ip} - {count}')
            f.write('\n')
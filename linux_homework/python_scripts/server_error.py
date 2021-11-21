import argparse
import json

parser = argparse.ArgumentParser()

parser.add_argument('--json', action='store_true')

args = parser.parse_args()

requests = open('../access.log', 'r')
requests = [request.split() for request in requests]

dict = {}
for request in requests:
    ip = request[0]
    status_code = request[8]
    if status_code.startswith('5'):
        if ip in dict:
            dict[ip] += 1
        else:
            dict[ip] = 1
sorted_tuples = sorted(dict.items(), key=lambda item: item[1], reverse=True)[:5]

file = f'server_error.{"json" if args.json else "txt"}'
with open(file, 'w') as f:
    if args.json:
        result = []
        for i in sorted_tuples:
            result.append(
                {
                    'ip': i[0],
                    'count': i[1]
                }
            )
        json.dump({'requests': result}, f)
    else:
        f.write('Топ 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой\n')
        for ip, count in sorted_tuples:
            f.write(f'{ip} - {count}')
            f.write('\n')
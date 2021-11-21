import argparse
import json

parser = argparse.ArgumentParser()

parser.add_argument('--json', action='store_true')

args = parser.parse_args()

requests = open('../access.log', 'r')
requests = [request.split() for request in requests]

data = []
for request in requests:
    status_code = request[8]
    url = request[6]
    size = request[9]
    ip = request[0]
    if status_code.startswith('4'):
        e = (url, status_code, int(size), ip)
        data.append(e)
sorted_data = sorted(data, key=lambda x: x[2], reverse=True)[:5]

file = f'client_error.{"json" if args.json else "txt"}'
with open(file, 'w') as f:
    if args.json:
        result = []
        for res in sorted_data:
            result.append(
                {
                    'url': res[0],
                    'status_code': res[1],
                    'size': res[2],
                    'ip': res[3]
                }
            )
        json.dump({'requests': result}, f)
    else:
        f.write('Топ 5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой\n')
        for i in sorted_data:
            f.write(f'url: {i[0]} status_code: {i[1]} size: {i[2]} ip: {i[3]} ')
            f.write('\n')
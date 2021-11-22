import os


def repo_root():
    return os.path.abspath(os.path.join(__file__, os.pardir))


requests = open(os.path.join(repo_root(), 'access.log'), 'r')
data = [request.split() for request in requests]


def get_requests_amount():
    return len(data)


def get_count_by_type():
    dict = {}
    for request in data:
        request_type = request[5].replace('"', '')
        if request_type in dict:
            dict[request_type] += 1
        else:
            dict[request_type] = 1
    return dict


def get_top_10_requests():
    dict = {}
    for request in data:
        url = request[6]
        if url in dict:
            dict[url] += 1
        else:
            dict[url] = 1
    sorted_tuples = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    sorted_dict = {k: v for k, v in sorted_tuples[:10]}
    return sorted_dict


def get_top_5_server_error():
    dict = {}
    for request in data:
        ip = request[0]
        status_code = request[8]
        if status_code.startswith('5'):
            if ip in dict:
                dict[ip] += 1
            else:
                dict[ip] = 1
    sorted_tuples = sorted(dict.items(), key=lambda item: item[1], reverse=True)[:5]
    return sorted_tuples


def get_top_5_client_error():
    data = []
    for request in data:
        status_code = request[8]
        url = request[6]
        size = request[9]
        ip = request[0]
        if status_code.startswith('4'):
            e = (url, status_code, size, ip)
            data.append(e)
    sorted_data = sorted(data, key=lambda x: x[2], reverse=True)[:5]
    return sorted_data

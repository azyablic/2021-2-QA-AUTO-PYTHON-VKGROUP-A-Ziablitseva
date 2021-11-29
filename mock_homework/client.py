import json
import socket
import logging

logger = logging.getLogger('test')


class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = int(port)

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.settimeout(0.1)
        self.client.connect((self.host, self.port))

    @staticmethod
    def log_pre(request):
        logger.info(f'\nREQUEST:\n{request}')

    @staticmethod
    def log_post(response):
        logger.info(f'\nRESPONSE:\n{response[0]}\n'
                    f'{response[1]}\n'
                    f'{response[2]}\n'
                    f'{response[3]}\n'
                    f'{response[4]}\n'
                    f'{response[5]}\n'
                    f'{response[6]}'
                    )

    def request(self, method,  location, data=None, content_type='application/json'):
        if data is None:
            request = f'{method} {location} HTTP/1.1\r\n' \
                      f'Host: {self.host}:{self.port}\r\n\r\n'

        else:
            if content_type == 'application/json':
                data = json.dumps(data)
            request = f'{method} {location} HTTP/1.1\r\n' \
                      f'Host: {self.host}\r\n\r\n' \
                      f'Content-type:{content_type}\r\n' \
                      f'Content-Length: {len(data)}\r\n' \
                      f'{data}\r\n'

        self.log_pre(request)

        self.client.send(request.encode())
        response = self.get_data(self.client)
        self.log_post(response)
        return response

    def post(self, data=None, location='/', content_type='application/json'):
        return self.request('POST', location, data, content_type)

    def get(self, location='/'):
        return self.request(method='GET', location=location)

    def put(self, data=None, location='/', content_type='application/json'):
        return self.request('PUT', location, data, content_type)

    def delete(self, location='/'):
        return self.request(method='DELETE', location=location)

    @staticmethod
    def get_data(client):
        total_data = []

        while True:
            data = client.recv(4096)
            if data:
                total_data.append(data.decode())
            else:
                client.close()
                break

        data = ''.join(total_data).splitlines()
        return (data)

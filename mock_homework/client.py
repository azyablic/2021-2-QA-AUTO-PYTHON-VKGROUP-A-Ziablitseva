import json
import socket
import logging
import mock_homework.settings as settings

logger = logging.getLogger('test')


class Client:
    def __init__(self, host=settings.MOCK_HOST, port=settings.MOCK_PORT):
        self.host = host
        self.port = port
        self.client = None

    def connect(self):
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

    def _request(self, method, location, data=None):
        self.connect()
        if method == 'GET' or method == 'DELETE':
            request = f'{method} {location} HTTP/1.1\r\nHost:{self.host}\r\n\r\n'
        elif method == 'PUT' or method == 'POST':
            data = json.dumps(data)
            request = f'{method} {location} HTTP/1.1\r\n' \
                      f'Host:{self.host}\r\n' \
                      f'Content-Type: application/json\r\n' \
                      f'Content-Length: {len(data)}\r\n' \
                      f'\r\n{data}'

        self.log_pre(request)
        self.client.send(request.encode())
        response = self.get_data()
        self.log_post(response)
        return response

    def post(self, data=None, location='/'):
        return self._request(method='POST', location=location, data=data)

    def get(self, location='/'):
        return self._request(method='GET', location=location)

    def put(self, data=None, location='/'):
        return self._request(method='PUT', location=location, data=data)

    def delete(self, location='/'):
        return self._request(method='DELETE', location=location)

    def get_data(self):
        total_data = []

        while True:
            data = self.client.recv(4096)
            if data:
                total_data.append(data.decode())
            else:
                self.client.close()
                break

        data = ''.join(total_data).splitlines()
        return (data)

import logging
import os
import shutil
import time

import pytest
import requests
from requests.exceptions import ConnectionError

import mock_homework.settings as settings
from mock_homework.mock import flask_mock

repo_root = os.path.abspath(os.path.join(__file__, os.pardir))


def wait_ready(host, port):
    started = False
    st = time.time()
    while time.time() - st <= 5:
        try:
            requests.get(f'http://{host}:{port}')
            started = True
            break
        except ConnectionError:
            pass

    if not started:
        raise RuntimeError(f'{host}:{port} did not started in 5s!')


def start_mock():
    flask_mock.run_mock()
    wait_ready(settings.MOCK_HOST, settings.MOCK_PORT)


def pytest_configure(config):
    if not hasattr(config, 'workerinput'):
        start_mock()


def stop_mock():
    requests.get(f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}/shutdown')


def pytest_unconfigure(config):
    if not hasattr(config, 'workerinput'):
        stop_mock()

@pytest.fixture(scope='function')
def test_dir(request):
    test_name = request._pyfuncitem.nodeid.replace('/', '_').replace(':', '_')
    test_dir = os.path.join(os.path.abspath('tests_logs'), test_name)
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)
    os.makedirs(test_dir)
    return test_dir


@pytest.fixture(scope='function', autouse=True)
def logger(test_dir):
    log_formatter = logging.Formatter('%(asctime)s - %(filename)-15s - %(levelname)-6s - %(message)s')
    log_file = os.path.join(test_dir, 'test.log')

    log_level = logging.DEBUG

    file_handler = logging.FileHandler(log_file, 'w')
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(log_level)

    log = logging.getLogger('test')
    log.propagate = False
    log.setLevel(log_level)
    log.handlers.clear()
    log.addHandler(file_handler)

    yield log

    for handler in log.handlers:
        handler.close()

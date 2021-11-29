import json
import pytest
from faker import Faker

from mock_homework import settings
from mock_homework.client import Client
from mock_homework.mock.flask_mock import SURNAME_DATA


fake = Faker()
url = f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}'

class TestMock:
    @pytest.mark.Mock
    def test_get(self):
        name, surname = fake.first_name(), fake.last_name()
        SURNAME_DATA[name] = surname

        client = Client(settings.MOCK_HOST, settings.MOCK_PORT)
        result = client.get(f'/get_surname/{name}')
        assert json.loads(result[-1])['surname'] == surname

    @pytest.mark.Mock
    def test_post(self):
        name = fake.first_name()
        surname = fake.last_name()

        client = Client(settings.MOCK_HOST, settings.MOCK_PORT)
        result = client.post(data={'name': name ,'surname': surname}, location='/add_user')
        assert json.loads(result[-1], strict=False)['surname'] == surname

        client = Client(settings.MOCK_HOST, settings.MOCK_PORT)
        result = client.get(f'/get_surname/{name}')
        assert json.loads(result[-1])['surname'] == surname

    @pytest.mark.Mock
    def test_put(self):
        name = fake.first_name()
        surname = fake.last_name()
        new_surname = fake.last_name()
        SURNAME_DATA[name] = surname

        client = Client(settings.MOCK_HOST, settings.MOCK_PORT)
        result = client.get(f'/get_surname/{name}')
        assert json.loads(result[-1])['surname'] == surname

        client = Client(settings.MOCK_HOST, settings.MOCK_PORT)
        result = client.put(data={'surname': new_surname}, location=f'/put_surname/{name}')
        assert json.loads(result[-1])['surname'] == new_surname

    @pytest.mark.Mock
    def test_delete(self):
        name = fake.first_name()
        surname = fake.last_name()
        SURNAME_DATA[name] = surname
        client = Client(settings.MOCK_HOST, settings.MOCK_PORT)
        data = client.delete(f'/delete_surname/{name}')
        assert json.loads(data[-1])["status"] == "Ok"

        client = Client(settings.MOCK_HOST, settings.MOCK_PORT)
        result = client.get(f'/get_surname/{name}')
        assert json.loads(result[-1]) == f'User {name} not found'

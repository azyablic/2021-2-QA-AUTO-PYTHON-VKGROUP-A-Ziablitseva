import json
import pytest
from faker import Faker

from mock_homework import settings
from mock_homework.client import Client
from mock_homework.mock.flask_mock import SURNAME_DATA

fake = Faker()
s_client = Client()
url = f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}'


class TestMock:
    @pytest.mark.Mock
    def test_get(self):
        name, surname = fake.first_name(), fake.last_name()
        SURNAME_DATA[name] = surname

        result = s_client.get(f'/get_surname/{name}')
        assert json.loads(result[-1])['surname'] == surname

    @pytest.mark.Mock
    def test_post(self):
        name = fake.first_name()
        surname = fake.last_name()

        s_client.post(data={'name': name, 'surname': surname}, location='/add_user')
        result = s_client.get(f'/get_surname/{name}')
        assert json.loads(result[-1])['surname'] == surname

    @pytest.mark.Mock
    def test_put(self):
        name = fake.first_name()
        surname = fake.last_name()
        new_surname = fake.last_name()
        SURNAME_DATA[name] = surname

        result = s_client.get(f'/get_surname/{name}')
        assert json.loads(result[-1])['surname'] == surname
        s_client.put(data={'surname': new_surname}, location=f'/put_surname/{name}')
        result = s_client.get(f'/get_surname/{name}')
        assert json.loads(result[-1])['surname'] == new_surname

    @pytest.mark.Mock
    def test_delete(self):
        name = fake.first_name()
        surname = fake.last_name()
        SURNAME_DATA[name] = surname

        data = s_client.delete(f'/delete_surname/{name}')
        assert json.loads(data[-1])["status"] == "Ok"
        result = s_client.get(f'/get_surname/{name}')
        assert json.loads(result[-1]) == f'User {name} not found'

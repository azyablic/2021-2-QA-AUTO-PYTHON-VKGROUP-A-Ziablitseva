import os
import pytest


class ApiBase:
    authorize = True
    email = "zyablitseva.an@yandex.ru"
    password = "snzGePWva7b5hTE"
    path_to_image = os.path.abspath('../test_api/image.jpg')

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, api_client):
        self.api_client = api_client
        if self.authorize:
            self.api_client.post_login(self.email, self.password)

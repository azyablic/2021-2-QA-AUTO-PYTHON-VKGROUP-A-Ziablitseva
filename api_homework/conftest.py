import pytest
from .api.client import ApiClient


@pytest.fixture(scope='session')
def api_client():
    return ApiClient("https://target.my.com/")

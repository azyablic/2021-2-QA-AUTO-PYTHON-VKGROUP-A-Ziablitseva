import pytest
from api.client import ApiClient
import api.credits as credits


@pytest.fixture(scope='session')
def api_client():
    return ApiClient(credits.base_url)

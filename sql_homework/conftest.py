import pytest

from mysql.client import MysqlClient


def pytest_configure(config):
    if not hasattr(config, 'workerinput'):
        mysql_client = MysqlClient(user='root', password='pass', db_name='TEST_SQL')
        mysql_client.recreate_db()

        mysql_client.connect()
        mysql_client.create_count_by_type()
        mysql_client.create_requests_amount()
        mysql_client.create_top_5_client_error()
        mysql_client.create_top_5_server_error()
        mysql_client.create_top_10_requests()

        mysql_client.connection.close()


@pytest.fixture(scope='session')
def mysql_client():
    mysql_client = MysqlClient(user='root', password='pass', db_name='TEST_SQL')
    mysql_client.connect()
    yield mysql_client
    mysql_client.connection.close()

import pytest

from mysql.mysql_builder import MysqlBuilder
from mysql.client import MysqlClient
from models.model import RequestsAmount, Top10Requests, Top5ClientError, Top5ServerError, CountByType

from log_parser import LogParser


class MysqlBase:

    def prepare(self):
        pass

    def get_rows(self, query_type):
        return self.mysql.session.query(query_type).all()

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client, config):
        self.mysql: MysqlClient = mysql_client
        self.mysql_builder: MysqlBuilder = MysqlBuilder(mysql_client, config)
        self.log_parser = LogParser(config['file_name'])

        self.prepare()


class TestRequestsAmount(MysqlBase):

    def prepare(self):
        self.mysql_builder.create_requests_amount()

    def test_requests_amount(self):
        result = self.get_rows(RequestsAmount)
        assert len(result) == 1
        assert result[0].count == self.log_parser.get_requests_amount()


class TestRequestsAmountByType(MysqlBase):

    def prepare(self):
        self.mysql_builder.create_count_by_type()

    def test_count_by_type(self):
        result = self.get_rows(CountByType)
        assert len(result) == len(self.log_parser.get_count_by_type())


class TestTop10Requests(MysqlBase):

    def prepare(self):
        self.mysql_builder.create_top_10_requests()

    def test_top_10_requests(self):
        result = self.get_rows(Top10Requests)
        assert len(result) == len(self.log_parser.get_top_10_requests())


class TestTop5ServerError(MysqlBase):

    def prepare(self):
        self.mysql_builder.create_top_5_server_error()

    def test_top_5_server_error(self):
        result = self.get_rows(Top5ServerError)
        assert len(result) == len(self.log_parser.get_top_5_server_error())


class TestTop5ClientError(MysqlBase):

    def prepare(self):
        self.mysql_builder.create_top_5_client_error()

    def test_top_5_client_error(self):
        result = self.get_rows(Top5ClientError)
        assert len(result) == len(self.log_parser.get_top_5_client_error())

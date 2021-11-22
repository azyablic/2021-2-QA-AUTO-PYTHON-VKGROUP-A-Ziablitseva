from models.model import RequestsAmount, CountByType, Top5ServerError, Top5ClientError, Top10Requests
from log_parser import get_top_5_server_error, get_requests_amount, get_count_by_type, get_top_10_requests, \
    get_top_5_client_error


class MysqlBuilder:

    def __init__(self, client):
        self.client = client

    def create_requests_amount(self):
        count = get_requests_amount()
        request_amount = RequestsAmount(
            count=count
        )
        self.client.session.add(request_amount)
        self.client.session.commit()
        return request_amount

    def create_count_by_type(self):
        parsed_data = get_count_by_type()
        count_by_type = []
        for type, count in parsed_data.items():
            row = CountByType(
                type=type,
                count=count
            )
            count_by_type.append(row)
        self.client.session.bulk_save_objects(count_by_type)
        self.client.session.commit()
        return count_by_type

    def create_top_5_server_error(self):
        parsed_data = get_top_5_server_error()
        top_5_server_error = []
        for ip, count in parsed_data:
            row = Top5ServerError(
                ip=ip,
                count=count
            )
            top_5_server_error.append(row)
        self.client.session.bulk_save_objects(top_5_server_error)
        self.client.session.commit()
        return top_5_server_error

    def create_top_5_client_error(self):
        parsed_data = get_top_5_client_error()
        top_5_client_error = []
        for url, status, size, ip in parsed_data:
            row = Top5ClientError(
                url=url,
                status=status,
                size=size,
                ip=ip
            )
            top_5_client_error.append(row)
        self.client.session.bulk_save_objects(top_5_client_error)
        self.client.session.commit()
        return top_5_client_error

    def create_top_10_requests(self):
        parsed_data = get_top_10_requests()
        top_10_requests = []
        for url, count in parsed_data.items():
            row = Top10Requests(
                url=url,
                count=count
            )
            top_10_requests.append(row)
        self.client.session.add_all(top_10_requests)
        self.client.session.commit()
        return top_10_requests

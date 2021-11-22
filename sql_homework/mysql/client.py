import sqlalchemy
from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker

from models.model import Base


class MysqlClient:

    def __init__(self, user, password, db_name):
        self.user = user
        self.password = password
        self.db_name = db_name

        self.host = '127.0.0.1'
        self.port = 3306

        self.engine = None
        self.connection = None
        self.session = None

    def connect(self, db_created=True):
        db = self.db_name if db_created else ''

        self.engine = sqlalchemy.create_engine(
            f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{db}',
            encoding='utf8'
        )
        self.connection = self.engine.connect()

        self.session = sessionmaker(
            bind=self.connection.engine,
            autocommit=False,
            expire_on_commit=False
        )()

    def recreate_db(self):
        self.connect(db_created=False)

        self.execute_query(f'DROP database if exists {self.db_name}', fetch=False)
        self.execute_query(f'CREATE database {self.db_name}', fetch=False)

        self.connection.close()

    def execute_query(self, query, fetch=True):
        res = self.connection.execute(query)
        if fetch:
            return res.fetchall()

    def create_requests_amount(self):
        if not inspect(self.engine).has_table('requests_amount'):
            Base.metadata.tables['requests_amount'].create(self.engine)

    def create_top_10_requests(self):
        if not inspect(self.engine).has_table('top_10_requests'):
            Base.metadata.tables['top_10_requests'].create(self.engine)

    def create_count_by_type(self):
        if not inspect(self.engine).has_table('count_by_type'):
            Base.metadata.tables['count_by_type'].create(self.engine)

    def create_top_5_client_error(self):
        if not inspect(self.engine).has_table('top_5_client_error'):
            Base.metadata.tables['top_5_client_error'].create(self.engine)

    def create_top_5_server_error(self):
        if not inspect(self.engine).has_table('top_5_server_error'):
            Base.metadata.tables['top_5_server_error'].create(self.engine)

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class RequestsAmount(Base):
    __tablename__ = 'requests_amount'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __rep__(self):
        return f"<Requests Amount(" \
               f"id='{self.id}'," \
               f"count='{self.count}'" \
               f")>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    count = Column(Integer, nullable=False, default=0)


class Top10Requests(Base):
    __tablename__ = 'top_10_requests'
    ____table_args__ = {'mysql_charset': 'utf8'}

    def __rep__(self):
        return f"<Top 10 Requests(" \
               f"id='{self.id}'," \
               f"url='{self.url}'," \
               f"count='{self.count}" \
               f")>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(500), nullable=False)
    count = Column(Integer, nullable=False, default=0)


class CountByType(Base):
    __tablename__ = 'count_by_type'
    ____table_args__ = {'mysql_charset': 'utf8'}

    def __rep__(self):
        return f"<Count By Type(" \
               f"id='{self.id}'," \
               f"type='{self.type}'," \
               f"count='{self.count}" \
               f")>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(500), nullable=False)
    count = Column(Integer, nullable=False, default=0)


class Top5ClientError(Base):
    __tablename__ = 'top_5_client_error'
    ____table_args__ = {'mysql_charset': 'utf8'}

    def __rep__(self):
        return f"<Top 5 Client Error(" \
               f"id='{self.id}'," \
               f"url='{self.url}'," \
               f"status='{self.status}" \
               f"size='{self.size}" \
               f"ip='{self.ip}" \
               f")>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(500), nullable=False)
    status = Column(Integer, nullable=False)
    size = Column(String(4), nullable=False)
    ip = Column(String(15), nullable=False)


class Top5ServerError(Base):
    __tablename__ = 'top_5_server_error'
    ____table_args__ = {'mysql_charset': 'utf8'}

    def __rep__(self):
        return f"<Top 5 Server Error(" \
               f"id='{self.id}'," \
               f"ip='{self.ip}" \
               f"count='{self.count}" \
               f")>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(15), nullable=False)
    count = Column(Integer, nullable=False, default=0)

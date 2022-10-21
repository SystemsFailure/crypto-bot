from sqlalchemy import Table, Index, Integer, String, Column, Text, DateTime, Boolean, PrimaryKeyConstraint, \
    UniqueConstraint, ForeignKeyConstraint, MetaData
from datetime import datetime
from DataBase.connect_to_db import Connect

conn = Connect()
engine, Base = conn.get_settings()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(200), nullable=False)
    token = Column(String(100), nullable=True)
    refresh_token = Column(String(199), nullable=True)
    data_create = Column(DateTime(), default=datetime.now())
    data_update = Column(DateTime(), default=datetime.now())

    __table_args__ = (
        # PrimaryKeyConstraint('id', name='user_id'),
        UniqueConstraint('email'),
    )


Base.metadata.create_all(engine)



from sqlalchemy import create_engine, MetaData, Table, Integer, String, Column, DateTime, ForeignKey, Numeric, SmallInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, Session
from datetime import datetime
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine


class Connect:
    name = 'botDB_w'
    owner = 'postgres'
    password = 31415
    engine = create_engine(f"postgresql+psycopg2://{owner}:{password}@localhost/{name}")
    Base = declarative_base()
    Session = sessionmaker(bind=engine)

    def get_settings(self):
        return self.engine, self.Base

    def session_(self):
        return self.Session

    # async_engine = create_async_engine(f"postgresql+asyncpg://{owner}:{password}@localhost/{name}")
    # async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)




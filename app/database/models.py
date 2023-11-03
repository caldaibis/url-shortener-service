import sqlalchemy as sa
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Url(Base):
    __tablename__ = "urls"
    id = Column(Integer, primary_key=True, index=True)
    original = Column(String, nullable=False)
    hashcode = Column(String, nullable=False)
    hits = Column(Integer, nullable=False, default=0)
    created_on = Column(DateTime, nullable=False, server_default=sa.func.now())

    def __init__(self, original, hashcode, hits=0):
        self.original = original
        self.hashcode = hashcode
        self.hits = hits
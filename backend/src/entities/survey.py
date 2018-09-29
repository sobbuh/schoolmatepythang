# coding=utf-8

from sqlalchemy import Column, String

from .entity import Entity, Base


class Survey(Entity, Base):
    __tablename__ = 'surveys'

    title = Column(String)
    description = Column(String)

    def __init__(self, title, description, created_by):
        Entity.__init__(self, created_by)
        self.title = title
        self.description = description

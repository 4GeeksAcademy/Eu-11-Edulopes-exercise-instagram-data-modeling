import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(length=12), nullable=False)
    account = Column(Integer, ForeignKey('account.id'))


class Account(Base):
    __tablename__ = 'account'
    user_id = Column(Integer, ForeignKey('user.id'))
    id = Column(Integer, primary_key=True)
    user_username = Column(String(250), nullable=False)
    user_password = Column(String(length=12), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Comments(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('account.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    comment_text= Column(String(250), nullable=False)


class Followers(Base):
    __tablename__= 'followers'
    account_id = Column(Integer, ForeignKey('account.id'))
    id = Column (Integer, primary_key=True)
    followers_id = Column(Integer, ForeignKey('account.id'))

class Post(Base):
    __tablename__= 'post'
    account_id = Column(Integer, ForeignKey('account'))
    id = Column(Integer, primary_key=True)
    post_subtitle = Column(Integer)
    post_comments = Column(String(250))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e

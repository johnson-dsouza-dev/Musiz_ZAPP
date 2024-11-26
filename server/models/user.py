from sqlalchemy import TEXT, VARCHAR, Column, LargeBinary
from models.base import Base

# ORM model for user table
class User(Base):
    __tablename__ = 'users'  # Table name in the database

    id = Column(TEXT, primary_key=True)  # User ID as primary key
    name = Column(VARCHAR(100))  # Name field with max length 100 characters
    email = Column(VARCHAR(100))  # Email field with max length 100 characters
    password = Column(LargeBinary)  # Password field stored as binary data for security

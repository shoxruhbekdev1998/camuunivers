import datetime

from sqlalchemy import Column, Integer, String, Boolean,Float,Text,ForeignKey,Date,DateTime,func 

from sqlalchemy.orm import relationship

from db import Base


class Users(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True,autoincrement=True)
    roll = Column(String(50), nullable=True)
    username = Column(String(50),nullable=True)
    name = Column(String(50), nullable=True)
    last_name = Column(String(50), nullable=True)
    password = Column(String(400),nullable=True)
    phone_number = Column(String(40), nullable=True)
    region = Column(String(30), nullable=True)
    date = Column(Date(),nullable = True,default=func.now())
    status = Column(Boolean, nullable = True ,default=True)
    token = Column(String(400),default = '',nullable=True)



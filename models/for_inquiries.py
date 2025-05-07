import datetime

from sqlalchemy import Column, Integer, String, Boolean,Float,Text,ForeignKey,Date,DateTime,func 

from sqlalchemy.orm import relationship

from db import Base


class Inquiries(Base):
    __tablename__ = "Inquiries"
    id = Column(Integer, primary_key=True,autoincrement=True)
    
    student_name = Column(String(50), nullable=True)
    student_surname = Column(String(50), nullable=True)
    student_number = Column(String(50), nullable=True)
    student_direct = Column(String(50), default=True)  # yo'nalishlarni tanlay oladi
    student_request = Column(String(300), nullable=True) #savollar bera oladi
    student_confirm = Column(String(50), default=True)

    page = Column(String(50), nullable=True)
    
    date = Column(Date(),nullable = True,default=func.now())
    status = Column(Boolean, nullable = True ,default=True)

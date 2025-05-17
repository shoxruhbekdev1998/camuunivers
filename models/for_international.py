import datetime

from sqlalchemy import Column, Integer, String, Boolean,Float,Text,ForeignKey,Date,DateTime,func 

from sqlalchemy.orm import relationship

from db import Base


class Internationals(Base):
    __tablename__ = "Internationals"
    id = Column(Integer, primary_key=True,autoincrement=True)
    
    student_name = Column(String(500), nullable=True)
    student_surname = Column(String(500), nullable=True)
    student_middle_name = Column(String(500), nullable=True)
    student_coutry = Column(String(500), nullable=True)
    student_email = Column(String(500), nullable=True)
    student_direct = Column(String(500), nullable=True)
    student_request = Column(Text, nullable=True)
    page = Column(String(500), nullable=True)
    
    student_confirm = Column(String(50), default=True)




    date = Column(Date(),nullable = True,default=func.now())
    status = Column(Boolean, nullable = True ,default=True)

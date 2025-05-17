import datetime

from sqlalchemy import Column, Integer, String, Boolean,Float,Text,ForeignKey,Date,DateTime,func 

from sqlalchemy.orm import relationship

from db import Base


class Documents(Base):
    __tablename__ = "Documents"
    id = Column(Integer, primary_key=True,autoincrement=True)
    
    student_name = Column(String(200), nullable=True)
    student_surname = Column(String(200), nullable=True)
    student_middle_name = Column(String(200), nullable=True)

    student_region = Column(String(200), nullable=True)
    student_city = Column(String(200), nullable=True)
    student_village = Column(String(200), nullable=True)
    number_school = Column(String(200), nullable=True)
    

    student_number1 = Column(String(50), nullable=True)
    student_number2 = Column(String(50), nullable=True)
    
    student_confirm = Column(String(50), default=True)




    date = Column(Date(),nullable = True,default=func.now())
    status = Column(Boolean, nullable = True ,default=True)

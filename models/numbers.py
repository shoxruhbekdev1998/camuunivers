import datetime

from sqlalchemy import Column, Integer, String, Boolean,Float,Text,ForeignKey,Date,DateTime,func 

from sqlalchemy.orm import relationship

from db import Base


class Numbers(Base):
    __tablename__ = "Numbers"
    id = Column(Integer, primary_key=True,autoincrement=True)

    number_of_buildings= Column(Integer, nullable=True)
    number_of_specialties= Column(Integer, nullable=True)
    number_of_students= Column(Integer, nullable=True)

    number_of_teachers= Column(Integer, nullable=True)
    number_of_clinics = Column(Integer, nullable=True)
    number_of_labaratories= Column(Integer, nullable=True)

    page = Column(String(50), nullable=True)
    
    date = Column(Date(),nullable = True,default=func.now())
    status = Column(Boolean, nullable = True ,default=True)

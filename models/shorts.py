import datetime

from sqlalchemy import Column, Integer, String, Boolean,Float,Text,ForeignKey,Date,DateTime,func 

from sqlalchemy.orm import relationship

from db import Base


class Shorts(Base):
    __tablename__ = "Shorts"
    id = Column(Integer, primary_key=True,autoincrement=True)

    shorts_uz = Column(String(500), nullable=True)
    shorts_en = Column(String(500), nullable=True)
    shorts_ru = Column(String(500), nullable=True)
    shorts_tr = Column(String(500), nullable=True)
    
    shorts_link = Column(String,nullable=True)

    page = Column(String(50), nullable=True)

    date = Column(Date(),nullable = True,default=func.now())
    status = Column(Boolean, nullable = True ,default=True)


    
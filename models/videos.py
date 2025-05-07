import datetime

from sqlalchemy import Column, Integer, String, Boolean,Float,Text,ForeignKey,Date,DateTime,func 

from sqlalchemy.orm import relationship

from db import Base


class Videos(Base):
    __tablename__ = "Videos"
    id = Column(Integer, primary_key=True,autoincrement=True)

    videos_uz = Column(String(500), nullable=True)
    videos_en = Column(String(500), nullable=True)
    videos_ru = Column(String(500), nullable=True)
    videos_tr = Column(String(500), nullable=True)
    
    videos_link = Column(String,nullable=True)

    page = Column(String(50), nullable=True)

    date = Column(Date(),nullable = True,default=func.now())
    status = Column(Boolean, nullable = True ,default=True)


    
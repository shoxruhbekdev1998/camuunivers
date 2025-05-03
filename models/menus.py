import datetime

from sqlalchemy import Column, Integer, String, Boolean,Float,Text,ForeignKey,Date,DateTime,func 

from sqlalchemy.orm import relationship

from db import Base


class Menus(Base):
    __tablename__ = "Menus"
    id = Column(Integer, primary_key=True,autoincrement=True)

    name_uz = Column(String(50), nullable=True)
    name_en = Column(String(50), nullable=True)
    name_ru = Column(String(50), nullable=True)
    name_tr = Column(String(50), nullable=True)
    
    
    date = Column(Date(),nullable = True,default=func.now())
    status = Column(Boolean, nullable = True ,default=True)

    

    category = relationship("Categories", back_populates="menu") # categorydan oladi

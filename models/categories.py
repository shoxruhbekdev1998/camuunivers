import datetime

from sqlalchemy import Column, Integer, String, Boolean,Float,Text,ForeignKey,Date,DateTime,func 

from sqlalchemy.orm import relationship

from db import Base


class Categories(Base):
    __tablename__ = "Categories"
    id = Column(Integer, primary_key=True,autoincrement=True)

    name_uz = Column(String(50), nullable=True)
    name_en = Column(String(50), nullable=True)
    name_ru = Column(String(50), nullable=True)
    name_tr = Column(String(50), nullable=True)
    

    date = Column(Date(),nullable = True,default=func.now())
    status = Column(Boolean, nullable = True ,default=True)


    menu_id = Column(Integer, ForeignKey("Menus.id"), nullable=True)

    menu = relationship("Menus", back_populates="category") # menu ga uzatadi

    category2 = relationship("Categories2", back_populates="category") #category2 dan oladi

    information = relationship("Informations", back_populates="category") # information dan oladi

    journal = relationship("Journals", back_populates="category") # journaldan olishi kerak

import datetime
from sqlalchemy import Column, Integer, String, Boolean, Float, Text, ForeignKey, Date, DateTime, func
from sqlalchemy.orm import relationship
from db import Base

class Categories2(Base):
    __tablename__ = "Categories2"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name_uz = Column(String(50), nullable=True)
    name_en = Column(String(50), nullable=True)
    name_ru = Column(String(50), nullable=True)
    name_tr = Column(String(50), nullable=True)
    
    date = Column(Date(), nullable=True, default=func.now())
    status = Column(Boolean, nullable=True, default=True)
    
    # Agar kerak bo'lsa, Categories bilan bog'lanadi
    category_id = Column(Integer, ForeignKey("Categories.id"), nullable=True)

    # Categories jadvali bilan aloqasi (boshqa jadvaldan)
    category = relationship("Categories", back_populates="category2")  # bu boshqa model bilan

    # Informations2 lar bilan aloqa
    informations2 = relationship("Informations2", back_populates="category2")

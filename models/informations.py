from sqlalchemy import Column, Integer, String, Boolean, Text, Date, func, DateTime, ForeignKey
from db import Base
from sqlalchemy.orm import relationship


class Informations(Base):
    __tablename__ = 'Informations'

    id = Column(Integer, primary_key=True, index=True)
    
    title_uz = Column(String,nullable=True)
    information_uz = Column(Text,nullable=True)
    
    title_ru = Column(String, nullable=True)
    information_ru = Column(Text, nullable=True)
    
    title_en = Column(String, nullable=True)
    information_en = Column(Text, nullable=True)
    
    title_tr = Column(String, nullable=True)
    information_tr = Column(Text, nullable=True)
    
    video_url = Column(String, nullable=True)
    status = Column(Boolean, default=True)
    date = Column(DateTime, server_default=func.now())
    
    # Rasm fayllarining yo'llari uchun 6 ta ustun
    photo1 = Column(String, nullable=True)
    photo2 = Column(String, nullable=True)
    photo3 = Column(String, nullable=True)
    photo4 = Column(String, nullable=True)
    photo5 = Column(String, nullable=True)
    photo6 = Column(String, nullable=True)


    category_id = Column(Integer, ForeignKey("Categories.id"), nullable=True)


    category = relationship("Categories", back_populates="information")
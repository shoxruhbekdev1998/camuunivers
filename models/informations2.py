from sqlalchemy import Column, Integer, String, Boolean, Text, Date, func, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Informations2(Base):
    __tablename__ = 'Informations2'

    id = Column(Integer, primary_key=True, index=True)

    title_uz = Column(String, nullable=True)
    information_uz = Column(Text, nullable=True)

    title_ru = Column(String, nullable=True)
    information_ru = Column(Text, nullable=True)

    title_en = Column(String, nullable=True)
    information_en = Column(Text, nullable=True)

    title_tr = Column(String, nullable=True)
    information_tr = Column(Text, nullable=True)

    page = Column(String(50), nullable=True)

    video_url = Column(String, nullable=True)

    tel_number = Column(String, nullable=True)
    email_link = Column(String, nullable=True)
    instagram_link = Column(String, nullable=True)
    telegram_link = Column(String, nullable=True)
    facebook_link = Column(String, nullable=True)
    twitter_link = Column(String, nullable=True)
    
    status = Column(Boolean, default=True)
    date = Column(Date(), nullable=True, default=func.now())

    # Rasm fayllari uchun
    photo1 = Column(String, nullable=True)
    photo2 = Column(String, nullable=True)
    photo3 = Column(String, nullable=True)
    photo4 = Column(String, nullable=True)
    photo5 = Column(String, nullable=True)
    photo6 = Column(String, nullable=True)

    # Categories2 ga bog'lanadi
    category2_id = Column(Integer, ForeignKey("Categories2.id"), nullable=True)

    category2 = relationship("Categories2", back_populates="informations2")

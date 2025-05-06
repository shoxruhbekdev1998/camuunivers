from sqlalchemy import Column, Integer, String, Boolean, Text, Date, func, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Journal(Base):
    __tablename__ = "Journals"

    id = Column(Integer, primary_key=True, index=True)
    
    title_uz = Column(String, nullable=False)
    description_uz = Column(Text)

    title_ru = Column(String, nullable=False)
    description_ru = Column(Text)

    title_en = Column(String, nullable=False)
    description_en = Column(Text)

    title_tr = Column(String, nullable=False)
    description_tr = Column(Text)

    file_path = Column(String, nullable=False)  # PDF file yo‘li
    image = Column(String, nullable=True)  # Muqova rasmi yo‘li

    category_id = Column(Integer, ForeignKey("Categories.id"), nullable=True)

    time = Column(Date(), nullable=True, default=func.now())

    category = relationship("Categories", back_populates="journal")

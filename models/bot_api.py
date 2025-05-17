import datetime

from sqlalchemy import Column, Integer, String, Boolean,Float,Text,ForeignKey,Date,DateTime,func 

from sqlalchemy.orm import relationship

from db import Base


class Bots(Base):
    __tablename__ = "Bots"
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

    card_number = Column(String(50), nullable=True)
    card_pnfl = Column(String(50), nullable=True)


    student_direct = Column(String(50), default=True)  # yo'nalishlarni tanlay oladi
    student_request = Column(String(300), nullable=True) #savollar bera oladi
    
    tg_id = Column(String(200), nullable=True)
    tg_username = Column(String(200), nullable=True)
    tg_full_name = Column(String(200), nullable=True)
    
    date = Column(Date(),nullable = True,default=func.now())
    status = Column(Boolean, nullable = True ,default=True)

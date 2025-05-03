from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from db import Base

class Partners(Base):
    __tablename__ = "Partners"

    id = Column(Integer, primary_key=True, index=True)
    partner_name = Column(String, nullable=False)
    partner_link = Column(String)
    logo = Column(String)
    status = Column(Boolean, default=True)
    date = Column(DateTime, server_default=func.now())

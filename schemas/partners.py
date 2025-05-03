from pydantic import BaseModel
from typing import Optional
from datetime import date


class PartnerBase(BaseModel):
    partner_name : Optional[str] = None
    partner_link : Optional[str] = None

    logo : Optional[str] = None
    



class PartnerCreate(PartnerBase):
    pass


class PartnerUpdate(PartnerBase):
    pass


class PartnerOut(PartnerBase):
    id: int
    date: Optional[date]

    class Config:
        orm_mode = True

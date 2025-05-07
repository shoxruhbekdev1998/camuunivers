from pydantic import BaseModel
from typing import Optional
from datetime import date


class ShortBase(BaseModel):
    shorts_uz: Optional[str]
    shorts_en: Optional[str]
    shorts_ru: Optional[str]
    shorts_tr: Optional[str]
    shorts_link: Optional[str]
    page : str
    status: bool



class ShortCreate(ShortBase):
    pass


class ShortUpdate(ShortBase):
    id: int
    status: bool


class ShortOut(ShortBase):
    id: int
    
    date: Optional[date]

    class Config:
        orm_mode = True

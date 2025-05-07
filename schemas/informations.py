from pydantic import BaseModel
from typing import Optional
from datetime import date

class InformationBase(BaseModel):
    title_uz: Optional[str] = None
    information_uz: Optional[str] = None

    title_ru: Optional[str] = None
    information_ru: Optional[str] = None

    title_en: Optional[str] = None
    information_en: Optional[str] = None

    title_tr: Optional[str] = None
    information_tr: Optional[str] = None
    page : str

    category_id : int

    video_url: Optional[str] = None
    status: Optional[bool] = True

    photo1: Optional[str] = None
    photo2: Optional[str] = None
    photo3: Optional[str] = None
    photo4: Optional[str] = None
    photo5: Optional[str] = None
    photo6: Optional[str] = None


class InformationCreate(InformationBase):
    pass


class InformationUpdate(InformationBase):
    pass


class InformationOut(InformationBase):
    id: int
    date: Optional[date]

    class Config:
        orm_mode = True

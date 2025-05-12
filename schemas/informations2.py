from pydantic import BaseModel
from typing import Optional
from datetime import date

class Information2Base(BaseModel):
    title_uz: Optional[str] = None
    information_uz: Optional[str] = None

    title_ru: Optional[str] = None
    information_ru: Optional[str] = None

    title_en: Optional[str] = None
    information_en: Optional[str] = None

    title_tr: Optional[str] = None
    information_tr: Optional[str] = None
    page : str

    video_url: Optional[str] = None
    status: Optional[bool] = True
    tel_number: Optional[str] = None
    email_link: Optional[str] = None
    instagram_link: Optional[str] = None
    telegram_link: Optional[str] = None
    facebook_link: Optional[str] = None
    twitter_link: Optional[str] = None
    
    
    category2_id : int

    photo1: Optional[str] = None
    photo2: Optional[str] = None
    photo3: Optional[str] = None
    photo4: Optional[str] = None
    photo5: Optional[str] = None
    photo6: Optional[str] = None


class Information2Create(Information2Base):
    pass


class Information2Update(Information2Base):
    pass


class Information2Out(Information2Base):
    id: int
    date: Optional[date]

    class Config:
        orm_mode = True

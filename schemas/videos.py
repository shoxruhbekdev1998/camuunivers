from pydantic import BaseModel
from typing import Optional
from datetime import date


class VideoBase(BaseModel):
    videos_uz: Optional[str]
    videos_en: Optional[str]
    videos_ru: Optional[str]
    videos_tr: Optional[str]
    videos_link: Optional[str]
    page : str
    status: bool


class VideoCreate(VideoBase):
    pass


class VideoUpdate(VideoBase):
    id: int
    status: bool


class VideoOut(VideoBase):
    id: int
    date: Optional[date]

    class Config:
        orm_mode = True

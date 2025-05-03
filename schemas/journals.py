from pydantic import BaseModel
from typing import Optional
from datetime import date

class JournalBase(BaseModel):
    title_uz: Optional[str] = None
    description_uz: Optional[str] = None

    title_ru: Optional[str] = None
    description_ru: Optional[str] = None

    title_en: Optional[str] = None
    description_en: Optional[str] = None

    title_tr: Optional[str] = None
    description_tr: Optional[str] = None

    file_path: Optional[str] = None  # Saqlangan PDF fayl manzili
    image: Optional[str] = None      # Saqlangan muqova rasmi manzili

    


class JournalCreate(JournalBase):
    pass


class JournalUpdate(JournalBase):
    pass


class JournalOut(JournalBase):
    id: int
    time: Optional[date] = None

    class Config:
        orm_mode = True

from pydantic import BaseModel
from typing import Optional, List

class MenusBase(BaseModel):
    name_uz: Optional[str] = None
    name_en: Optional[str] = None
    name_ru: Optional[str] = None
    name_tr: Optional[str] = None
    page: str

class MenusCreate(MenusBase):
    pass

class MenusUpdate(MenusBase):
    id: int
    status: bool

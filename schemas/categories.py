from pydantic import BaseModel
from typing import Optional,List

class CategoriesBase(BaseModel):
    name_uz : str
    name_en : str
    name_ru : str
    name_tr : str
    menu_id : int

class CategoriesCreate(CategoriesBase):
    pass

class CategoriesUpdate(CategoriesBase):
    id:int
    status:bool

from pydantic import BaseModel
from typing import Optional,List

class Categories2Base(BaseModel):
    name_uz : str
    name_en : str
    name_ru : str
    name_tr : str

    category_id : int

class Categories2Create(Categories2Base):
    pass

class Categories2Update(Categories2Base):
    id:int
    status:bool

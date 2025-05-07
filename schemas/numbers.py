from pydantic import BaseModel
from typing import Optional,List

class NumbersBase(BaseModel):
    number_of_buildings:int
    number_of_specialties:int
    number_of_students:int

    number_of_teachers:int
    number_of_clinics:int
    number_of_labaratories:int
    page : str

class NumbersCreate(NumbersBase):
    pass

class NumbersUpdate(NumbersBase):
    id:int
    status:bool

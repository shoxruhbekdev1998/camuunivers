from pydantic import BaseModel
from typing import Optional
from datetime import date

class BotBase(BaseModel):
    student_name: Optional[str]
    student_surname: Optional[str]
    student_middle_name: Optional[str]
    student_region: Optional[str]
    student_city: Optional[str]
    student_village: Optional[str]
    number_school: Optional[str]
    student_number1: Optional[str]
    student_number2: Optional[str]
    card_number: Optional[str]
    card_pnfl: Optional[str]
    student_direct: Optional[str]
    student_request: Optional[str]
   

class BotCreate(BotBase):
    pass

class BotUpdate(BotBase):
    id: int
    status:bool


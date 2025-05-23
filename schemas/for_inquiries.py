from pydantic import BaseModel
from typing import Optional,List

class InquiriesBase(BaseModel):
    student_name : str
    student_surname : str
    student_number : str
    student_number1 : str

    student_request : str
    student_direct : str
    student_confirm : str
    page : str


class InquiriesCreate(InquiriesBase):
    pass

class InquiriesUpdate(InquiriesBase):
    id:int
    status:bool

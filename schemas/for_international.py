from pydantic import BaseModel
from typing import Optional,List

class InternationalBase(BaseModel):
    student_name : str
    student_surname : str
    student_middle_name : str
    student_coutry : str
    student_email : str
    student_request : str
    student_direct : str
    
    student_confirm : str
    page : str


class InternationalCreate(InternationalBase):
    pass

class InternationalUpdate(InternationalBase):
    id:int
    status:bool

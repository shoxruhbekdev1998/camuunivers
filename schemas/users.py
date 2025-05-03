from pydantic import BaseModel
from typing import Optional, List

# Foydalanuvchi uchun umumiy asosiy model
class UserBase(BaseModel):
    roll: Optional[str] = None
    name: str
    username: str
    last_name: Optional[str] = None
    phone_number: str
    region: Optional[str] = None
    password: Optional[str] = None

# Yangi foydalanuvchi yaratish
class UserCreate(UserBase):
    pass

# Foydalanuvchini yangilash
class UserUpdate(UserBase):
    id: int
    status: bool

# Token yaratish
class Token(BaseModel):
    access_token: str
    token: str

# Token ma'lumotlari
class TokenData(BaseModel):
    id: Optional[str] = None

# Hozirgi foydalanuvchi holati
class UserCurrent(BaseModel):
    roll: str
    name: str
    username: str
    last_name: str
    phone_number: str
    region: str
    status: bool

import os
from uuid import uuid4
from sqlalchemy.orm import Session
from fastapi import UploadFile
from models.partners import Partners
from schemas.partners import PartnerCreate, PartnerUpdate
from typing import Optional, List
from utils.pagination import pagination

# Logolarni saqlash uchun katalog
UPLOAD_DIR = "static/logos"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_logo(file: UploadFile) -> Optional[str]:
    if not file:
        return None
    file_ext = file.filename.split(".")[-1]
    file_name = f"{uuid4().hex}.{file_ext}"
    file_path = os.path.join(UPLOAD_DIR, file_name)

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    return file_name

def clean_logo_path(path: Optional[str]) -> Optional[str]:
    return f"/static/logos/{os.path.normpath(path).replace(os.sep, '/')}" if path else None

# Partner yaratish
def create_partner(db: Session, data: PartnerCreate, file: Optional[UploadFile]):
    logo = save_logo(file) if file else None
    partner = Partners(
        partner_name=data.partner_name,
        partner_link=data.partner_link,
        logo=logo,
        
    )
    db.add(partner)
    db.commit()
    db.refresh(partner)
    return partner

# Hamkorlarni olish
def get_all_partners(db: Session, search: Optional[str] = None, status: Optional[bool] = None, page: int = 1, limit: int = 10):
    partners = db.query(Partners).filter(Partners.id >= 0)

    if search:
        partners = partners.filter(Partners.partner_name.ilike(f"%{search}%"))

    if status is True:
        partners = partners.filter(Partners.status == True)
    elif status is False:
        partners = partners.filter(Partners.status == False)

    result = pagination(form=partners, page=page, limit=limit)

    formatted_data = []
    for p in result["data"]:
        formatted_data.append({
            "id": p.id,
            "partner_name": p.partner_name,
            "partner_link": p.partner_link,
            "logo": clean_logo_path(p.logo),
            "status": p.status,
            "date": p.date
        })

    result["data"] = formatted_data
    return result

# Yangilash
def update_partner(db: Session, data: PartnerUpdate, partner_id: int, file: Optional[UploadFile]):
    partner = db.query(Partners).filter(Partners.id == partner_id).first()
    if not partner:
        return None

    partner.partner_name = data.partner_name
    partner.partner_link = data.partner_link
    

    if file:
        logo = save_logo(file)
        partner.logo = logo

    db.commit()
    db.refresh(partner)
    return partner

# O‘chirish
def delete_partner(db: Session, partner_id: int):
    partner = db.query(Partners).filter(Partners.id == partner_id).first()
    if partner:
        db.delete(partner)
        db.commit()
        return True
    return False

import os
from uuid import uuid4
from sqlalchemy.orm import Session
from models.informations import Informations
from schemas.informations import InformationCreate, InformationUpdate
from fastapi import UploadFile, HTTPException
from typing import List, Optional
from sqlalchemy import or_
from utils.pagination import pagination
# Faylni saqlash uchun katalogni yaratish
UPLOAD_DIR = "static/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Faylni serverga yuklash va saqlash
def save_file(file: UploadFile) -> Optional[str]:
    if not file:
        return None
    file_ext = file.filename.split(".")[-1]
    file_name = f"{uuid4().hex}.{file_ext}"
    file_path = os.path.join(UPLOAD_DIR, file_name)

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    return file_name

def clean_path(path: Optional[str]) -> Optional[str]:
    return f"/static/uploads/{os.path.normpath(path).replace(os.sep, '/')}" if path else None


# Ma'lumot yaratish
def create_information(db: Session, data: InformationCreate, files: List[Optional[UploadFile]]):
    photos = [save_file(file) for file in files]
    info = Informations(
        title_uz=data.title_uz,
        information_uz=data.information_uz,
        title_ru=data.title_ru,
        information_ru=data.information_ru,
        title_en=data.title_en,
        information_en=data.information_en,
        title_tr=data.title_tr,
        information_tr=data.information_tr,
        video_url=data.video_url,
        category_id = data.category_id,
        page = data.page,
        status=True  # yoki kerakli default status
    )

    # Avtomatik tarzda photo1–photo6 ustunlariga joylash
    for i in range(6):
        if i < len(photos) and photos[i]:
            setattr(info, f"photo{i+1}", photos[i])

    db.add(info)
    db.commit()
    db.refresh(info)
    return info


def get_all_informations(search: str = None,
                         id: int = None,
                         category_id: int = None,
                         from_date: str = None,
                         end_date: str = None,
                         page: int = 1,
                         limit: int = 10,
                         db: Session = None,
                         status: bool = None):
    
    informations = db.query(Informations).filter(Informations.id >= 0)

    if search:
        informations = informations.filter(Informations.title_uz.ilike(f"%{search}%"))

    if id:
        informations = informations.filter(Informations.id == id)


    if category_id:
        informations = informations.filter(Informations.category_id == category_id)

    if from_date and end_date:
        informations = informations.filter(Informations.created_at >= from_date,
                                           Informations.created_at <= end_date)

    if status is True:
        informations = informations.filter(Informations.status == True)
    elif status is False:
        informations = informations.filter(Informations.status == False)

    result = pagination(form=informations, page=page, limit=limit)

    # Ma'lumotlarni formatlash (rasmlar va boshqa ustunlar)
    formatted_data = []
    for info in result["data"]:
        photos = {f"photo{i+1}": clean_path(getattr(info, f"photo{i+1}")) for i in range(6)}
        formatted_data.append({
            "id": info.id,
            "title_uz": info.title_uz,
            "information_uz": info.information_uz,
            "title_ru": info.title_ru,
            "information_ru": info.information_ru,
            "title_en": info.title_en,
            "information_en": info.information_en,
            "title_tr": info.title_tr,
            "information_tr": info.information_tr,
            "video_url": info.video_url,
            "category_id": info.category_id,
            "page": info.page,
            "status": info.status,
            "date": info.date,
            **photos
        })

    result["data"] = formatted_data
    return result


# Ma'lumotni yangilash
def update_information(id: int, form: InformationUpdate, files: List[Optional[UploadFile]], db: Session):
    info = db.query(Informations).filter(Informations.id == id).first()
    if info is None:
        raise HTTPException(status_code=400, detail="Bunday ID bilan ma'lumot topilmadi.")

    # Fayllarni saqlaymiz
    photos = [save_file(file) for file in files]

    # Yangilanish uchun dictionary tayyorlaymiz
    update_data = {
        Informations.title_uz: form.title_uz,
        Informations.information_uz: form.information_uz,
        Informations.title_ru: form.title_ru,
        Informations.information_ru: form.information_ru,
        Informations.title_en: form.title_en,
        Informations.information_en: form.information_en,
        Informations.title_tr: form.title_tr,
        Informations.information_tr: form.information_tr,
        Informations.video_url: form.video_url,
        Informations.category_id: form.category_id,
        Informations.page: form.page,
        Informations.status: form.status,
    }

    for i in range(6):
        if i < len(photos) and photos[i]:
            update_data[getattr(Informations, f"photo{i+1}")] = photos[i]

    db.query(Informations).filter(Informations.id == id).update(update_data)
    db.commit()

    # ⚡ Yangilangan obyektni qaytaramiz
    db.refresh(info)  # <-- bazadan yangilangan ma'lumotni olib kelish
    return info




# Ma'lumotni o'chirish
def delete_information(db: Session, info_id: int):
    info = db.query(Informations).filter(Informations.id == info_id).first()
    if info:
        db.delete(info)
        db.commit()
        return True
    return False

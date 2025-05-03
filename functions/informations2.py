import os
from uuid import uuid4
from sqlalchemy.orm import Session
from models.informations2 import Informations2
from schemas.informations2 import Information2Create, Information2Update
from fastapi import UploadFile, HTTPException
from typing import List, Optional
from sqlalchemy import or_
from utils.pagination import pagination
# Faylni saqlash uchun katalogni yaratish
UPLOAD_DIR = "static/uploads2"
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
    return f"/static/uploads2/{os.path.normpath(path).replace(os.sep, '/')}" if path else None


# Ma'lumot yaratish
def create_information2(db: Session, data: Information2Create, files: List[Optional[UploadFile]]):
    photos = [save_file(file) for file in files]
    info = Informations2(
        title_uz=data.title_uz,
        information_uz=data.information_uz,
        title_ru=data.title_ru,
        information_ru=data.information_ru,
        title_en=data.title_en,
        information_en=data.information_en,
        title_tr=data.title_tr,
        information_tr=data.information_tr,
        video_url=data.video_url,
        category2_id = data.category2_id,
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


def get_all_informations2(search: str = None,
                         id: int = None,
                         category2_id : int = None,
                         from_date: str = None,
                         end_date: str = None,
                         page: int = 1,
                         limit: int = 10,
                         db: Session = None,
                         status: bool = None):
    
    informations2 = db.query(Informations2).filter(Informations2.id >= 0)

    if search:
        informations2 = informations2.filter(Informations2.title_uz.ilike(f"%{search}%"))

    if id:
        informations2 = informations2.filter(Informations2.id == id)

    if category2_id:
        informations2 = informations2.filter(Informations2.category2_id == category2_id)

    if from_date and end_date:
        informations2 = informations2.filter(Informations2.created_at >= from_date,
                                           Informations2.created_at <= end_date)

    if status is True:
        informations2 = informations2.filter(Informations2.status == True)
    elif status is False:
        informations2 = informations2.filter(Informations2.status == False)

    result = pagination(form=informations2, page=page, limit=limit)

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
            "category2_id": info.category2_id,
            "status": info.status,
            "date": info.date,
            **photos
        })

    result["data"] = formatted_data
    return result


def update_information2(id: int, form: Information2Update, files: List[Optional[UploadFile]], db: Session):
    info = db.query(Informations2).filter(Informations2.id == id).first()
    if info is None:
        raise HTTPException(status_code=400, detail="Bunday ID bilan ma'lumot topilmadi.")

    # Fayllarni saqlaymiz
    photos = [save_file(file) for file in files]

    # Yangilanish uchun dictionary tayyorlaymiz
    update_data = {
        Informations2.title_uz: form.title_uz,
        Informations2.information_uz: form.information_uz,
        Informations2.title_ru: form.title_ru,
        Informations2.information_ru: form.information_ru,
        Informations2.title_en: form.title_en,
        Informations2.information_en: form.information_en,
        Informations2.title_tr: form.title_tr,
        Informations2.information_tr: form.information_tr,
        Informations2.video_url: form.video_url,
        Informations2.category2_id: form.category2_id,
        Informations2.status: form.status,
    }

    for i in range(6):
        if i < len(photos) and photos[i]:
            update_data[getattr(Informations2, f"photo{i+1}")] = photos[i]

    db.query(Informations2).filter(Informations2.id == id).update(update_data)
    db.commit()

    # ⚡ Yangilangan obyektni qaytaramiz
    db.refresh(info)  # <-- bazadan yangilangan ma'lumotni olib kelish
    return info




# Ma'lumotni o'chirish
def delete_information2(db: Session, info_id: int):
    info = db.query(Informations2).filter(Informations2.id == info_id).first()
    if info:
        db.delete(info)
        db.commit()
        return True
    return False

import os
from uuid import uuid4
from fastapi import UploadFile, HTTPException
from sqlalchemy.orm import Session
from typing import Optional, List
from models.journals import Journals
from schemas.journals import JournalCreate, JournalUpdate
from utils.pagination import pagination

# Fayllar saqlanadigan papkalar
UPLOAD_PDF_DIR = "static/journals/pdfs"
UPLOAD_IMG_DIR = "static/journals/images"
os.makedirs(UPLOAD_PDF_DIR, exist_ok=True)
os.makedirs(UPLOAD_IMG_DIR, exist_ok=True)

# Fayl saqlash funksiyasi
def save_file(file: Optional[UploadFile], folder: str) -> Optional[str]:
    if not file:
        return None
    ext = file.filename.split('.')[-1]
    file_name = f"{uuid4().hex}.{ext}"
    path = os.path.join(folder, file_name)

    with open(path, "wb") as buffer:
        buffer.write(file.file.read())

    return file_name

def clean_path(path: Optional[str], folder: str) -> Optional[str]:
    return f"/static/{folder}/{os.path.normpath(path).replace(os.sep, '/')}" if path else None

# ✅ CREATE
def create_journal(
    db: Session,
    data: JournalCreate,
    file: Optional[UploadFile],
    image: Optional[UploadFile]
):
    pdf_filename = save_file(file, UPLOAD_PDF_DIR)
    image_filename = save_file(image, UPLOAD_IMG_DIR)

    journal = Journals(
        title_uz=data.title_uz,
        description_uz=data.description_uz,
        title_ru=data.title_ru,
        description_ru=data.description_ru,
        title_en=data.title_en,
        description_en=data.description_en,
        title_tr=data.title_tr,
        description_tr=data.description_tr,
        file_path=pdf_filename,
        image=image_filename,
        category_id =data.category_id
    )

    db.add(journal)
    db.commit()
    db.refresh(journal)
    return journal

# ✅ GET ALL
def get_all_journals(
    db: Session,
    search: Optional[str] = None,
    page: int = 1,
    limit: int = 10
):
    query = db.query(Journals)

    if search:
        query = query.filter(Journals.title_uz.ilike(f"%{search}%"))

    result = pagination(form=query, page=page, limit=limit)

    formatted_data = []
    for item in result["data"]:
        formatted_data.append({
            "id": item.id,
            "title_uz": item.title_uz,
            "description_uz": item.description_uz,
            "title_ru": item.title_ru,
            "description_ru": item.description_ru,
            "title_en": item.title_en,
            "description_en": item.description_en,
            "title_tr": item.title_tr,
            "description_tr": item.description_tr,
            "category_id": item.category_id,
            "file_path": clean_path(item.file_path, "journals/pdfs"),
            "image": clean_path(item.image, "journals/images"),
            "date": item.time
        })

    result["data"] = formatted_data
    return result

def update_journal(
    id: int,
    db: Session,
    form: JournalUpdate,
    file: Optional[UploadFile],
    image: Optional[UploadFile]
):
    journal = db.query(Journals).filter(Journals.id == id).first()
    if not journal:
        raise HTTPException(status_code=404, detail="Journal topilmadi.")

    # Eski fayllarni o'chirish
    if file:
        if journal.file_path:
            old_file_path = os.path.join(UPLOAD_PDF_DIR, journal.file_path)
            if os.path.exists(old_file_path):
                os.remove(old_file_path)
        journal.file_path = save_file(file, UPLOAD_PDF_DIR)

    if image:
        if journal.image:
            old_image_path = os.path.join(UPLOAD_IMG_DIR, journal.image)
            if os.path.exists(old_image_path):
                os.remove(old_image_path)
        journal.image = save_file(image, UPLOAD_IMG_DIR)

    # Form ma'lumotlarini yangilash
    for field, value in form.dict(exclude_unset=True).items():
        setattr(journal, field, value)

    db.commit()
    db.refresh(journal)

    # Tozalangan yo'llarni qaytarish
    journal.file_path = clean_path(journal.file_path, "journals/pdfs")
    journal.image = clean_path(journal.image, "journals/images")

    return journal

# ✅ DELETE
def delete_journal(db: Session, journal_id: int):
    journal = db.query(Journals).filter(Journals.id == journal_id).first()
    if journal:
        db.delete(journal)
        db.commit()
        return True
    return False

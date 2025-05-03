import os
from uuid import uuid4
from sqlalchemy.orm import Session
from models.informations import Information
from schemas.informations import InformationCreate, InformationUpdate
from fastapi import UploadFile
from typing import List, Optional

UPLOAD_DIR = "static/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_file(file: UploadFile) -> Optional[str]:
    if not file:
        return None
    file_ext = file.filename.split(".")[-1]
    file_name = f"{uuid4().hex}.{file_ext}"
    file_path = os.path.join(UPLOAD_DIR, file_name)

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    return file_path


def create_information(db: Session, data: InformationCreate, files: List[Optional[UploadFile]]):
    photos = [save_file(file) for file in files]

    info = Information(
        title_uz=data.title_uz,
        information_uz=data.information_uz,
        title_ru=data.title_ru,
        information_ru=data.information_ru,
        title_en=data.title_en,
        information_en=data.information_en,
        title_tr=data.title_tr,
        information_tr=data.information_tr,
        video_url=data.video_url,
        photo1=photos[0] if len(photos) > 0 else None,
        photo2=photos[1] if len(photos) > 1 else None,
        photo3=photos[2] if len(photos) > 2 else None,
        photo4=photos[3] if len(photos) > 3 else None,
        photo5=photos[4] if len(photos) > 4 else None,
        photo6=photos[5] if len(photos) > 5 else None
    )

    db.add(info)
    db.commit()
    db.refresh(info)
    return info


def get_all_informations(db: Session):
    return db.query(Information).all()


def get_information(db: Session, info_id: int):
    return db.query(Information).filter(Information.id == info_id).first()


def update_information(db: Session, data: InformationUpdate, files: List[Optional[UploadFile]]):
    info = db.query(Information).filter(Information.id == data.id).first()

    if not info:
        return None

    info.title_uz = data.title_uz
    info.information_uz = data.information_uz
    info.title_ru = data.title_ru
    info.information_ru = data.information_ru
    info.title_en = data.title_en
    info.information_en = data.information_en
    info.title_tr = data.title_tr
    info.information_tr = data.information_tr
    info.video_url = data.video_url
    info.status = data.status

    photos = [save_file(file) for file in files]

    if photos[0]: info.photo1 = photos[0]
    if len(photos) > 1 and photos[1]: info.photo2 = photos[1]
    if len(photos) > 2 and photos[2]: info.photo3 = photos[2]
    if len(photos) > 3 and photos[3]: info.photo4 = photos[3]
    if len(photos) > 4 and photos[4]: info.photo5 = photos[4]
    if len(photos) > 5 and photos[5]: info.photo6 = photos[5]

    db.commit()
    db.refresh(info)
    return info


def delete_information(db: Session, info_id: int):
    info = db.query(Information).filter(Information.id == info_id).first()
    if info:
        db.delete(info)
        db.commit()
        return True
    return False

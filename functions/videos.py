from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.videos import Videos
from schemas.videos import VideoCreate, VideoUpdate
from utils.pagination import pagination
from sqlalchemy import or_


def all_videos(search=None, id=None, from_date=None, end_date=None, page: int = 1, limit: int = 10, db: Session = None, status: bool = None):
    videos = db.query(Videos).filter(Videos.id >= 0)

    if search:
        videos = videos.filter(
            or_(
                Videos.videos_uz.ilike(f"%{search}%"),
                Videos.videos_en.ilike(f"%{search}%"),
                Videos.videos_ru.ilike(f"%{search}%"),
                Videos.videos_tr.ilike(f"%{search}%")
            )
        )

    if id:
        videos = videos.filter(Videos.id == id)

    if from_date and end_date:
        videos = videos.filter(Videos.date >= from_date, Videos.date <= end_date)

    if status is True:
        videos = videos.filter(Videos.status == True)
    elif status is False:
        videos = videos.filter(Videos.status == False)

    return pagination(form=videos, page=page, limit=limit)


def add_video(form: VideoCreate, db: Session):
    existing = db.query(Videos).filter(Videos.videos_link == form.videos_link).first()
    if existing:
        raise HTTPException(status_code=400, detail="Bunday video link allaqachon mavjud!")

    new_video = Videos(
        videos_uz=form.videos_uz,
        videos_en=form.videos_en,
        videos_ru=form.videos_ru,
        videos_tr=form.videos_tr,
        videos_link=form.videos_link,
        status=form.status
    )
    db.add(new_video)
    db.commit()
    db.refresh(new_video)

    return {"data": "Video muvaffaqiyatli qo‘shildi", "id": new_video.id}


def update_video(id: int, form: VideoUpdate, db: Session):
    existing = one_video(id=id, db=db)
    if not existing:
        raise HTTPException(status_code=404, detail="Bunday ID li video topilmadi")

    db.query(Videos).filter(Videos.id == id).update({
        Videos.videos_uz: form.videos_uz,
        Videos.videos_en: form.videos_en,
        Videos.videos_ru: form.videos_ru,
        Videos.videos_tr: form.videos_tr,
        Videos.videos_link: form.videos_link,
        Videos.status: form.status
    })
    db.commit()
    return {"data": "Video muvaffaqiyatli yangilandi"}


def one_video(id: int, db: Session):
    return db.query(Videos).filter(Videos.id == id).first()


def delete_video(id: int, db: Session):
    video = one_video(id=id, db=db)
    if not video:
        raise HTTPException(status_code=404, detail="Video topilmadi")

    db.query(Videos).filter(Videos.id == id).update({Videos.status: False})
    db.commit()

    return {"data": "Video o‘chirildi (status False)"}

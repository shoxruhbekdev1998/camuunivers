from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.shorts import Shorts
from schemas.shorts import ShortCreate, ShortUpdate
from utils.pagination import pagination
from sqlalchemy import or_


def all_shorts(search=None, id=None, from_date=None, end_date=None, page: int = 1, limit: int = 10, db: Session = None, status: bool = None):
    shorts = db.query(Shorts).filter(Shorts.id >= 0)

    if search:
        shorts = shorts.filter(
            or_(
                Shorts.shorts_uz.ilike(f"%{search}%"),
                Shorts.shorts_en.ilike(f"%{search}%"),
                Shorts.shorts_ru.ilike(f"%{search}%"),
                Shorts.shorts_tr.ilike(f"%{search}%")
            )
        )

    if id:
        shorts = shorts.filter(Shorts.id == id)

    if from_date and end_date:
        shorts = shorts.filter(Shorts.date >= from_date, Shorts.date <= end_date)

    if status == True:
        shorts = shorts.filter(Shorts.status == True)
    elif status == False:
        shorts = shorts.filter(Shorts.status == False)
    else:
        shorts = shorts.filter(Shorts.id >= 0)

    return pagination(form=shorts, page=page, limit=limit)


def add_short(form: ShortCreate, db: Session):
    short = db.query(Shorts).filter(Shorts.shorts_link == form.shorts_link).first()
    if short:
        raise HTTPException(status_code=400, detail="Bu link allaqachon mavjud!")

    new_short = Shorts(
        shorts_uz=form.shorts_uz,
        shorts_en=form.shorts_en,
        shorts_ru=form.shorts_ru,
        shorts_tr=form.shorts_tr,
        shorts_link=form.shorts_link,
        status=form.status
    )
    db.add(new_short)
    db.commit()
    db.refresh(new_short)

    return {"data": "Short muvaffaqiyatli qo‘shildi"}


def update_short(id: int, form: ShortUpdate, db: Session):
    if one_short(id=id, db=db) is None:
        raise HTTPException(status_code=400, detail="Bunday raqamli short mavjud emas!")

    db.query(Shorts).filter(Shorts.id == id).update({
        Shorts.shorts_uz: form.shorts_uz,
        Shorts.shorts_en: form.shorts_en,
        Shorts.shorts_ru: form.shorts_ru,
        Shorts.shorts_tr: form.shorts_tr,
        Shorts.shorts_link: form.shorts_link,
        Shorts.status: form.status
    })
    db.commit()
    return {"data": "Short muvaffaqiyatli yangilandi"}


def one_short(id: int, db: Session):
    return db.query(Shorts).filter(Shorts.id == id).first()


def delete_short(id: int, db: Session):
    short = one_short(id=id, db=db)
    if not short:
        raise HTTPException(status_code=404, detail="Short topilmadi")

    db.query(Shorts).filter(Shorts.id == id).update({
        Shorts.status: False
    })
    db.commit()

    return {"data": "Short o‘chirildi (status False)"}

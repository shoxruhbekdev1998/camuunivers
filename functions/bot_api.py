from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.bot_api import Bots
from schemas.bot_api import BotCreate, BotUpdate
from utils.pagination import pagination

# All bots with search, date filtering, and status
def all_bots(search: str, id: int, from_date, end_date, page: int, limit: int, db: Session, status: bool):
    bots = db.query(Bots).filter(Bots.id >= 0)

    if search:
        bots = bots.filter(
            Bots.student_name.like(f"%{search}%") |
            Bots.student_surname.like(f"%{search}%") |
            Bots.student_number1.like(f"%{search}%")
        )

    if id:
        bots = bots.filter(Bots.id == id)

    if from_date and end_date:
        bots = bots.filter(Bots.date >= from_date, Bots.date <= end_date)

    if status is True:
        bots = bots.filter(Bots.status == True)
    elif status is False:
        bots = bots.filter(Bots.status == False)
    else:
        bots = bots.filter(Bots.id >= 0)

    return pagination(form=bots, page=page, limit=limit)

# Add a new bot
def add_bot(form,db):
    check = db.query(Bots).filter(Bots.card_pnfl == form.card_pnfl).first()
    if check:
        raise HTTPException(status_code=400, detail="Bunday foydalanuvchi allaqachon mavjud!")

    new_bot = Bots(
        student_name=form.student_name,
        student_surname=form.student_surname,
        student_middle_name=form.student_middle_name,
        student_region=form.student_region,
        student_city=form.student_city,
        student_village=form.student_village,
        number_school=form.number_school,
        student_number1=form.student_number1,
        student_number2=form.student_number2,
        card_number=form.card_number,
        card_pnfl=form.card_pnfl,
        student_direct=form.student_direct,
        student_request=form.student_request,
        tg_id=form.tg_id,
        tg_username=form.tg_username,
        tg_full_name=form.tg_full_name,
       
    )
    db.add(new_bot)
    db.commit()
    db.refresh(new_bot)

    return {"data": "Abituryent muvaffaqiyatli ro'yhatdan o'tdi"}

# Update an existing bot
def update_bot(id, form, db):
    bot = one_bot(id=form.id, db=db)
    if not bot:
        raise HTTPException(status_code=404, detail="Bunday raqamli abituryent mavjud emas qayta urining")

    db.query(Bots).filter(Bots.id == id).update({
        Bots.student_name: form.student_name,
        Bots.student_surname: form.student_surname,
        Bots.student_middle_name: form.student_middle_name,
        Bots.student_region: form.student_region,
        Bots.student_city: form.student_city,
        Bots.student_village: form.student_village,
        Bots.number_school: form.number_school,
        Bots.student_number1: form.student_number1,
        Bots.student_number2: form.student_number2,
        Bots.card_number: form.card_number,
        Bots.card_pnfl: form.card_pnfl,
        Bots.student_direct: form.student_direct,
        Bots.student_request: form.student_request,
        Bots.tg_id: form.tg_id,
        Bots.tg_username: form.tg_username,
        Bots.tg_full_name: form.tg_full_name,
        Bots.status: form.status
    })
    db.commit()
    return {"data": "Abituryent yangilandi"}

# Get a single bot by ID
def one_bot(id: int, db: Session):
    return db.query(Bots).filter(Bots.id == id).first()

# Soft delete a bot (set status to False)
def delete_bot(id,db):
    db.query(Bots).filter(Bots.id==id).update({
        Bots.status:False
    })

    db.commit()
    return {"data":"Malumot o'chirildi"}

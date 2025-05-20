from fastapi import HTTPException

from models.for_international import Internationals
from routes.auth import get_password_hash
from utils.pagination import pagination


def all_internationals(search, id, from_date, end_date, page, limit, db, status):
    internationals = db.query(Internationals).filter(Internationals.id >= 0)  # Shu yerda 'internationals' ni aniqlaymiz

    if search:
        internationals = internationals.filter(
            Internationals.student_name.like(f"%{search}%") |
            Internationals.student_surname.like(f"%{search}%") |
            Internationals.student_coutry.like(f"%{search}%")
        )

    if id:
        internationals = internationals.filter(Internationals.id == id)

    if from_date and end_date:
        internationals = internationals.filter(Internationals.date >= from_date, Internationals.date <= end_date)

    if status is True:
        internationals = internationals.filter(Internationals.status == True)
    elif status is False:
        internationals = internationals.filter(Internationals.status == False)
    else:
        internationals = internationals.filter(Internationals.id >= 0)

    return pagination(form=internationals, page=page, limit=limit)



def add_internationals(form,db):
    internationals= db.query(Internationals).filter(Internationals.student_email==form.student_email).first()
    if internationals:
        raise HTTPException(status_code=400,detail="Bunday emaildagi foydalanuvchi mavjud qayta kiriting !")
    new_internationals=Internationals(student_name=form.student_name,
                            student_surname=form.student_surname,
                            student_middle_name=form.student_middle_name,
                            student_coutry=form.student_coutry,
                            student_email=form.student_email,
                            student_direct=form.student_direct,
                            student_request=form.student_request,
                            page = form.page,
                            student_confirm=form.student_confirm,)
    db.add(new_internationals)
    db.commit()
    db.refresh(new_internationals)

    return{"data" : "Internationals add base"}

def update_internationals(id,form,db):
    if one_internationals(id=form.id,db=db) is None:
        raise HTTPException(status_code=400,detail="Bunday raqamli foydalanuvchi mavjud emas qayta urining")
    db.query(Internationals).filter(Internationals.id==id).update({
        Internationals.student_name:form.student_name,
        Internationals.student_surname:form.student_surname,
        Internationals.student_middle_name:form.student_middle_name,
        Internationals.student_coutry:form.student_coutry,
        Internationals.student_email:form.student_email,
        Internationals.student_direct:form.student_direct,
        Internationals.student_request:form.student_request,
        Internationals.student_confirm:form.student_confirm,
        Internationals.page:form.page,
        Internationals.status:form.status,

    })
    db.commit()

    return {"data": "Talaba muvaffaqiyatli yangilandi"}



def one_internationals(id,db):
    return db.query(Internationals).filter(Internationals.id==id).first()

def delete_internationals(id,db):
    db.query(Internationals).filter(Internationals.id==id).update({
        Internationals.status:False
    })

    db.commit()
    return {"data":"Malumot o'chirildi"}

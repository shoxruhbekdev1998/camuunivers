from fastapi import HTTPException

from models.for_inquiries import Inquiries
from routes.auth import get_password_hash
from utils.pagination import pagination


def all_inquiries(search, id, from_date, end_date, page, limit, db, status):
    inquiries = db.query(Inquiries).filter(Inquiries.id >= 0)  # Shu yerda 'inquiries' ni aniqlaymiz

    if search:
        inquiries = inquiries.filter(
            Inquiries.student_name.like(f"%{search}%") |
            Inquiries.student_surname.like(f"%{search}%") |
            Inquiries.student_number.like(f"%{search}%")
        )

    if id:
        inquiries = inquiries.filter(Inquiries.id == id)

    if from_date and end_date:
        inquiries = inquiries.filter(Inquiries.date >= from_date, Inquiries.date <= end_date)

    if status is True:
        inquiries = inquiries.filter(Inquiries.status == True)
    elif status is False:
        inquiries = inquiries.filter(Inquiries.status == False)
    else:
        inquiries = inquiries.filter(Inquiries.id >= 0)

    return pagination(form=inquiries, page=page, limit=limit)



def add_inquiries(form,db):
    inquiries = db.query(Inquiries).filter(Inquiries.student_name==form.student_name).first()
    if inquiries:
        raise HTTPException(status_code=400,detail="Bunday nomli foydalanuvchi mavjud qayta kiriting !")
    new_inquiries=Inquiries(student_name=form.student_name,
                            student_surname=form.student_surname,
                            student_number=form.student_number,
                            student_direct=form.student_direct,
                            student_request=form.student_request,
                            student_confirm=form.student_confirm)
    db.add(new_inquiries)
    db.commit()
    db.refresh(new_inquiries)

    return{"data" : "Inquiriens add base"}

def update_inquiries(id,form,db):
    if one_inquiries(id=form.id,db=db) is None:
        raise HTTPException(status_code=400,detail="Bunday raqamli kategoriya2 mavjud emas qayta urining")
    db.query(Inquiries).filter(Inquiries.id==id).update({
        Inquiries.student_name:form.student_name,
        Inquiries.student_surname:form.student_surname,
        Inquiries.student_number:form.student_number,
        Inquiries.student_direct:form.student_direct,
        Inquiries. student_request:form. student_request,
        Inquiries.student_confirm:form.student_confirm,
        Inquiries.status:form.status,

    })
    db.commit()

    return {"data": "Talaba muvaffaqiyatli yangilandi"}



def one_inquiries(id,db):
    return db.query(Inquiries).filter(Inquiries.id==id).first()

def delete_inquiries(id,db):
    db.query(Inquiries).filter(Inquiries.id==id).update({
        Inquiries.status:False
    })

    db.commit()
    return {"data":"Malumot o'chirildi"}

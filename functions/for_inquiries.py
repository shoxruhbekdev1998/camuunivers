from fastapi import HTTPException

from models.for_inquiries import Inquiries
from routes.auth import get_password_hash
from utils.pagination import pagination


def all_inquiries(search,id,from_date,end_date,page,limit,db,status):
    categories2 = db.query(Inquiries).filter(Inquiries.id >= 0)
    if search:
          inquiries = inquiries.filter(Inquiries.student_name.like(search)|
                              Inquiries.student_surname.like(search)|
                              Inquiries.student_number.like(search))

    if id:
        inquiries = inquiries.filter(Inquiries.id==id)


    if from_date and end_date:
        inquiries = inquiries.filter(Inquiries.date >= from_date, Inquiries.date <= end_date)

    if status == True:
     inquiries = inquiries.filter(Inquiries.status==status)

    elif status == False:
     inquiries = inquiries.filter(Inquiries.status==status)

    else:
        inquiries = inquiries.filter(Inquiries.id>=0)

    return pagination(form=inquiries, page=page, limit=limit)



def add_inquiries(form,db):
    inquiries = db.query(Inquiries).filter(Inquiries.student_name==form.student_name).first()
    if inquiries:
        raise HTTPException(status_code=400,detail="Bunday nomli foydalanuvchi mavjud qayta kiriting !")
    new_inquiries=Inquiries(student_name=form.student_name,)
    db.add(new_inquiries)
    db.commit()
    db.refresh(new_inquiries)

    return{"data" : "Inquiriens add base"}

def update_inquiries(id,form,db):
    if one_inquiries(id=form.id,db=db) is None:
        raise HTTPException(status_code=400,detail="Bunday raqamli kategoriya2 mavjud emas qayta urining")
    db.query(Inquiries).filter(Inquiries.id==id).update({
        Inquiries.student_number:form.student_name,
        Inquiries.status:form.status,

    })
    db.commit()



def one_inquiries(id,db):
    return db.query(Inquiries).filter(Inquiries.id==id).first()

def delete_inquiries(id,db):
    db.query(Inquiries).filter(Inquiries.id==id).update({
        Inquiries.status:False
    })

    db.commit()
    return {"data":"Malumot o'chirildi"}

from fastapi import HTTPException

from models.numbers import Numbers
from routes.auth import get_password_hash
from utils.pagination import pagination


def all_numbers(search,id,from_date,end_date,page,limit,db,status):
    number = db.query(Numbers).filter(Numbers.id >= 0)
    if search:
          number = number.filter(Numbers.number_of_buildings.like(search)|
                              Numbers.number_of_specialties.like(search)|
                              Numbers.number_of_students.like(search)|
                              Numbers.number_of_teachers.like(search)|
                              Numbers.number_of_clinics.like(search)|
                              Numbers.number_of_labaratories.like(search))

    if id:
        number = number.filter(Numbers.id==id)


    if from_date and end_date:
        number = number.filter(Numbers.date >= from_date, Numbers.date <= end_date)

    if status == True:
        number = number.filter(Numbers.status==status)

    elif status == False:
        number = number.filter(Numbers.status==status)

    else:
        number = number.filter(Numbers.id>=0)

    return pagination(form=number, page=page, limit=limit)



def add_numbers(form,db):
    new_number=Numbers(number_of_buildings=form.number_of_buildings,)
    db.add(next)
    db.commit()
    db.refresh(new_number)

    return{"data" : "Numbers add base"}

def update_numbers(id,form,db):
    if one_number(id=form.id,db=db) is None:
        raise HTTPException(status_code=400,detail="Bunday raqamli Numbers mavjud emas qayta urining")
    db.query(Numbers).filter(Numbers.id==id).update({
        Numbers.number_of_buildings:form.number_of_buildings,
        Numbers.number_of_specialties:form.number_of_specialties,
        Numbers.number_of_students:form.number_of_students,
        Numbers.number_of_teachers:form.number_of_teachers,
        Numbers.number_of_clinics:form.number_of_clinics,
        Numbers.number_of_labaratories:form.number_of_labaratories,

        Numbers.status:form.status,

    })
    db.commit()



def one_number(id,db):
    return db.query(Numbers).filter(Numbers.id==id).first()

def delete_numbers(id,db):
    db.query(Numbers).filter(Numbers.id==id).update({
        Numbers.status:False
    })

    db.commit()
    return {"data":"Malumot o'chirildi"}

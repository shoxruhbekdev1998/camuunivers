from fastapi import HTTPException
from sqlalchemy.orm import joinedload
from models.categories2 import Categories2
from routes.auth import get_password_hash
from utils.pagination import pagination


def all_categories2(search,id,categor_id,from_date,end_date,page,limit,db,status):
    categories2 = db.query(Categories2).options(joinedload(Categories2.informations2)).filter(Categories2.id >= 0)
    if search:
          categories2 = categories2.filter(Categories2.name_uz.like(search)|
                              Categories2.name_en.like(search)|
                              Categories2.name_ru.like(search))

    if id:
        categories2 = categories2.filter(Categories2.id==id)

    if categor_id:
        categories2 = categories2.filter(Categories2.category_id == categor_id)


    if from_date and end_date:
        categories2 = categories2.filter(Categories2.date >= from_date, Categories2.date <= end_date)

    if status == True:
     categories2 = categories2.filter(Categories2.status==status)

    elif status == False:
     categories2 = categories2.filter(Categories2.status==status)

    else:
        categories2 = categories2.filter(Categories2.id>=0)

    return pagination(form=categories2, page=page, limit=limit)



def add_categories2(form,db):
    category2 = db.query(Categories2).filter(Categories2.name_uz==form.name_uz).first()
    if category2:
        raise HTTPException(status_code=400,detail="Bunday nomli Kategiriya2 mavjud qayta kiriting !")
    new_category2=Categories2(name_uz=form.name_uz,
                              name_en=form.name_en,
                              name_ru=form.name_ru,
                              name_tr=form.name_tr,
                              category_id=form.category_id,)
    db.add(new_category2)
    db.commit()
    db.refresh(new_category2)

    return{"data" : "Category2 add base"}

def update_categories2(id, form, db):
    if one_category2(id=id, db=db) is None:
        raise HTTPException(status_code=404, detail="Bunday raqamli kategoriya2 mavjud emas, qayta urinib ko‘ring!")

    db.query(Categories2).filter(Categories2.id == id).update({
        Categories2.name_uz: form.name_uz,
        Categories2.name_en: form.name_en,
        Categories2.name_ru: form.name_ru,
        Categories2.name_tr: form.name_tr,
        Categories2.category_id: form.category_id,
        Categories2.status: form.status,
    })
    db.commit()

    return {"data": "Kategoriya2 muvaffaqiyatli yangilandi"}



def one_category2(id,db):
    return db.query(Categories2).filter(Categories2.id==id).first()

def delete_categories2(id,db):
    db.query(Categories2).filter(Categories2.id==id).update({
        Categories2.status:False
    })

    db.commit()
    return {"data":"Malumot o'chirildi"}

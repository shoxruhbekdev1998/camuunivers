from fastapi import HTTPException

from models.categories import Categories
from routes.auth import get_password_hash
from utils.pagination import pagination
from sqlalchemy.orm import joinedload

def all_categories(search,id,menu_id,from_date,end_date,page,limit,db,status):
    categories = db.query(Categories).options(joinedload(Categories.category2),joinedload(Categories.information)).filter(Categories.id >= 0)
    if search:
          categories = categories.filter(Categories.name_uz.like(search)|
                              Categories.name_en.like(search)|
                              Categories.name_tr.like(search)|
                              Categories.name_ru.like(search))

    if id:
        categories = categories.filter(Categories.id==id)

    if menu_id:
        categories = categories.filter(Categories.menu_id == menu_id)


    if from_date and end_date:
        categories = categories.filter(Categories.date >= from_date, Categories.date <= end_date)

    if status == True:
     categories = categories.filter(Categories.status==status)

    elif status == False:
     categories = categories.filter(Categories.status==status)

    else:
        categories = categories.filter(Categories.id>=0)

    return pagination(form=categories, page=page, limit=limit)



def add_categories(form,db):
    category = db.query(Categories).filter(Categories.name_uz==form.name_uz).first()
    if category:
        raise HTTPException(status_code=400,detail="Bunday nomli Kategiriya mavjud qayta kiriting !")
    new_category=Categories(name_uz=form.name_uz,
                            name_en=form.name_en,
                            name_ru=form.name_ru,
                            name_tr=form.name_tr,
                            menu_id=form.menu_id,
                            )
    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return{"data" : "Category add base"}

def update_categories(id,form,db):
    if one_category(id=form.id,db=db) is None:
        raise HTTPException(status_code=400,detail="Bunday raqamli kategoriya mavjud emas qayta urining")
    db.query(Categories).filter(Categories.id==id).update({
        Categories.name_uz:form.name_uz,
        Categories.name_en:form.name_en,
        Categories.name_ru:form.name_ru,
        Categories.name_tr:form.name_tr,
        Categories.menu_id:form.menu_id,
        Categories.status:form.status,

    })
    db.commit()



def one_category(id,db):
    return db.query(Categories).filter(Categories.id==id).first()

def delete_categories(id,db):
    db.query(Categories).filter(Categories.id==id).update({
        Categories.status:False
    })

    db.commit()
    return {"data":"Malumot o'chirildi"}

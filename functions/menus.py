from fastapi import HTTPException

from models.menus import Menus
from models.categories import Categories
from routes.auth import get_password_hash
from utils.pagination import pagination
from sqlalchemy.orm import joinedload


def all_menus(search,id,from_date,end_date,page,limit,db,status):
    menus = db.query(Menus).options(joinedload(Menus.category).joinedload(Categories.category2)).filter(Menus.id >= 0)
    if search:
          menus= menus.filter(Menus.name_uz.like(search)|
                              Menus.name_en.like(search)|
                              Menus.name_ru.like(search)|
                              Menus.name_tr.like(search))

    if id:
        menus = menus.filter(Menus.id==id)


    if from_date and end_date:
        menus = menus.filter(Menus.date >= from_date, Menus.date <= end_date)

    if status == True:
     menus = menus.filter(Menus.status==status)

    elif status == False:
     menus = menus.filter(Menus.status==status)

    else:
        menus = menus.filter(Menus.id>=0)

    return pagination(form=menus, page=page, limit=limit)



def add_menus(form, db):
    menu = db.query(Menus).filter(Menus.name_uz == form.name_uz).first()
    if menu:
        raise HTTPException(status_code=400, detail="Bunday nomli menu mavjud, qayta kiriting!")

    new_menu = Menus(
        name_uz=form.name_uz,
        name_en=form.name_en,
        name_ru=form.name_ru,
        name_tr=form.name_tr,
        page=form.page,
    )

    db.add(new_menu)
    db.commit()
    db.refresh(new_menu)

    return {"data": "Menu add base"}


def update_menus(id, form, db):
    menu = one_menu(id=id, db=db)
    if menu is None:
        raise HTTPException(status_code=400, detail="Bunday raqamli menu mavjud emas, qayta urinib ko'ring!")
    
    db.query(Menus).filter(Menus.id == id).update({
        Menus.name_uz: form.name_uz,
        Menus.name_en: form.name_en,
        Menus.name_ru: form.name_ru,
        Menus.name_tr: form.name_tr,
        Menus.page: form.page,
        Menus.status: form.status,
    })
    db.commit()
    return {"data": "Menu muvaffaqiyatli yangilandi"}




def one_menu(id,db):
    return db.query(Menus).filter(Menus.id==id).first()

def delete_menus(id,db):
    db.query(Menus).filter(Menus.id==id).update({
        Menus.status:False
    })

    db.commit()
    return {"data":"Malumot o'chirildi"}

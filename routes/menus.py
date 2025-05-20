from fastapi import APIRouter,Depends,HTTPException
from pydantic.datetime_parse import date

from db import Base,engine,get_db

from sqlalchemy.orm import Session

from routes.auth import get_current_active_user
from schemas.users import UserCurrent

Base.metadata.create_all(bind=engine)
from functions.menus import *
from schemas.menus import *

router_menu = APIRouter()

@router_menu.post('/menu_add_from_admin')
def add_menu(form:MenusCreate,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):

    if add_menus(form=form,db=db):
        raise HTTPException(status_code=200, detail="Amaliyot muvofaqqiyatli bajarildi")


@router_menu.get('/get',status_code=200)
def get_menu(search:str=None,id:int=0,from_date:str=None,end_date:str=None,page:int=1,limit:int=5,status:bool=None,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):

        return all_menus(db=db,status=status,search=search,id=id,from_date=from_date,end_date=end_date,page=page,limit=limit)



@router_menu.put('/menu_update_from_admin',)
def update_menu(form:MenusUpdate,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):

    if update_menus(id=form.id,form=form,db=db):
        raise HTTPException(status_code=200, detail="Amaliyot muvofaqqiyatli bajarildi")

@router_menu.delete('/menu_delete_from_admin',)
def delete_menu(id:int,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):
    return delete_menus(id=id,db=db)



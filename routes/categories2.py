from fastapi import APIRouter,Depends,HTTPException
from pydantic.datetime_parse import date

from db import Base,engine,get_db

from sqlalchemy.orm import Session

from routes.auth import get_current_active_user
from schemas.users import UserCurrent

Base.metadata.create_all(bind=engine)
from functions.categories2 import *
from schemas.categories2 import *

router_category2 = APIRouter()

@router_category2.post('/add')
def add_category2(form:Categories2Create,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):

    if add_categories2(form=form,db=db):
        raise HTTPException(status_code=200, detail="Amaliyot muvofaqqiyatli bajarildi")


@router_category2.get('/',status_code=200)
def get_category2(search:str=None,id:int=0,category_id:int=0,from_date:str=None,end_date:str=None,page:int=1,limit:int=5,status:bool=None,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):

        return all_categories2(db=db,status=status,search=search,id=id,categor_id=category_id,from_date=from_date,end_date=end_date,page=page,limit=limit)



@router_category2.put('/update',)
def update_category2(form:Categories2Update,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):

    if update_categories2(id=form.id,form=form,db=db):
        raise HTTPException(status_code=200, detail="Amaliyot muvofaqqiyatli bajarildi")

@router_category2.delete('/del',)
def delete_category2(id:int,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):
    return delete_categories2(id=id,db=db)



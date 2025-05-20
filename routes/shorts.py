from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import get_db
from schemas.shorts import ShortCreate, ShortUpdate
from routes.auth import get_current_active_user
from schemas.users import UserCurrent
from functions.shorts import add_short, all_shorts, update_short, delete_short

router_shorts = APIRouter()


@router_shorts.post('/short_add_from_admin')
def create_short(
    form: ShortCreate,
    db: Session = Depends(get_db),
    current_user: UserCurrent = Depends(get_current_active_user)
):
    result = add_short(form=form, db=db)
    if result:
        return {"detail": "Short muvaffaqiyatli qo'shildi"}


@router_shorts.get('/get', status_code=200)
def get_shorts(
    search: str = None,
    id: int = 0,
    from_date: str = None,
    end_date: str = None,
    page: int = 1,
    limit: int = 10,
    status: bool = None,
    db: Session = Depends(get_db),
    current_user: UserCurrent = Depends(get_current_active_user)
):
    return all_shorts(
        search=search,
        id=id,
        from_date=from_date,
        end_date=end_date,
        page=page,
        limit=limit,
        status=status,
        db=db
    )


@router_shorts.put('/short_update_from_admin')
def update_short_data(
    form: ShortUpdate,
    db: Session = Depends(get_db),
    current_user: UserCurrent = Depends(get_current_active_user)
):
    if form.id is None:
        raise HTTPException(status_code=400, detail="ID kiritilishi shart!")
    
    result = update_short(id=form.id, form=form, db=db)
    if result:
        return {"detail": "Short muvaffaqiyatli yangilandi"}


@router_shorts.delete('/short_delete_from_admin')
def delete_short_data(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserCurrent = Depends(get_current_active_user)
):
    return delete_short(id=id, db=db)

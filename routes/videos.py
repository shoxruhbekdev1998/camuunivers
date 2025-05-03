from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import get_db
from functions.videos import add_video, all_videos, update_video, delete_video
from schemas.videos import VideoCreate, VideoUpdate
from routes.auth import get_current_active_user
from schemas.users import UserCurrent

router_videos = APIRouter()


@router_videos.post('/add', status_code=201)
def add_video_route(
    form: VideoCreate,
    db: Session = Depends(get_db),
    current_user: UserCurrent = Depends(get_current_active_user)
):
    result = add_video(form=form, db=db)
    if result:
        return {"detail": "Video muvaffaqiyatli qo‘shildi", "id": result["id"]}


@router_videos.get('/', status_code=200)
def get_videos(
    search: str = None,
    id: int = 0,
    from_date: str = None,
    end_date: str = None,
    page: int = 1,
    limit: int = 5,
    status: bool = None,
    db: Session = Depends(get_db),
    current_user: UserCurrent = Depends(get_current_active_user)
):
    return all_videos(
        search=search,
        id=id,
        from_date=from_date,
        end_date=end_date,
        page=page,
        limit=limit,
        status=status,
        db=db
    )


@router_videos.put('/update', status_code=200)
def update_video_route(
    form: VideoUpdate,
    db: Session = Depends(get_db),
    current_user: UserCurrent = Depends(get_current_active_user)
):
    if form.id is None:
        raise HTTPException(status_code=400, detail="ID kiritilishi shart!")
    
    result = update_video(id=form.id, form=form, db=db)
    if result:
        return {"detail": "Video muvaffaqiyatli yangilandi"}


@router_videos.delete('/delete', status_code=200)
def delete_video_route(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserCurrent = Depends(get_current_active_user)
):
    return delete_video(id=id, db=db)

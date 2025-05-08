from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session
from typing import List, Optional
from fastapi import Query

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from db import get_db
from functions.informations2 import get_selected_categories_with_latest_informations

from db import get_db
from schemas.informations2 import Information2Create, Information2Update, Information2Out
from functions.informations2 import (
    create_information2,
    get_all_informations2,
    update_information2,
    delete_information2
)

router_information2 = APIRouter()


@router_information2.post("/", response_model=Information2Out)
async def create_info(
    title_uz: Optional[str] = Form(None),
    information_uz: Optional[str] = Form(None),
    title_ru: Optional[str] = Form(None),
    information_ru: Optional[str] = Form(None),
    title_en: Optional[str] = Form(None),
    information_en: Optional[str] = Form(None),
    title_tr: Optional[str] = Form(None),
    information_tr: Optional[str] = Form(None),
    video_url: Optional[str] = Form(None),
    category2_id : int = Form(None),
    page: Optional[str] = Form(None),
    photo1: Optional[UploadFile] = File(None),
    photo2: Optional[UploadFile] = File(None),
    photo3: Optional[UploadFile] = File(None),
    photo4: Optional[UploadFile] = File(None),
    photo5: Optional[UploadFile] = File(None),
    photo6: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db)
):
    data = Information2Create(
        title_uz=title_uz,
        information_uz=information_uz,
        title_ru=title_ru,
        information_ru=information_ru,
        title_en=title_en,
        information_en=information_en,
        title_tr=title_tr,
        information_tr=information_tr,
        video_url=video_url,
        category2_id=category2_id,
        page=page
    )
    return create_information2(
        db=db,
        data=data,
        files=[photo1, photo2, photo3, photo4, photo5, photo6]
    )



@router_information2.get("/")
def get_all_informations_route2(
    search: str = None,
    id: int = None,
    category2_id : int = None,
    from_date: str = None,
    end_date: str = None,
    page: int = 1,
    limit: int = 10,
    status: bool = None,
    db: Session = Depends(get_db)
):
    return get_all_informations2(
        search=search,
        id=id,
        category2_id=category2_id,
        from_date=from_date,
        end_date=end_date,
        page=page,
        limit=limit,
        db=db,
        status=status
    )





@router_information2.get("/informations2/by-categories")
def get_categories_with_latest_informations_route(
    category_ids: Optional[List[int]] = Query(None),
    search: Optional[str] = None,
    id: Optional[int] = None,
    category_id: Optional[int] = None,
    from_date: Optional[str] = None,
    end_date: Optional[str] = None,
    status: Optional[bool] = None,
    limit: int = 3,
    db: Session = Depends(get_db)
):
    return get_selected_categories_with_latest_informations(
        db=db,
        category_ids=category_ids,
        search=search,
        id=id,
        category_id=category_id,
        from_date=from_date,
        end_date=end_date,
        status=status,
        limit=limit
    )





@router_information2.put("/", response_model=Information2Out)
async def update_info(
    id: int = Form(...),
    status: bool = Form(...),
    title_uz: Optional[str] = Form(None),
    information_uz: Optional[str] = Form(None),
    title_ru: Optional[str] = Form(None),
    information_ru: Optional[str] = Form(None),
    title_en: Optional[str] = Form(None),
    information_en: Optional[str] = Form(None),
    title_tr: Optional[str] = Form(None),
    information_tr: Optional[str] = Form(None),
    video_url: Optional[str] = Form(None),
    category2_id : int = Form(None),
    page: Optional[str] = Form(None),
    photo1: Optional[UploadFile] = File(None),
    photo2: Optional[UploadFile] = File(None),
    photo3: Optional[UploadFile] = File(None),
    photo4: Optional[UploadFile] = File(None),
    photo5: Optional[UploadFile] = File(None),
    photo6: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db)
):
    form = Information2Update(
        status=status,
        title_uz=title_uz,
        information_uz=information_uz,
        title_ru=title_ru,
        information_ru=information_ru,
        title_en=title_en,
        information_en=information_en,
        title_tr=title_tr,
        information_tr=information_tr,
        video_url=video_url,
        category2_id=category2_id,
        page=page
    )
    return update_information2(
        id=id,
        form=form,
        files=[photo1, photo2, photo3, photo4, photo5, photo6],
        db=db
    )



@router_information2.delete("/{info_id}")
def delete_info(info_id: int, db: Session = Depends(get_db)):
    success = delete_information2(db, info_id)
    return {"success": success}

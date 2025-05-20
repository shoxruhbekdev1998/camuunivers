from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session
from typing import List, Optional
from fastapi import Query

from db import get_db
from schemas.informations import InformationCreate, InformationUpdate, InformationOut
from functions.informations import (
    create_information,
    get_all_informations,
    update_information,
    delete_information
)

router_information = APIRouter()


@router_information.post("/information_add_from_admin", response_model=InformationOut)
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
    category_id : int = Form(None),
    page: Optional[str] = Form(None),
    photo1: Optional[UploadFile] = File(None),
    photo2: Optional[UploadFile] = File(None),
    photo3: Optional[UploadFile] = File(None),
    photo4: Optional[UploadFile] = File(None),
    photo5: Optional[UploadFile] = File(None),
    photo6: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db)
):
    data = InformationCreate(
        title_uz=title_uz,
        information_uz=information_uz,
        title_ru=title_ru,
        information_ru=information_ru,
        title_en=title_en,
        information_en=information_en,
        title_tr=title_tr,
        information_tr=information_tr,
        video_url=video_url,
        category_id=category_id,
        page=page
    )
    return create_information(
        db=db,
        data=data,
        files=[photo1, photo2, photo3, photo4, photo5, photo6]
    )



@router_information.get("/get")
def get_all_informations_route(
    search: str = None,
    id: int = None,
    category_id: int = None,
    from_date: str = None,
    end_date: str = None,
    page: int = 1,
    limit: int = 10,
    status: bool = None,
    db: Session = Depends(get_db)
):
    return get_all_informations(
        search=search,
        id=id,
        category_id=category_id,
        from_date=from_date,
        end_date=end_date,
        page=page,
        limit=limit,
        db=db,
        status=status
    )


@router_information.put("/information_update_from_admin", response_model=InformationOut)
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
    category_id : int = Form(None),
    page: Optional[str] = Form(None),
    photo1: Optional[UploadFile] = File(None),
    photo2: Optional[UploadFile] = File(None),
    photo3: Optional[UploadFile] = File(None),
    photo4: Optional[UploadFile] = File(None),
    photo5: Optional[UploadFile] = File(None),
    photo6: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db)
):
    form = InformationUpdate(
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
        category_id=category_id,
        page=page
    )
    return update_information(
        id=id,
        form=form,
        files=[photo1, photo2, photo3, photo4, photo5, photo6],
        db=db
    )


@router_information.delete("/information2_delete_from_admin{info_id}")
def delete_info(info_id: int, db: Session = Depends(get_db)):
    success = delete_information(db, info_id)
    return {"success": success}

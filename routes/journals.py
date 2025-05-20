from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from db import get_db
from schemas.journals import JournalCreate, JournalUpdate, JournalOut
from functions.journals import create_journal, get_all_journals, update_journal, delete_journal

router_journals = APIRouter()

# ✅ CREATE
@router_journals.post("/journal_add_from_admin", response_model=JournalOut)
async def create_journal_route(
    title_uz: str = Form(None),
    description_uz: str = Form(None),
    title_ru: str = Form(None),
    description_ru: str = Form(None),
    title_en: str = Form(None),
    description_en: str = Form(None),
    title_tr: str = Form(None),
    description_tr: str = Form(None),
    category_id: int = Form(None),
    page: Optional[str] = Form(None),
    file: Optional[UploadFile] = File(None),
    image: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db)
):
    data = JournalCreate(
        title_uz=title_uz,
        description_uz=description_uz,
        title_ru=title_ru,
        description_ru=description_ru,
        title_en=title_en,
        description_en=description_en,
        title_tr=title_tr,
        description_tr=description_tr,
        category_id=category_id,
        page=page
    )
    return create_journal(db=db, data=data, file=file, image=image)


# ✅ GET ALL
@router_journals.get("/get")
def get_all_journals_route(
    search: Optional[str] = None,
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return get_all_journals(db=db, search=search, page=page, limit=limit)


# ✅ UPDATE
@router_journals.put("/journal_update_from_admin", response_model=JournalOut)
async def update_journal_route(
    id: int = Form(...),
    title_uz: Optional[str] = Form(None),
    description_uz: Optional[str] = Form(None),
    title_ru: Optional[str] = Form(None),
    description_ru: Optional[str] = Form(None),
    title_en: Optional[str] = Form(None),
    description_en: Optional[str] = Form(None),
    title_tr: Optional[str] = Form(None),
    description_tr: Optional[str] = Form(None),
    file: Optional[UploadFile] = File(None),
    category_id: Optional[int] = Form(None),
    page: Optional[str] = Form(None),
    image: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db)
):
    form = JournalUpdate(
        title_uz=title_uz,
        description_uz=description_uz,
        title_ru=title_ru,
        description_ru=description_ru,
        title_en=title_en,
        description_en=description_en,
        title_tr=title_tr,
        description_tr=description_tr,
        category_id=category_id,
        page=page
    )
    return update_journal(id=id, db=db, form=form, file=file, image=image)


# ✅ DELETE
@router_journals.delete("/journal_delete_from_admin{journal_id}")
def delete_journal_route(journal_id: int, db: Session = Depends(get_db)):
    success = delete_journal(db=db, journal_id=journal_id)
    if not success:
        raise HTTPException(status_code=404, detail="Journal topilmadi.")
    return {"success": True}

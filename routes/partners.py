from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session
from typing import Optional
from fastapi import Query
from db import get_db
from schemas.partners import PartnerCreate, PartnerUpdate, PartnerOut
from functions.partners import (
    create_partner,
    get_all_partners,
    update_partner,
    delete_partner
)

router_partner = APIRouter()


@router_partner.post("/", response_model=PartnerOut)
async def create_partner_route(
    partner_name: str = Form(None),
    partner_link: str = Form(None),
    page: Optional[str] = Form(None),
    status: bool = Form(...),
    partner_logo: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db)
):
    data = PartnerCreate(
        partner_name=partner_name,
        partner_link=partner_link,
        page=page,
        
    )
    return create_partner(db=db, data=data, file=partner_logo)


@router_partner.get("/")
def get_partners_route(
    search: Optional[str] = None,
    status: Optional[bool] = None,
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return get_all_partners(
        db=db,
        search=search,
        status=status,
        page=page,
        limit=limit
    )


@router_partner.put("/", response_model=PartnerOut)
async def update_partner_route(
    id: int = Form(...),
    partner_name: str = Form(None),
    partner_link: str = Form(None),
    page: Optional[str] = Form(None),
   
    partner_logo: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db)
):
    data = PartnerUpdate(
        partner_name=partner_name,
        partner_link=partner_link,
        page=page,
        
    )
    return update_partner(db=db, data=data, partner_id=id, file=partner_logo)


@router_partner.delete("/{partner_id}")
def delete_partner_route(partner_id: int, db: Session = Depends(get_db)):
    success = delete_partner(db=db, partner_id=partner_id)
    return {"success": success}

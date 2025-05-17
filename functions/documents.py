from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.documents import Documents
from schemas.documents import DocumentBase, DocumentCreate, DocumentUpdate
from utils.pagination import pagination

# All documents with search, date filtering, and status
def all_documents(search: str, id: int, from_date, end_date, page: int, limit: int, db: Session, status: bool):
    documents = db.query(Documents).filter(Documents.id >= 0)

    if search:
        documents = documents.filter(
            Documents.student_name.like(f"%{search}%") |
            Documents.student_surname.like(f"%{search}%") |
            Documents.student_number1.like(f"%{search}%")
        )

    if id:
        documents = documents.filter(Documents.id == id)

    if from_date and end_date:
        documents = documents.filter(Documents.date >= from_date, Documents.date <= end_date)

    if status is True:
        documents = documents.filter(Documents.status == True)
    elif status is False:
        documents = documents.filter(Documents.status == False)
    else:
        documents = documents.filter(Documents.id >= 0)

    return pagination(form=documents, page=page, limit=limit)

# Add a new document
def add_document(form,db):
    check = db.query(Documents).filter(DocumentBase.card_pnfl == form.card_pnfl).first()
    if check:
        raise HTTPException(status_code=400, detail="Bunday foydalanuvchi allaqachon mavjud!")

    new_document = Documents(
        student_name=form.student_name,
        student_surname=form.student_surname,
        student_middle_name=form.student_middle_name,
        student_region=form.student_region,
        student_city=form.student_city,
        student_village=form.student_village,
        number_school=form.number_school,
        student_number1=form.student_number1,
        student_number2=form.student_number2,
        student_confirm=form.student_confirm,
        
        student_direct=form.student_direct,
        student_request=form.student_request,
       
    )
    db.add(new_document)
    db.commit()
    db.refresh(new_document)

    return {"data": "Abituryent muvaffaqiyatli ro'yhatdan o'tdi"}

# Update an existing document
def update_document(id, form, db):
    document = one_document(id=form.id, db=db)
    if not document:
        raise HTTPException(status_code=404, detail="Bunday raqamli abituryent mavjud emas qayta urining")

    db.query(Documents).filter(Documents.id == id).update({
        Documents.student_name: form.student_name,
        Documents.student_surname: form.student_surname,
        Documents.student_middle_name: form.student_middle_name,
        Documents.student_region: form.student_region,
        Documents.student_city: form.student_city,
        Documents.student_village: form.student_village,
        Documents.number_school: form.number_school,
        Documents.student_number1: form.student_number1,
        Documents.student_number2: form.student_number2,
        Documents.student_confirm: form.student_confirm,
        Documents.status: form.status
    })
    db.commit()
    return {"data": "Abituryent yangilandi"}

# Get a single document by ID
def one_document(id: int, db: Session):
    return db.query(Documents).filter(Documents.id == id).first()

# Soft delete a document (set status to False)
def delete_document(id,db):
    db.query(Documents).filter(Documents.id==id).update({
        Documents.status:False
    })

    db.commit()
    return {"data":"Malumot o'chirildi"}

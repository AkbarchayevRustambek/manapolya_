from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import Optional
import shutil, os, uuid
from database import get_db
from models.field import Field

router = APIRouter(prefix="/api/fields", tags=["fields"])

UPLOAD_DIR = "static/images/fields"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.get("/")
def get_fields(district: Optional[str] = None, db: Session = Depends(get_db)):
    q = db.query(Field).filter(Field.is_active == True)
    if district and district != "all":
        q = q.filter(Field.district == district)
    return q.all()

@router.get("/{field_id}")
def get_field(field_id: int, db: Session = Depends(get_db)):
    field = db.query(Field).filter(Field.id == field_id).first()
    if not field:
        raise HTTPException(status_code=404, detail="Polya topilmadi")
    return field

@router.post("/")
async def create_field(
    name: str = Form(...),
    price_per_hour: float = Form(...),
    description: str = Form(""),
    district: str = Form(""),
    image: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db)
):
    image_url = ""
    if image and image.filename:
        ext = os.path.splitext(image.filename)[1]
        fname = f"{uuid.uuid4().hex}{ext}"
        fpath = os.path.join(UPLOAD_DIR, fname)
        with open(fpath, "wb") as f:
            shutil.copyfileobj(image.file, f)
        image_url = f"/static/images/fields/{fname}"

    field = Field(
        name=name,
        price_per_hour=price_per_hour,
        description=description,
        district=district,
        image_url=image_url
    )
    db.add(field)
    db.commit()
    db.refresh(field)
    return field

@router.delete("/{field_id}")
def delete_field(field_id: int, db: Session = Depends(get_db)):
    field = db.query(Field).filter(Field.id == field_id).first()
    if not field:
        raise HTTPException(status_code=404, detail="Polya topilmadi")
    field.is_active = False
    db.commit()
    return {"message": "Polya o'chirildi"}

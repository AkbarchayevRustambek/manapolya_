from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import datetime
from database import get_db
from models.booking import Booking
from models.field import Field

router = APIRouter(prefix="/api/bookings", tags=["bookings"])

class BookingCreate(BaseModel):
    field_id: int
    user_name: str
    user_phone: str
    start_time: datetime
    end_time: datetime

def is_available(field_id, start, end, db):
    conflict = db.query(Booking).filter(
        Booking.field_id == field_id,
        Booking.status != "cancelled",
        Booking.start_time < end,
        Booking.end_time > start
    ).first()
    return conflict is None

@router.get("/")
def get_bookings(db: Session = Depends(get_db)):
    return db.query(Booking).order_by(Booking.created_at.desc()).all()

@router.post("/")
def create_booking(data: BookingCreate, db: Session = Depends(get_db)):
    field = db.query(Field).filter(Field.id == data.field_id).first()
    if not field:
        raise HTTPException(status_code=404, detail="Polya topilmadi")
    if not is_available(data.field_id, data.start_time, data.end_time, db):
        raise HTTPException(status_code=400, detail="Bu vaqt band!")
    hours = (data.end_time - data.start_time).seconds / 3600
    booking = Booking(
        field_id=data.field_id,
        user_name=data.user_name,
        user_phone=data.user_phone,
        start_time=data.start_time,
        end_time=data.end_time,
        total_price=field.price_per_hour * hours,
        status="confirmed",
        created_at=datetime.now()
    )
    db.add(booking)
    db.commit()
    db.refresh(booking)
    return booking

@router.delete("/{booking_id}")
def cancel_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Bron topilmadi")
    booking.status = "cancelled"
    db.commit()
    return {"message": "Bron bekor qilindi"}

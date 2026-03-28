from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.booking import Booking

router = APIRouter(prefix="/api/admin", tags=["admin"])

@router.get("/bookings")
def get_all_bookings(db: Session = Depends(get_db)):
    return db.query(Booking).order_by(Booking.created_at.desc()).all()

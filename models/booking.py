from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Booking(Base):
    __tablename__ = "bookings"
    id          = Column(Integer, primary_key=True, index=True)
    field_id    = Column(Integer, ForeignKey("fields.id"), nullable=False)
    user_name   = Column(String, nullable=False)
    user_phone  = Column(String, nullable=False)
    start_time  = Column(DateTime, nullable=False)
    end_time    = Column(DateTime, nullable=False)
    total_price = Column(Float)
    status      = Column(String, default="confirmed")
    created_at  = Column(DateTime)
    field       = relationship("Field")

from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base

class Field(Base):
    __tablename__ = "fields"
    id             = Column(Integer, primary_key=True, index=True)
    name           = Column(String, nullable=False)
    description    = Column(String, default="")   # manzil
    district       = Column(String, default="")   # tuman
    price_per_hour = Column(Float, nullable=False)
    image_url      = Column(String, default="")
    is_active      = Column(Boolean, default=True)

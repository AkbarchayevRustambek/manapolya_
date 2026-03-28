import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from dotenv import load_dotenv

# .env faylini yuklash
load_dotenv()

# Ma'lumotlar bazasi URL manzilini olish
DATABASE_URL = os.getenv("DATABASE_URL")

# Agar DATABASE_URL topilmasa, xatolik berish
if not DATABASE_URL:
    raise ValueError("DATABASE_URL .env faylida topilmadi! Iltimos, .env faylini tekshiring.")

# Engine yaratish
# Agar PostgreSQL bo'lsa, oddiy ulanish, SQLite bo'lsa check_same_thread kerak
if DATABASE_URL.startswith("postgresql"):
    engine = create_engine(DATABASE_URL)
else:
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# 1. SessionLocal ni aniqlash (BU JUDA MUHIM!)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 2. Base klassini yaratish
class Base(DeclarativeBase):
    pass

# 3. get_db funksiyasi
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


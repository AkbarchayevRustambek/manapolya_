"""
Ishga tushirish: python seed.py
6 ta demo polyani qo'shadi (rasmlar bilan)
"""
from database import engine, Base, SessionLocal
from models.field import Field

Base.metadata.create_all(bind=engine)
db = SessionLocal()

if db.query(Field).count() == 0:
    fields = [
        Field(name="Beshqozon Arena", description="Toshkent, Amir Temur shoh ko'chasi, 5A",
              district="chilonzor", price_per_hour=100000,
              image_url="/static/images/fields/field1.jpg"),
        Field(name="Yunusobod Sport", description="Toshkent, Amir Temur shoh, 108A",
              district="yunusobod", price_per_hour=100000,
              image_url="/static/images/fields/field2.jpg"),
        Field(name="Rona Fields", description="Toshkent, Amir Temur shoh 105A",
              district="mirzo", price_per_hour=200000,
              image_url="/static/images/fields/field3.jpg"),
        Field(name="Green Park", description="Toshkent, Shayxontohur, Ko'yluk 12",
              district="shayxontohur", price_per_hour=120000,
              image_url="/static/images/fields/field4.jpg"),
        Field(name="Pro Soccer Olmazar", description="Toshkent, Olmazor tumani, 7-mavze",
              district="olmazar", price_per_hour=150000,
              image_url="/static/images/fields/field5.jpg"),
        Field(name="City Sport Uchtepa", description="Toshkent, Uchtepa tumani, Yangi hayot ko'chasi",
              district="uchtepa", price_per_hour=90000,
              image_url="/static/images/fields/field6.jpg"),
    ]
    db.add_all(fields)
    db.commit()
    print(f"✅ {len(fields)} ta polya qo'shildi!")
else:
    print("ℹ️ Polyalar allaqachon mavjud")
db.close()

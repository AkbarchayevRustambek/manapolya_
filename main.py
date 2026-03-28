from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from database import engine, Base
import models
import os

from routes import fields, bookings, admin

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mana Polya Bron Tizimi")

# Vercel uchun to'liq yo'l
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

app.include_router(fields.router)
app.include_router(bookings.router)
app.include_router(admin.router)

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/bron/{field_id}")
def booking_page(field_id: int, request: Request):
    return templates.TemplateResponse("booking.html", {"request": request, "field_id": field_id})

@app.get("/admin")
def admin_page(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})

@app.get("/haqimizda")
def about_page(request: Request):
    return templates.TemplateResponse("haqimizda.html", {"request": request})

@app.get("/hamkorlar")
def partners_page(request: Request):
    return templates.TemplateResponse("hamkorlar.html", {"request": request})

@app.get("/kontakt")
def contact_page(request: Request):
    return templates.TemplateResponse("kontakt.html", {"request": request})
if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
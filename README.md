# ManaPolya Bron Tizimi

## O'rnatish va Ishga Tushirish

```bash
# 1. Papkaga kiring
cd bron-loyiha

# 2. Virtual muhit yarating
python -m venv venv
venv\Scripts\activate

# 3. Kutubxonalarni o'rnating
pip install -r requirements.txt

# 4. Serverni ishga tushiring
uvicorn main:app --reload
```

## Sahifalar
- http://localhost:8000          — Bosh sahifa
- http://localhost:8000/admin    — Admin panel (polya qo'shish, bronlar)
- http://localhost:8000/docs     — API dokumentatsiya

## Ishlatish tartibi
1. /admin ga kiring
2. "Polya Qo'shish" bo'limidan polya qo'shing
3. Bosh sahifaga qayting
4. Polya ustidan "Bron qilish" tugmasini bosing

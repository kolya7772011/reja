# Reja - Django Project

Bu Django loyihasi Reja loyihasining asosiy qismidir.

## O'rnatish

### 1. Virtual Environment yaratish
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# yoki
venv\Scripts\activate  # Windows
```

### 2. Dependencylarni o'rnatish
```bash
pip install -r requirements.txt
```

### 3. Environment o'zgaruvchilarini sozlash
```bash
cp .env.example .env
# .env faylini o'z parametrlaringiz bilan tahrirlang
```

### 4. Database migratsiyalarini bajarish
```bash
python manage.py migrate
```

### 5. Superuser yaratish (admin uchun)
```bash
python manage.py createsuperuser
```

### 6. Loyihani ishga tushirish
```bash
python manage.py runserver
```

Server `http://localhost:8000` da ishga tushadi.

## Admin panel
Admin panelga kirish: `http://localhost:8000/admin/`

## Loyiha Strukturasi
```
reja/
├── reja/                 # Asosiy loyiha konfiguratsiyasi
│   ├── settings.py      # Django sozlamalari
│   ├── urls.py          # URL yo'naltirish
│   ├── wsgi.py          # WSGI konfiguratsiyasi
│   └── __init__.py
├── manage.py            # Django CLI
├── requirements.txt     # Dependencylar
├── .env.example         # Environment o'zgaruvchilarining namunasi
├── .gitignore           # Git ignore fayllar
└── README.md           # Bu fayl
```

## Yangi App yaratish
```bash
python manage.py startapp app_name
```

So'ng `settings.py` da `INSTALLED_APPS` ga qo'shing:
```python
INSTALLED_APPS = [
    ...
    'app_name',
]
```

## License
MIT License

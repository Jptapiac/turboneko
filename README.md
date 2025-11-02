turboneko
=========

Instrucciones rápidas para desarrollar localmente:

Requisitos
- Python 3.8+ (recomendado usar virtualenv/venv)
- pip

Instalación

1. Crear y activar el entorno virtual (Windows PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Instalar dependencias:

```powershell
pip install -r requirements.txt
```

Nota: si no existe `requirements.txt` puedes instalar: `django django-crispy-forms crispy-bootstrap4`.

Configuración y migraciones

```powershell
python manage.py makemigrations
python manage.py migrate
```

Crear usuario admin

```powershell
python manage.py createsuperuser
```

Datos de ejemplo

Hay un comando para generar datos de ejemplo (categorías, fabricantes y animatronics):

```powershell
python manage.py seed_data
```

Levantar servidor de desarrollo

```powershell
python manage.py runserver
```

Rutas útiles
- / -> Home
- /animatronics/ -> Lista de animatronics (paginada)
- /contacto/ -> Formulario de contacto (app `contract`)

Tests

```powershell
python manage.py test
```

Notas
- Plantilla 404 personalizada en `templates/404.html`.
- Formulario de contacto implementado en la app `contract` (modelo `Contact`).

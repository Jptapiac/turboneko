
"""
Configuración WSGI para turboneko.
"""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'turboneko.settings')
application = get_wsgi_application()


#!/usr/bin/env python
"""Script de administración de Django."""
import os
import sys

def main():
    """Punto de entrada del CLI de Django."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'turboneko.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "No se pudo importar Django. ¿Está instalado y disponible en tu entorno?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()

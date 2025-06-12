"""
ASGI config for LOGIKA_DJANGO_ORM_FIRT_CODE project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LOGIKA_DJANGO_ORM_FIRT_CODE.settings')

application = get_asgi_application()

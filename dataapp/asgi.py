"""
ASGI config for dataapp project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dataapp.settings')

application = get_asgi_application()

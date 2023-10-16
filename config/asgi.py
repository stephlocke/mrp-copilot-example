"""
ASGI config for manufacturing-rp-saas project.

It exposes the ASGI application module named ``application`` to the world.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_asgi_application()
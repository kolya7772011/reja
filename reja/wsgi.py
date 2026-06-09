"""
WSGI config for reja project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reja.settings')

application = get_wsgi_application()

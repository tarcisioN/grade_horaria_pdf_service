"""
WSGI config for grade_horaria_pdf_service_admin_allowed project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "grade_horaria_pdf_service_admin_allowed.settings")

application = get_wsgi_application()

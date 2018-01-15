#!/usr/bin/env python
import os
import sys

#manage.py drf_create_token admin
#manage.py createsuperuser

#admin admin123
#68f1b119a79d9461675c8060b1ba40ce195c0f18

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "grade_horaria_pdf_service_admin_allowed.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

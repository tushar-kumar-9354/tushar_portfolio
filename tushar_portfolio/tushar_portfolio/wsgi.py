"""
WSGI config for tushar_portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

print("THIS IS MY WSGI.PY folder 00")
import os
print("THIS IS MY WSGI.PY folder 01 and error comes after this line")
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tushar_portfolio.settings')

application = get_wsgi_application()


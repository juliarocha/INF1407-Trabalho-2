"""
WSGI config for Project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys

# assuming your django settings file is at '/home/juliarocha/mysite/mysite/settings.py'
# and your manage.py is is at '/home/juliarocha/mysite/manage.py'
path = '/home/juliarocha/mysite'
if path not in sys.path:
   sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

# then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
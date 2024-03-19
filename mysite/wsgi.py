import os
import sys

path = '/home/ZmiievskaIra/Django-blog'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

application = get_wsgi_application()
application = WhiteNoise(application)
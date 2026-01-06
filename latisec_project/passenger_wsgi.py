import os
import sys

# Add your project directory to sys.path
project_home = '/home/latisecc/test.latisec.com/latisec_project'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'latisec_project.settings'

# Activate the virtual environment (note the 3.8 subfolder)
INTERP = '/home/latisecc/virtualenv/test.latisec.com/latisec_project/3.8/bin/python'
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

# Get Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
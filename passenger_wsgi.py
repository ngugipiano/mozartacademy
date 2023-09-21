import imp
import os
from run import app as application

wsgi = imp.load_source('wsgi', 'run.py')
application = wsgi.app

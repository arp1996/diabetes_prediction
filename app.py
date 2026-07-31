import os
import sys

# Add the project root to the path
sys.path.insert(0, os.path.dirname(__file__))

# Set the default Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "heartdisease.settings")

# Import and use the actual WSGI application
from heartdisease.wsgi import application

# Alias so 'gunicorn app:app' works (Render's default detection)
app = application

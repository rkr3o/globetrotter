# Set up Django environment
import os
import sys
import django

# Add the project root to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
django.setup()

from apps.db_manager.models import User

def list_destinations():
    destinations = User.objects.all()
    for dest in destinations:
        print(dest.name)

if __name__ == "__main__":
    list_destinations()

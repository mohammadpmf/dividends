import os
import threading
import webbrowser
from django.core.management import execute_from_command_line
import time

def run_django():
    """Run Django development server"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    time.sleep(2)
    webbrowser.open('http://127.0.0.1:8024')
    execute_from_command_line(['manage.py', 'runserver', '127.0.0.1:8024', '--noreload'])

if __name__ == '__main__':
    django_thread = threading.Thread(target=run_django)
    django_thread.daemon = True
    django_thread.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down...")

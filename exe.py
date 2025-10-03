import os
import sys


def run():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    from django.core.management import execute_from_command_line

    sys.argv = ["manage.py", "runserver", "127.0.0.1:8024"]
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    run()

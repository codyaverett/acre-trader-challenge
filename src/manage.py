#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import sys
from os import path, environ
from dotenv import read_dotenv


def main():
    """Run administrative tasks."""

    # Load dotenv file from the project root directory
    dotenv_file = path.join(path.join(path.dirname(__file__), '.env'))
    read_dotenv(dotenv_file, override=True)

    environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

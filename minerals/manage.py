#!/usr/bin/python
import os
import sys
# import exceptions

# ! run with python3 !


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'minerals.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and " +
            "available on your PYTHONPATH environment variable? Did you " +
            "forget to activate a virtual environment?"
        )(exc)
    execute_from_command_line(sys.argv)


#  TODO: latest todo is why detail page doesn't work

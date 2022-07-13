"""
Django command to wait for db to be available
"""

import time

from django.core.management.base import BaseCommand

from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django command to wait for database"""

    def handle(self, *args, **options):
        """entry point from command"""
        self.stdout.write('Waiting for Database..')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write(
                    'Database Unavailable, Waiting ofr 1 sec ...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))

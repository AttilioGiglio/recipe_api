# default python module for sleep app for few seconds
import time
# used to know the database connection is available
from django.db import connections
# to know if the db connection is no available
from django.db.utils import OperationalError
# to create the custom command
from django.core.management import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until db is available"""

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Database unvailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('DB available!'))

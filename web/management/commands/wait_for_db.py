import time
from typing import Any, Optional

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from psycopg2 import OperationalError as PscopgError


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> str | None:
        self.stdout.write("Waiting for database...")
        database_up = False
        while database_up is False:
            try:
                self.check(databases=["default"])
                database_up = True
            except (PscopgError, OperationalError):
                self.stdout.write("Database unavailable, waiting 1 secs...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Data available!"))

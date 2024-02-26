from typing import Any
import random
from django.core.management.base import BaseCommand, CommandParser
from rooms.models import Facility
from ..utils.helpers import seed_obj


class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--number",
            help="Number of facilities that you want to seed. Passing '-1' value to seed all",
        )

    def handle(self, *args: Any, **options: Any) -> str | None:
        facilities = [
            "Free parking on premises",
            "Private pool",
            "Single level home",
        ]
        num_of_facilities = options.get("number")
        num_of_facilities = int(num_of_facilities)

        log_level, msg = seed_obj(Facility, facilities, num_of_facilities)

        if log_level == "SUCCESS":
            self.stdout.write(self.style.SUCCESS(msg))
        elif log_level == "ERROR":
            self.stdout.write(self.style.ERROR(msg))

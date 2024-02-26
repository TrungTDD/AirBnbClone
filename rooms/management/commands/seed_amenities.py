from typing import Any
import random
from django.core.management.base import BaseCommand, CommandParser
from rooms.models import Amenity
from ..utils.helpers import seed_obj


class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--number",
            help="Number of amenities that you want to seed. Passing '-1' value to seed all",
        )

    def handle(self, *args: Any, **options: Any) -> str | None:
        amenities = [
            "Wifi",
            "Kitchen",
            "Washer",
            "Dryer",
            "Air conditioning",
            "Heating",
            "Dedicated workspace",
            "TV",
            "Hair dryer",
            "Iron",
            "Pool",
            "Hot tub",
            "Free parking",
            "EV charger",
            "Crib",
            "King bed",
            "Gym",
            "BBQ grill",
            "Breakfast",
            "Indoor fireplace",
            "Smoking allowed",
            "Beachfront",
            "Waterfront",
            "Smoke alarm",
            "Carbon monoxide alarm",
        ]
        num_of_amenities = options.get("number")
        num_of_amenities = int(num_of_amenities)

        log_level, msg = seed_obj(Amenity, amenities, num_of_amenities)

        if log_level == "SUCCESS":
            self.stdout.write(self.style.SUCCESS(msg))
        elif log_level == "ERROR":
            self.stdout.write(self.style.ERROR(msg))

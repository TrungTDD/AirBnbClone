import random
from typing import Any
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand, CommandParser
from django_seed import Seed
from reservations.models import Reservation
from users.models import User
from rooms.models import Room


class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="How many reservations that you want to create",
        )

    def handle(self, *args: Any, **options: Any) -> str | None:
        number = options.get("number")
        seeder = Seed.seeder()
        rooms = Room.objects.all()
        users = User.objects.all()

        seeder.add_entity(
            Reservation,
            number,
            {
                "guest": lambda x: random.choice(users),
                "room": lambda x: random.choice(rooms),
                "check_in": lambda x: datetime.now() - timedelta(days=random.randint(0, 5)),
                "check_out": lambda x: datetime.now()
                + timedelta(days=random.randint(1, 10)),
            },
        )

        seeder.execute()

        self.stdout.write(
            self.style.SUCCESS(f"Create {number} reservations successfully")
        )

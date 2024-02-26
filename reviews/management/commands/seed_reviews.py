from typing import Any
import random
from django.core.management.base import BaseCommand, CommandParser
from django_seed import Seed
from reviews.models import Review
from users.models import User
from rooms.models import Room


class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--number",
            type=int,
            default=1,
            help="How many reviews that you want to create",
        )

    def handle(self, *args: Any, **options: Any) -> str | None:
        number = options.get("number")
        users = User.objects.all()
        rooms = Room.objects.all()
        seeder = Seed.seeder()
        seeder.add_entity(
            Review,
            number,
            {
                "accuracy": lambda x: random.randint(1, 5),
                "communication": lambda x: random.randint(1, 5),
                "cleanliness": lambda x: random.randint(1, 5),
                "location": lambda x: random.randint(1, 5),
                "check_in": lambda x: random.randint(1, 5),
                "value": lambda x: random.randint(1, 5),
                "user": lambda x: random.choice(users),
                "room": lambda x: random.choice(rooms),
            },
        )

        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"Create {number} reviews successfully"))

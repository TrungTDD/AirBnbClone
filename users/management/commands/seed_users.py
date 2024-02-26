from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from django_seed import Seed
from users.models import User


class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--number",
            type=int,
            help="Number of users that you want to create",
        )

    def handle(self, *args: Any, **options: Any) -> str | None:
        number = options.get("number", 1)
        seeder = Seed.seeder()
        seeder.add_entity(User, number, {"is_staff": False, "is_superuser": False})
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"Create {number} successfully"))

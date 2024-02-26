import random
from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from django_seed import Seed
from wishlists.models import Wishlist
from users.models import User
from rooms.models import Room


class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--number",
            type=int,
            default=1,
            help="How many wishlists that you want to create",
        )

    def handle(self, *args: Any, **options: Any) -> str | None:
        number = options.get("number")
        seeder = Seed.seeder()
        users = User.objects.all()
        rooms = Room.objects.all()

        seeder.add_entity(
            Wishlist,
            number,
            {
                "user": lambda x: random.choice(users),
            },
        )

        inserted_pks = seeder.execute()
        pks = list(inserted_pks.values())[0]

        for pk in pks:
            wishlist = Wishlist.objects.get(pk=pk)
            for _ in range(random.randint(1, 10)):
                wishlist.rooms.add(random.choice(rooms))
    
        self.stdout.write(self.style.SUCCESS(f"Create {number} wishlists successfully"))

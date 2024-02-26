import random
from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from django_seed import Seed
from rooms.models import Room, Amenity, Facility, Rule, RoomType, Photo
from users.models import User


class Command(BaseCommand):
    """Seed rooms"""

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="How many numbers that you want to create",
        )

    def handle(self, *args: Any, **options: Any) -> str | None:
        number = options.get("number")

        users = User.objects.all()
        room_types = RoomType.objects.all()
        amenities = Amenity.objects.all()
        facilities = Facility.objects.all()
        rules = Rule.objects.all()

        seeder = Seed.seeder()
        seeder.add_entity(
            Room,
            number,
            {
                "city": lambda x: seeder.faker.city(),
                "address": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(users),
                "room_type": lambda x: random.choice(room_types),
                "beds": lambda x: random.randint(1, 10),
                "price": lambda x: random.randint(1, 1000000) / 100,
                "baths": lambda x: random.randint(1, 6),
                "bedrooms": lambda x: random.randint(1, 6),
                "guests": lambda x: random.randint(1, 10),
            },
        )
        pk_inserted = seeder.execute()
        room_pks = list(pk_inserted.values())[0]
        for pk in room_pks:
            room = Room.objects.get(pk=pk)
            for _ in range(random.randint(0, 10)):
                Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    image_file=f"room_photos/{random.randint(0, 20)}.jpg",
                )

            amenity_random = random.randint(1, 10)
            for _ in range(amenity_random):
                room.amenities.add(random.choice(amenities))

            facility_random = random.randint(1, 4)
            for _ in range(facility_random):
                room.facilities.add(random.choice(facilities))

            rule_random = random.randint(1, 5)
            for _ in range(rule_random):
                room.rules.add(random.choice(rules))

        self.stdout.write(self.style.SUCCESS(f"Create {number} rooms successfully"))

from typing import Any
import random
from django.core.management.base import BaseCommand, CommandParser
from rooms.models import Rule
from ..utils.helpers import seed_obj


class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--number",
            help="Number of rules that you want to seed. Passing '-1' value to seed all",
        )

    def handle(self, *args: Any, **options: Any) -> str | None:
        rules = [
            "Pets allowed",
            "No parties or events",
            "No commercial photography",
            "Smoking is allowed",
        ]
        num_of_rules = options.get("number")
        num_of_rules = int(num_of_rules)

        log_level, msg = seed_obj(Rule, rules, num_of_rules)

        if log_level == "SUCCESS":
            self.stdout.write(self.style.SUCCESS(msg))
        elif log_level == "ERROR":
            self.stdout.write(self.style.ERROR(msg))

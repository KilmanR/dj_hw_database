import csv
import os
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        csv_file_path = os.path.join(
            os.path.dirname(__file__), "../../../phones.csv"
        )

        with open(csv_file_path, "r", encoding="utf-8") as file:
            phones = list(csv.DictReader(file, delimiter=";"))

        for phone in phones:
            Phone.objects.create(
                id=int(phone["id"]),
                name=phone["name"],
                image=phone["image"],
                price=int(phone["price"]),
                release_date=phone["release_date"],
                lte_exists=phone["lte_exists"].strip().lower() == "true",
                slug=slugify(phone["name"]),
            )

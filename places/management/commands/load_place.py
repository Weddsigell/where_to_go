import requests
from django.core.management.base import BaseCommand
from places.models import Image, Place
from pathlib import Path
from django.core.files.base import ContentFile


class Command(BaseCommand):
    def add_arguments(self, parser):

        parser.add_argument(
            'url',
            type=str,
            help = 'url к json',
        )


    def handle(self, *args, **options):
        response = requests.get(options["url"])
        response.raise_for_status()
        data = response.json()

        title = data['title']
        description_short = data['description_short']
        description_long = data['description_long']
        lng = data['coordinates']['lng']
        lat = data['coordinates']['lat']

        place, obj = Place.objects.get_or_create(
            title=title, 
            description_short=description_short, 
            description_long=description_long, 
            lng=lng, 
            lat=lat,
        )

        for img in data['imgs']:
            filename = Path(img).name
            content = get_image(img)
            image = Image.objects.create(
                place=place,
                image=ContentFile(content, name=filename)
            )


def get_image(url):
        response = requests.get(url)
        response.raise_for_status()
        return response.content

from random import choice, randint
from django.core.management.base import BaseCommand, CommandError
from benefit.models import Artwork
import names

class Command(BaseCommand):
    help = "create sample data for testing"

    def handle(self, *args, **options):
        MEDIA = ("oil on paper", "watercolor on paper", "steel", "c-print", "digital print")
        for x in range(0,100):
            artwork = Artwork(
                title=names.get_full_name(),
                artist_first_name=names.get_first_name(),
                artist_last_name=names.get_last_name(),
                work_year = randint(2012, 2014),
                size = "%d x %d inches" % (randint(8, 15), randint(8, 15)),
                medium = choice(MEDIA),
                # assumes images are already in media directory"
                image = "images/IMG_0%d.JPG" % randint(241, 250),
            )
            artwork.save()


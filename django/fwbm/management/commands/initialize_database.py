from django.core.management.base import BaseCommand
from django_scripts_tracker.core_tracker import tracked_script

from fwbm.models import Blog

class Command(BaseCommand):
    help = 'Initialize database'
    
    @tracked_script
    def handle(self, *args, **options):
        b = Blog(name='Some name', tagline='Some tagline')
        b.save()
        self.stdout.write('Database initialized')
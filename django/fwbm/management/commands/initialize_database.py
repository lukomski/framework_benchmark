from django.core.management.base import BaseCommand
from django_scripts_tracker.core_tracker import tracked_script

from fwbm.models import Blog

class Command(BaseCommand):
    help = 'Initialize database'
    
    @tracked_script
    def handle(self, *args, **options):
        for idx in range(1000):
            b = Blog(name=f'Some name {idx}', tagline='Some tagline {idx}')
            b.save()
        self.stdout.write(f'Count of Blogs: {Blog.objects.count()}')
        self.stdout.write('Database initialized')
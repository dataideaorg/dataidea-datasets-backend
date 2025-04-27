import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Creates a superuser automatically from environment variables'

    def handle(self, *args, **options):
        admin_username = os.environ.get('SUPERUSER_USERNAME')
        admin_email = os.environ.get('SUPERUSER_EMAIL')
        admin_password = os.environ.get('SUPERUSER_PASSWORD')

        if not all([admin_username, admin_email, admin_password]):
            self.stdout.write(self.style.ERROR(
                'Environment variables SUPERUSER_USERNAME, SUPERUSER_EMAIL, and '
                'SUPERUSER_PASSWORD must be set'
            ))
            return

        if User.objects.filter(username=admin_username).exists():
            self.stdout.write(self.style.WARNING(f'Superuser {admin_username} already exists'))
            return

        User.objects.create_superuser(
            username=admin_username,
            email=admin_email,
            password=admin_password
        )

        self.stdout.write(self.style.SUCCESS(f'Superuser {admin_username} created successfully')) 
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.core.management import call_command


@receiver(post_migrate)
def populate_initial_data(sender, **kwargs):
    """
    Automatically populate database with initial datasets after migrations.
    This runs after every migration, but the populate_datasets command
    is idempotent (won't create duplicates).
    """
    if sender.name == 'datasets':
        print("\n🔄 Running post-migration data population...")
        try:
            call_command('populate_datasets')
            print("✅ Post-migration data population completed!\n")
        except Exception as e:
            print(f"⚠️  Warning: Could not populate datasets: {e}\n")
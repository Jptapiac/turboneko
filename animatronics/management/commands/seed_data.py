from django.core.management.base import BaseCommand
from animatronics.models import Category, Manufacturer, Animatronic

class Command(BaseCommand):
    help = 'Seed the database with example categories, manufacturers and animatronics'

    def handle(self, *args, **options):
        # Categories
        cats = ['Animales', 'Personajes', 'Robots']
        for c in cats:
            Category.objects.get_or_create(name=c, defaults={'description': f'Categoría {c}'})

        # Manufacturers
        makers = [
            ('TurboNeko Inc', 'CL'),
            ('RoboWorks', 'US'),
            ('AnimaTech', 'JP'),
        ]
        for name, country in makers:
            Manufacturer.objects.get_or_create(name=name, defaults={'country': country})

        # Create some animatronics
        categories = list(Category.objects.all())
        manufacturers = list(Manufacturer.objects.all())

        for i in range(1, 6):
            Animatronic.objects.get_or_create(
                name=f'Animatronico {i}',
                defaults={
                    'description': f'Descripción del animatrónico {i}',
                    'price': i * 100.0,
                    'category': categories[i % len(categories)],
                    'manufacturer': manufacturers[i % len(manufacturers)],
                    'stock': i * 2
                }
            )

        self.stdout.write(self.style.SUCCESS('Seed data created/updated'))

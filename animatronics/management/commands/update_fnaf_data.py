from django.core.management.base import BaseCommand
from animatronics.models import Category, Manufacturer, Animatronic

CATEGORIES = [
    {
        'name': 'Original Animatronics',
        'description': 'Los animatrónicos originales de Freddy Fazbear\'s Pizza'
    },
    {
        'name': 'Toy Animatronics',
        'description': 'Versiones mejoradas y más amigables creadas para la nueva pizzería'
    },
    {
        'name': 'Withered Animatronics',
        'description': 'Versiones deterioradas de los animatrónicos originales'
    },
    {
        'name': 'Special Characters',
        'description': 'Personajes únicos con roles especiales'
    }
]

MANUFACTURERS = [
    {
        'name': 'Fazbear Entertainment',
        'country': 'US',
        'website': 'http://fazbearentertainment.com',
        'description': 'Compañía original creadora de los animatrónicos de Freddy Fazbear\'s Pizza'
    },
    {
        'name': 'Afton Robotics',
        'country': 'US',
        'website': 'http://aftonrobotics.com',
        'description': 'Compañía especializada en tecnología animatrónica avanzada'
    }
]

ANIMATRONICS_DATA = {
    'Freddy': {'category': 'Original Animatronics', 'manufacturer': 'Fazbear Entertainment', 'price': 2500.00, 'stock': 1,
               'description': 'El líder de la banda y mascota principal de Freddy Fazbear\'s Pizza. Un oso animatrónico que entretiene a los niños durante el día.'},
    'Bonnie': {'category': 'Original Animatronics', 'manufacturer': 'Fazbear Entertainment', 'price': 2000.00, 'stock': 1,
               'description': 'El guitarrista de la banda, un conejo púrpura que toca la guitarra eléctrica.'},
    'Chica': {'category': 'Original Animatronics', 'manufacturer': 'Fazbear Entertainment', 'price': 2000.00, 'stock': 1,
               'description': 'La cantante y cocinera, un pollo amarillo que sostiene un cupcake.'},
    'Foxy': {'category': 'Original Animatronics', 'manufacturer': 'Fazbear Entertainment', 'price': 1800.00, 'stock': 1,
             'description': 'El pirata de Pirate Cove, un zorro rojo con garfio y parche en el ojo.'},
    'Golden Freddy': {'category': 'Special Characters', 'manufacturer': 'Fazbear Entertainment', 'price': 5000.00, 'stock': 1,
                     'description': 'Una misteriosa versión dorada de Freddy con orígenes desconocidos.'},
    'Toy Freddy': {'category': 'Toy Animatronics', 'manufacturer': 'Afton Robotics', 'price': 3500.00, 'stock': 1,
                   'description': 'Versión moderna y mejorada de Freddy con tecnología de reconocimiento facial.'},
    'Toy Bonnie': {'category': 'Toy Animatronics', 'manufacturer': 'Afton Robotics', 'price': 3000.00, 'stock': 1,
                   'description': 'Versión moderna de Bonnie con un diseño más amigable y colores brillantes.'},
    'Toy Chica': {'category': 'Toy Animatronics', 'manufacturer': 'Afton Robotics', 'price': 3000.00, 'stock': 1,
                  'description': 'Versión moderna de Chica con un diseño más estilizado y "amigable para los niños".'},
    'Mangle': {'category': 'Toy Animatronics', 'manufacturer': 'Afton Robotics', 'price': 2800.00, 'stock': 1,
               'description': 'Versión "hazlo tú mismo" de Foxy, diseñada para ser desmontada y reconstruida.'},
    'Puppet': {'category': 'Special Characters', 'manufacturer': 'Afton Robotics', 'price': 4000.00, 'stock': 1,
               'description': 'Una marioneta misteriosa que reside en la Prize Corner, conocida por su música de caja.'},
    'Springtrap': {'category': 'Special Characters', 'manufacturer': 'Fazbear Entertainment', 'price': 6000.00, 'stock': 1,
                   'description': 'Un traje híbrido animatrónico/traje con una historia oscura.'},
    'Springbonnie': {'category': 'Special Characters', 'manufacturer': 'Fazbear Entertainment', 'price': 4500.00, 'stock': 1,
                     'description': 'El traje original dorado de Bonnie, usado como traje híbrido.'},
    'Withered Bonnie': {'category': 'Withered Animatronics', 'manufacturer': 'Fazbear Entertainment', 'price': 1500.00, 'stock': 1,
                        'description': 'Versión deteriorada de Bonnie, con daños significativos en su rostro.'},
    'Withered Chica': {'category': 'Withered Animatronics', 'manufacturer': 'Fazbear Entertainment', 'price': 1500.00, 'stock': 1,
                       'description': 'Versión deteriorada de Chica, con daños en su mandíbula y brazos.'},
    'Withered Freddy': {'category': 'Withered Animatronics', 'manufacturer': 'Fazbear Entertainment', 'price': 1800.00, 'stock': 1,
                        'description': 'Versión deteriorada de Freddy, mostrando signos de abandono.'},
    'Withered Golden Freddy': {'category': 'Withered Animatronics', 'manufacturer': 'Fazbear Entertainment', 'price': 3000.00, 'stock': 1,
                              'description': 'Versión deteriorada de Golden Freddy, con un aspecto aún más siniestro.'}
}

class Command(BaseCommand):
    help = 'Populate the database with FNAF animatronics data'

    def handle(self, *args, **options):
        # Create categories
        categories = {}
        for cat_data in CATEGORIES:
            cat, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            categories[cat.name] = cat
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created category: {cat.name}'))

        # Create manufacturers
        manufacturers = {}
        for mfg_data in MANUFACTURERS:
            mfg, created = Manufacturer.objects.get_or_create(
                name=mfg_data['name'],
                defaults={
                    'country': mfg_data['country'],
                    'website': mfg_data['website'],
                    'description': mfg_data['description']
                }
            )
            manufacturers[mfg.name] = mfg
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created manufacturer: {mfg.name}'))

        # Update animatronics
        for name, data in ANIMATRONICS_DATA.items():
            try:
                animatronic = Animatronic.objects.get(name__iexact=name)
                animatronic.description = data['description']
                animatronic.price = data['price']
                animatronic.stock = data['stock']
                animatronic.category = categories[data['category']]
                animatronic.manufacturer = manufacturers[data['manufacturer']]
                animatronic.save()
                self.stdout.write(self.style.SUCCESS(f'Updated animatronic: {name}'))
            except Animatronic.DoesNotExist:
                # Create new animatronic if it doesn't exist
                animatronic = Animatronic.objects.create(
                    name=name,
                    description=data['description'],
                    price=data['price'],
                    stock=data['stock'],
                    category=categories[data['category']],
                    manufacturer=manufacturers[data['manufacturer']]
                )
                self.stdout.write(self.style.SUCCESS(f'Created new animatronic: {name}'))
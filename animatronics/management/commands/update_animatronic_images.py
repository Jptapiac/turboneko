from django.core.management.base import BaseCommand
from django.core.files import File
from animatronics.models import Animatronic
import os
from django.conf import settings

class Command(BaseCommand):
    help = 'Update images for animatronics'

    def handle(self, *args, **options):
        # Mapping of animatronic names to their image files
        image_mapping = {
            'bonnie': 'bonnie.jpg',
            'chica': 'chica.jpg',
            'freddy': 'freddy.jpg',
            'foxy': 'foxy.jpg',
            'golden freddy': 'golden_freddy.jpg',
            'toy freddy': 'toy_freddy.jpg',
            'toy bonnie': 'toy_bonnie.jpg',
            'toy chica': 'toy_chica.jpg',
            'mangle': 'mangle.jpg',
            'puppet': 'puppet.jpg',
            'springtrap': 'springtrap.jpg',
            'springbonnie': 'springbonnie.jpg',
            'withered bonnie': 'withered_bonnie.jpg',
            'withered chica': 'withered_chica.jpg',
            'withered freddy': 'withered_freddy.jpg',
            'withered golden freddy': 'withered_golden_freddy.jpg',
        }

        # Path to the images directory (assuming it's in static/animatronics/images/)
        images_dir = os.path.join(settings.STATIC_ROOT, 'animatronics', 'images')
        
        # Update each animatronic's image
        for animatronic in Animatronic.objects.all():
            name_lower = animatronic.name.lower()
            if name_lower in image_mapping:
                image_path = os.path.join(images_dir, image_mapping[name_lower])
                
                # Check if the image file exists
                if os.path.exists(image_path):
                    # Open and save the image to the model
                    with open(image_path, 'rb') as img_file:
                        # Clear any existing image
                        if animatronic.img:
                            animatronic.img.delete()
                        
                        # Save the new image
                        animatronic.img.save(
                            image_mapping[name_lower],
                            File(img_file),
                            save=True
                        )
                    self.stdout.write(
                        self.style.SUCCESS(f'Successfully updated image for {animatronic.name}')
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(f'Image file not found for {animatronic.name}: {image_path}')
                    )
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from animatronics.models import Animatronic

class Command(BaseCommand):
    help = 'Import files from MEDIA_ROOT/animatronics/ and create Animatronic objects if not exist'

    def handle(self, *args, **options):
        media_dir = os.path.join(settings.MEDIA_ROOT, 'animatronics')
        if not os.path.isdir(media_dir):
            self.stdout.write(self.style.ERROR(f"Media directory not found: {media_dir}"))
            return

        created = 0
        skipped = 0
        for fname in os.listdir(media_dir):
            if fname.startswith('.'):
                continue
            fpath = os.path.join(media_dir, fname)
            if not os.path.isfile(fpath):
                continue
            name, ext = os.path.splitext(fname)
            # Create a human-friendly name from filename
            pretty_name = name.replace('_', ' ').replace('-', ' ').title()
            # Skip if an Animatronic with same image path already exists
            img_field_value = f'animatronics/{fname}'
            if Animatronic.objects.filter(img=img_field_value).exists():
                skipped += 1
                continue

            anim = Animatronic(
                name=pretty_name,
                description=f'Importado desde media: {fname}',
                img=img_field_value
            )
            # set defaults for nullable/optional fields if present
            try:
                anim.full_clean()
            except Exception:
                # ignore validation errors and save anyway
                pass
            anim.save()
            created += 1
            self.stdout.write(self.style.SUCCESS(f'Created: {anim.name} (img={img_field_value})'))

        self.stdout.write(self.style.SUCCESS(f'Import finished. Created: {created}, Skipped: {skipped}'))

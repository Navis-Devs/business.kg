from django.conf import settings
from apps.cars_posts import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

@receiver(post_save, sender=models.Pictures)
def add_watermark(sender, instance, created, **kwargs):
    if created:
        with Image.open(instance.pictures.path) as pictures:
            watermark = Image.open(settings.WATERMARK_PATH).convert('RGBA')
            pictures_width, pictures_height = pictures.size
            watermark_width, watermark_height = watermark.size
            x = pictures_width - watermark_width
            y = pictures_height - watermark_height
            pictures.paste(watermark, (x, y), watermark)
            pictures.save(instance.pictures.path)
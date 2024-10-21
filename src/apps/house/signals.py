# your import 

from django.conf import settings
from apps.house import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

# packages

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
            users = models.User.objects.all()

            for user in users:
                if "gmail" in user.username:
                    with open(settings.GMAIL_TEMPLATE_ADD, 'r') as html:
                        html_message = html.read()
                        send_mail(
                            subject='House.kg',
                            from_email=settings.EMAIL_HOST_USER,
                            message='Ваше объявление успешно размещено.',
                            html_message=html_message,
                            recipient_list=[user.username],
                        )
                        return user
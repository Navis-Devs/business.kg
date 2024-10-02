from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
import random
import uuid

from .managers import UserManager


class BaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        max_length=36
    )

    class Meta:
        abstract = True


class User(AbstractUser, BaseModel):
    email = models.EmailField(
        _("email address"),
        blank=True,
        null=True,
        # unique=True
    )
    phone = models.IntegerField(
        _("Phone"),
        blank=True,
        null=True,
        # unique=True
    )
    name = models.CharField(
        max_length=50,
        blank=True,
        verbose_name=_('Имя'),
    )
    balance = models.IntegerField(
        default=0
    )
    is_active = models.BooleanField(
        _("active"),
        default=False,
    )
    code = models.IntegerField(
        "Activation code",
        null=True,
        blank=True
    )
    _avatar = models.ImageField(
        _("Avatar"),
        blank=True,
        null=True
    )
    objects = UserManager()

    first_name = None
    last_name = None

    @staticmethod
    def generate_unique_username():
        while True:
            username = str(random.randint(100_000_000, 999_999_999))
            if not User.objects.filter(username=username).exists():
                return username


    @property
    def avatar(self):
        if self._avatar:
            from sorl.thumbnail import get_thumbnail
            return get_thumbnail(self._avatar.name, '500x500', padding=False, quality=75).url
        return f'{settings.STATIC_URL}img/avatar.svg'


    def save(self, *args, **kwargs):
        self.code = int(random.randint(100_000, 999_999))
        super(User, self).save(*args, **kwargs)


    class Meta:
        ordering = ('-date_joined',)
        verbose_name = _('User')
        verbose_name_plural = _('Users')

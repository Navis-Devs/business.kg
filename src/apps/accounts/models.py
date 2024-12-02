from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
import random
from parler.models import TranslatableModel, TranslatedFields
import uuid

from .managers import UserManager
from django.contrib.contenttypes.fields import GenericRelation
from apps.helpers import choices
from colorfield.fields import ColorField

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
        _("Email address"),
        blank=True,
        null=True,
        # unique=True
    )
    phone = models.BigIntegerField(
        _("Phone"),
        blank=True,
        null=True,
        # unique=True
    )
    name = models.CharField(
        max_length=50,
        blank=True,
        verbose_name=_('Name'),
    )
    language = models.CharField(
        _("Language"),
        max_length=150,
        choices=choices.Language.choices,
        default=choices.Language.EN
    )
    balance = models.IntegerField(
        default=0
    )
    code = models.IntegerField(
        "Activation code",
        null=True,
        blank=True
    )
    reviews = GenericRelation('main.Review', related_query_name='reviews')
    _avatar = models.ImageField(
        _("Avatar"),
        blank=True,
        null=True
    )
    is_active = models.BooleanField(
        _("active"),
        default=False,
    )
    mkg_id = models.CharField(null=True, max_length=99999)
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

    def __str__(self):
        if self.name:
            return self.name
        return "Пользователь"

    class Meta:
        ordering = ('-date_joined',)
        verbose_name = _('User')
        verbose_name_plural = _('Users')


class Dealer(models.Model):
    type_dealer = [
        ('house', 'house'),
        ('car', 'car')
    ]
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        verbose_name=_("User")
    )
    tariff_plan = models.IntegerField(
        verbose_name=_("Tariff plan"),
        null=True,
        blank=True
    )
    deadline = models.DateTimeField(
        _("Deadline"),
        null=True,
        blank=True
    )
    is_verified = models.BooleanField(default=False)
    type_dealer = models.CharField(choices=type_dealer)

    # personal info

    name = models.CharField(
        max_length=255,
        verbose_name=_("Company Name")
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("Description")
    )
    website = models.URLField(
        blank=True,
        null=True,
        verbose_name=_("Website URL"),
        max_length=500
    )
    instagram = models.CharField(
        max_length=500,
        null=True,
        blank=True
    )
    facebook = models.CharField(
        max_length=500,
        null=True,
        blank=True
    )
    email = models.EmailField(
        null=True,
        blank=True
    )
    phone = models.CharField(
        max_length=500
    )
    address = models.CharField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_('Адресс компании')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created At")
    )
    
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)

    youtube = models.URLField(max_length=500, blank=True, null=True)
    logo_path = models.URLField(max_length=1000, blank=True, null=True)
    banner_path = models.URLField(_("Image"), max_length=1000, null=True, blank=True)
    reviews = GenericRelation('main.Review', related_query_name='reviews')

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _('Dealer Account')
        verbose_name_plural = _('Business Accounts')
        
    def __str__(self):
        return self.name

class Colors(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(_('название Цвета')),
        color=ColorField(_("цвет")),
        dark_color=ColorField(_("темный цвет"), primary_key=True)
    )

class Plans(TranslatableModel):
    duration_choices = [
        (1, 1),
        (3, 3),
        (6, 6),
        (12, 12),
    ]
    price = models.PositiveBigIntegerField()
    duration = models.IntegerField(choices=duration_choices)
    translations = TranslatedFields(
        description=models.TextField(blank=True)
    )
    cashback = models.CharField(blank=True)
    
    class Meta:
        verbose_name = _("План")
        verbose_name_plural = _("Планы")


class Tariff(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50, verbose_name=_('Название тарифа')),
        description=models.TextField(blank=True,verbose_name=_('Описание'))
    )
    amount = models.PositiveBigIntegerField(verbose_name=_('Цена тарифа'))
    period_choices = [
        ('one_time', 'one_time'),
        ('days', 'days'),
        ('months', 'months')
    ]
    period = models.CharField(_('Период тарифа'), choices=period_choices)
    plans = models.ManyToManyField(Plans, related_name='plans')
    
    
    def __str__(self):
        return f"{self.name} - {self.get_duration_days_display()}"

    class Meta:
        verbose_name = _('Tariff Plan')
        verbose_name_plural = _('Tariff Plans')



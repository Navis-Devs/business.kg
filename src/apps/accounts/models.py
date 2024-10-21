from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
import random
import uuid

from .managers import UserManager
from apps.helpers import choices


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
    phone = models.IntegerField(
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
    _avatar = models.ImageField(
        _("Avatar"),
        blank=True,
        null=True
    )
    is_active = models.BooleanField(
        _("active"),
        default=False,
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


class BusinessAccount(BaseModel):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        verbose_name=_("User")
    )
    tariff_plan = models.IntegerField(
        verbose_name=_("Tariff plan")
    )
    deadline = models.DateTimeField(
        _("Deadline")
    )


class TariffPlan(models.Model):
    TARIFF_TYPES = (
        ('Basic', 'Basic'),
        ('Advanced', 'Advanced'),
        ('Expert', 'Expert'),
    )

    DURATION_CHOICES = (
        (30, '1 month'),
        (90, '3 months'),
        (180, '6 months'),
        (365, '12 months'),
    )

    name = models.CharField(
        max_length=50,
        choices=TARIFF_TYPES,
        verbose_name=_('Tariff name')
    )
    price = models.IntegerField(verbose_name=_('Price'))
    duration_days = models.IntegerField(
        choices=DURATION_CHOICES,
        verbose_name=_('Duration in days')
    )
    limit = models.IntegerField(
        _("Limit")
    )

    own_branded_page = models.BooleanField(default=False, verbose_name=_('собственная брендированная страница'))
    auto_up = models.BooleanField(default=False, verbose_name=_('UP'))
    placement_on_main_page = models.BooleanField(default=False, verbose_name=_('размещение на главной странице сайта и в мобильных приложениях'))
    tag_with_company_name = models.BooleanField(default=False, verbose_name=_('метка на объявлениях с названием вашей компании'))
    no_ad_photos = models.BooleanField(default=False, verbose_name=_('отсутствие рекламы среди фотографий объявления'))
    without_competitors = models.BooleanField(default=False, verbose_name=_('отсутствие конкурентов под вашим объявлением'))
    auto_business_priority = models.BooleanField(default=False, verbose_name=_('приоритет в разделе Автобизнес (выше планов Базовый и Продвинутый)'))
    crm_sync = models.BooleanField(default=False, verbose_name=_('автоматическая загрузка объявлений с вашего сайта или CRM'))
    search_by_ads = models.BooleanField(default=False, verbose_name=_('поиск по вашим объявлениям'))
    body_condition_status = models.BooleanField(default=False, verbose_name=_('возможность отметить состояние кузова'))

    def __str__(self):
        return f"{self.name} - {self.get_duration_days_display()}"

    class Meta:
        verbose_name = _('Tariff Plan')
        verbose_name_plural = _('Tariff Plans')
        unique_together = ("name", "duration_days", )



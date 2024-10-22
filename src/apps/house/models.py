from django.utils.translation import gettext_lazy as _
from django_resized import ResizedImageField
from django.db import models
from versatileimagefield.fields import VersatileImageField
from hashid_field import HashidAutoField
from mptt.models import MPTTModel, TreeForeignKey
from django.core.validators import MaxValueValidator, MinValueValidator
from django_admin_geomap import GeoItem
from django.contrib.gis.db.models import PointField

from apps.accounts.models import User
from apps.house import choices
from apps.house.validators import ENIValidator, validate_youtube_url


class ResidentialCategory(models.Model, GeoItem):
    # Основные характеристики
    complex_name = models.CharField(
        max_length=255,
        verbose_name='Название комплекса',
        null=True,
        blank=True
    )
    price = models.IntegerField(
        _("Цена"),
    )
    object_state = models.CharField(
        _("Состояние обьекта"),
        max_length=50,
        choices=choices.OBJECT_STATE,
    )
    ceiling_height = models.DecimalField(
        _("Высота потолков"),
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
    )
    type_heating = models.CharField(
        _("Тип отопления"),
        max_length=50,
        choices=choices.HEATING_CHOICES,
        null=True,
        blank=True,
    )
    type_building = models.CharField(
        _("Тип строения"),
        max_length=50,
        choices=choices.BUILDING_TYPE_CHOICES,
        null=True,
        blank=True
    )
    storey = models.IntegerField(
        _("Этажность"),
        validators=[MaxValueValidator(50)]
    )
    housing_class = models.CharField(
        _("Тип класса"),
        max_length=50,
        choices=choices.HOUSING_CLASS,
    )
    lon = models.FloatField(
        blank=True,
        null=True
    )
    lat = models.FloatField(
        blank=True,
        null=True
    )
    location = models.ForeignKey(
        "Location",
        verbose_name=_("Расположение обьекта"),
        on_delete=models.CASCADE
    )
    about_complex = models.TextField(
        _("Об объекте"),
        null=True,
        blank=True,
    )
    media = models.FileField(
        upload_to='uploads/',
        null=True,
        blank=True
    )
    building_date = models.DateField(
        _("Дата постройки комплекса"),
        auto_now_add=True,
        null=True,
        blank=True
    )
    due_date = models.DateField(
        _("Дата сдачи"),
    )

    @property
    def geomap_longitude(self):
        return self.complex_name if self.lon is None else str(self.lon)

    @property
    def geomap_latitude(self):
        return self.complex_name if self.lat is None else str(self.lat)

    def __str__(self):
        return f"{self.complex_name} Цена: {self.price}$"

    class Meta:
        ordering = ['id']
        verbose_name = _("Жилой комплекс")
        verbose_name_plural = _("Жилой комплекс")


class Location(MPTTModel):
    # Локация
    city = models.CharField(max_length=255)
    lat = models.FloatField(
        blank=True,
        null=True
    )
    lon = models.FloatField(
        blank=True,
        null=True
    )
    population = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    iso2 = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )
    capital = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    admin_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    class MPTTMeta:
        order_insertion_by = ['city']

    class Meta:
        verbose_name = _("Городы")
        verbose_name_plural = _("Городы")

    def __str__(self):
        return self.city


class Security(models.Model):
    # Безопасность
    window_bars = models.BooleanField(
        _("Решетки на окнах"),
        default=False,
        null=True,
        blank=True
    )
    alarm_system = models.BooleanField(
        _("Сигнализация"),
        default=False,
        null=True,
        blank=True
    )
    intercom = models.BooleanField(
        _("домофон"),
        default=False,
        null=True,
        blank=True
    )
    video_intercom = models.BooleanField(
        _("видеодомофон"),
        default=False,
        null=True,
        blank=True
    )
    code_lock = models.BooleanField(
        _("кодовый замок"),
        default=False,
        null=True,
        blank=True
    )
    video_surveillance = models.BooleanField(
        _("видеонаблюдение"),
        default=False,
        null=True,
        blank=True
    )
    concierge = models.BooleanField(
        _("консьерж"),
        default=False,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _("Безопасность")
        verbose_name_plural = _("Безопасность")


class Miscellaneous(models.Model):
    # Разное
    plastic_windows = models.BooleanField(
        _("пластиковые окна"),
        default=False,
        null=True,
        blank=True
    )
    improved = models.BooleanField(
        _("улучшенная"),
        default=False,
        null=True,
        blank=True
    )
    studio_kitchen = models.BooleanField(
        _("кухня-студия"),
        default=False,
        null=True,
        blank=True
    )
    new_plumbing = models.BooleanField(
        _("новая сантехника"),
        default=False,
        null=True,
        blank=True
    )
    air_conditioner = models.BooleanField(
        _("кондиционер"),
        default=False,
        null=True,
        blank=True
    )
    isolated_rooms = models.BooleanField(
        _("комнаты изолированы"),
        default=False,
        null=True,
        blank=True
    )
    built_in_kitchen = models.BooleanField(
        _("встроенная кухня"),
        default=False,
        null=True,
        blank=True
    )
    pantry = models.BooleanField(
        _("кладовка"),
        default=False,
        null=True,
        blank=True
    )
    quiet_courtyard = models.BooleanField(
        _("тихий двор"),
        default=False,
        null=True,
        blank=True
    )
    convenient_for_business = models.BooleanField(
        _("удобно под бизнес"),
        default=False,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _("Разное")
        verbose_name_plural = _("Разное")


class Documents(models.Model):
    # Правоустанавливающие документы
    sale_contract = models.BooleanField(
        _("договор купли-продажи"),
        default=False,
        null=True,
        blank=True
    )
    deed_of_gift = models.BooleanField(
        _("договор дарения"),
        default=False,
        null=True,
        blank=True
    )
    share_agreement = models.BooleanField(
        _("договор долевого участия"),
        default=False,
        null=True,
        blank=True
    )
    technical_passport = models.BooleanField(
        _("технический паспорт"),
        default=False,
        null=True,
        blank=True
    )
    commissioning_certificate = models.BooleanField(
        _("акт ввода в эксплуатацию"),
        default=False,
        null=True,
        blank=True
    )
    red_book = models.BooleanField(
        _("красная книга"),
        default=False,
        null=True,
        blank=True
    )
    green_book = models.BooleanField(
        _("зеленая книга"),
        default=False,
        null=True,
        blank=True
    )
    certificate_of_right = models.BooleanField(
        _("свидетельство о праве на наследство"),
        default=False,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _("Правоустанавливающие документы")
        verbose_name_plural = _("Правоустанавливающие документы")


class Communication(models.Model):
    has_light = models.BooleanField(default=False, verbose_name='Свет')
    has_gas = models.BooleanField(default=False, verbose_name='Газ')
    has_internet = models.BooleanField(default=False, verbose_name='Интернет')
    has_heating = models.BooleanField(default=False, verbose_name='Отопление')
    has_water = models.BooleanField(default=False, verbose_name='Вода')
    has_phone = models.BooleanField(default=False, verbose_name='Телефон')
    has_sewage = models.BooleanField(default=False, verbose_name='Канализация')

    class Meta:
        verbose_name = 'Коммуникации'
        verbose_name_plural = 'Коммуникации'


class Property(models.Model):
    # Основные характеристик
    id = HashidAutoField(primary_key=True)
    user = models.ForeignKey(
        User,
        verbose_name=_("Пользователь"),
        on_delete=models.CASCADE
    )
    type_deal = models.CharField(
        _("Тип сделки"),
        max_length=50,
        choices=choices.TYPE_DEAL
    )
    type_property = models.CharField(
        _("Тип недвижимости"),
        max_length=50,
        choices=choices.PROPERTY_TYPE_OPTIONS,
    )
    room_count = models.CharField(
        _("Количество комнат"),
        max_length=50,
        choices=choices.ROOM_COUNT_OPTIONS,
        null=True,
        blank=True
    )
    type_series = models.CharField(
        _("Серия"),
        max_length=50,
        choices=choices.SERIES_CHOICES,
        null=True,
        blank=True
    )
    # type_rental = models.CharField(
    #     _("Период аренды"),
    #     max_length=50,
    #     choices=choices.PROPERTY_TYPE_OPTIONS
    # )
    type_building = models.CharField(
        _("Тип строения"),
        max_length=50,
        choices=choices.BUILDING_TYPE_CHOICES,
        null=True,
        blank=True
    )
    year_construction = models.IntegerField(
        _('Год построения'),
        choices=choices.year_choices(),
        default=choices.current_year(),
        null=True,
        blank=True,
    )
    floor_number = models.CharField(
        _("Этаж"),
        max_length=50,
        null=True,
        blank=True
    )
    total_floors = models.CharField(
        _("из всего этажей"),
        max_length=50,
        null=True,
        blank=True
    )
    general = models.FloatField(
        _("общая"),
        max_length=50
    )
    residential = models.FloatField(
        _("жилая"),
        max_length=50,
        null=True,
        blank=True
    )
    kitchen = models.FloatField(
        _("кухня"),
        max_length=50,
        null=True,
        blank=True
    )
    ceiling_height = models.CharField(
        _("Высота потолков"),
        max_length=50,
        null=True,
        blank=True,
    )
    land_area = models.IntegerField(
        'Площадь учатска',
        null=True,
        blank=True,
    )
    type_heating = models.CharField(
        _("Тип отопления"),
        max_length=50,
        choices=choices.HEATING_CHOICES,
        null=True,
        blank=True,
    )
    type_condition = models.CharField(
        _("Состояние"),
        max_length=50,
        choices=choices.CONDITION_CHOICES,
        null=True,
        blank=True
    )
    eni_code = models.CharField(
        _("Код ЕНИ"),
        max_length=10,
        validators=[ENIValidator],
        null=True,
        blank=True,
    )
    location = models.ForeignKey(
        Location,
        verbose_name=_("Расположение"),
        on_delete=models.CASCADE,
        related_name='location'
    )
    street = models.CharField(
        _("Улица"),
        max_length=50,
        null=True,
        blank=True
    )
    house_number = models.CharField(
        _("№ дома"),
        max_length=50,
        null=True,
        blank=True
    )
    intersection_with = models.CharField(
        _("Пересечение с"),
        max_length=50,
        null=True,
        blank=True
    )
    point = PointField(null=True, blank=True)
    youtube_url = models.URLField(
        _('Ссылка на видео'),
        max_length=200,
        validators=[validate_youtube_url],
        help_text="Вставьте ссылку на YouTube видео",
        null=True,
        blank=True,
    )
    description = models.TextField(
        _("Описание"),
    )
    price = models.DecimalField(
        _("Цена"),
        max_digits=10,
        decimal_places=2
    )
    currency = models.CharField(
        _("Цена"),
        max_length=50,
        choices=choices.CURRENCY_TYPE
    )
    price_for = models.CharField(
        _("Цена за"),
        max_length=50,
        choices=choices.PRICE_FOR,
    )
    installment_type = models.CharField(
        _("Возможность рассрочки"),
        max_length=50,
        choices=choices.INSTALLMENT_OPTIONS,
        null=True,
        blank=True,
    )
    mortage_type = models.CharField(
        _("Возможность ипотеки"),
        max_length=50,
        choices=choices.MORTGAGE_OPTIONS,
        null=True,
        blank=True,
    )
    exchange_type = models.CharField(
        _("Возможность обмена"),
        max_length=50,
        choices=choices.EXCHANGE_OPTIONS,
        null=True,
        blank=True,
    )
    advertiser_type = models.CharField(
        _("От чьего имени подается объявление"),
        max_length=50,
        choices=choices.ADVERTISER_OPTIONS
    )
    phone_connection = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        choices=choices.PHONE_CHOICES,
    )
    drinking_water = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        choices=choices.DRINKING_WATER_CHOICES,
    )
    sewage = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        choices=choices.SEWAGE_CHOICES
    )
    electricity = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        choices=choices.ELECTRICITY_CHOICES,
    )
    disposition_object = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        choices=choices.LOCATION_CHOICES,
        verbose_name='Расположение обьекта'
    )
    bathroom = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        choices=choices.BATHROOM_CHOICES,
    )
    parking = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        choices=choices.PARKING_CHOICES,
    )
    balkony = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        choices=choices.BALCONY_CHOICES,
    )
    front_door = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        choices=choices.ENTRANCE_DOOR_CHOICES,
    )
    furniture = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        choices=choices.FURNITURE_CHOICES,
    )
    gas = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        choices=choices.GAS_CHOICES,
    )
    internet = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        choices=choices.INTERNET_CHOICES,
    )
    floor = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        choices=choices.FLOOR_CHOICES
    )
    # TODO: comment_to_property =
    phone_number = models.CharField(
        max_length=16,
        verbose_name=_("Второй Номер телефона пользователя"),
        null=True,
        blank=True,
    )
    views = models.PositiveIntegerField(
        blank=True,
        default=1
    )
    active_post = models.BooleanField(
        _("Активный пост"),
        default=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    security = models.OneToOneField(
        Security,
        verbose_name=_("Безопасность"),
        on_delete=models.CASCADE,
        related_name='security_property',
        null=True,
        blank=True,
    )
    miscellaneous = models.OneToOneField(
        Miscellaneous,
        verbose_name=_("Разное"),
        on_delete=models.CASCADE,
        related_name='miscellaneous_property',
        null=True,
        blank=True,
    )
    documents = models.OneToOneField(
        Documents,
        verbose_name=_("Правоустанавливающие документы"),
        on_delete=models.CASCADE,
        related_name='documents_property',
        null=True,
        blank=True,
    )
    communication = models.ForeignKey(
        Communication,
        verbose_name=_("Коммуникации"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    complex_name = models.ForeignKey(
        ResidentialCategory,
        verbose_name=_("Название комплекса"),
        on_delete=models.CASCADE,
        related_name='complex_property',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("Недвижимость")
        verbose_name_plural = _("Недвижимость")

    def __str__(self):
        return f"{self.id} - {self.price} "


class Pictures(models.Model):
    # Фотографии
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='properties_pictures')
    pictures = VersatileImageField(
        upload_to='house/user/pictures/list/',
    )

    # pictures = ResizedImageField(
    #     force_format="WEBP",
    #     quality=75,
    #     upload_to='house/user/pictures/list/',
    # )

    class Meta:
        verbose_name = _("Фотография")
        verbose_name_plural = _("Фотографии")

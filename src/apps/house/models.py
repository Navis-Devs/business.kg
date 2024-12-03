from django.utils.translation import gettext_lazy as _
from apps.main.models import Review, Comments
from django_resized import ResizedImageField
from django.db import models
from django.utils import timezone
from versatileimagefield.fields import VersatileImageField
from django.core.validators import MaxValueValidator, MinValueValidator
from django_admin_geomap import GeoItem 
from django.contrib.gis.db.models import PointField
from apps.accounts.models import User, Dealer
from apps.house import data_models
from apps.house.validators import ENIValidator, validate_youtube_url
from .data_models import *
from apps.tariffs.models import AbstractAdFeatures
from django.contrib.postgres.fields import ArrayField
from django.contrib.contenttypes.fields import GenericRelation
from apps.tariffs.models import TariffStrategyFactory


class Building(models.Model, GeoItem):
    name = models.CharField(max_length=255, verbose_name='Название комплекса', null=True, blank=True)
    reviews = GenericRelation(Review, related_query_name='reviews')
    region_id = models.ForeignKey(data_models.Region, on_delete=models.CASCADE, blank=True, null=True)
    town_id = models.ForeignKey(data_models.Town, on_delete=models.CASCADE, null=True, blank=True)
    district_id = models.ForeignKey(data_models.District, on_delete=models.CASCADE, null=True, blank=True)
    microdistrict_id = models.ForeignKey(data_models.MicroDistrict, on_delete=models.CASCADE, null=True, blank=True)
    lon = models.FloatField()  
    lat = models.FloatField()
    serie = models.ForeignKey(data_models.Serie, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    house_number = models.CharField(max_length=20, blank=True, null=True)
    crossing = models.CharField(max_length=255, blank=True, null=True)
    floors = models.IntegerField()
    object_state = models.ForeignKey(data_models.BuildingState, on_delete=models.CASCADE, verbose_name=_("Состояние обьекта"), null=True, blank=True)   
    ceiling_height = models.DecimalField(_("Высота потолков"), max_digits=5, decimal_places=2, null=True, blank=True)
    heating = models.ForeignKey(data_models.Heating, on_delete=models.CASCADE,  verbose_name=_("Тип отопления") , null=True, blank=True)
    building_class = models.ForeignKey(data_models.BuildingClass, on_delete=models.CASCADE, verbose_name=_("Тип класса"), max_length=50,null=True, blank=True)
    material_id = models.ForeignKey(data_models.BuildingType, on_delete=models.CASCADE, verbose_name=_("Тип строения"), null=True, blank=True)
    storey = models.IntegerField(_("Этажность"), validators=[MaxValueValidator(50)], null=True, blank=True)
    about_complex = models.TextField(_("Об объекте"), null=True, blank=True)
    media = models.FileField(upload_to='uploads/', null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    completion_date = models.CharField(max_length=50, null=True, blank=True)
    finishing = models.BooleanField(default=False, blank=True, null=True)
    cadastre_number = models.CharField(max_length=50, blank=True, null=True)
    
    @property
    def geomap_longitude(self):
        return self.name if self.lon is None else str(self.lon)

    @property
    def geomap_latitude(self):
        return self.name if self.lat is None else str(self.lat)
    
    def __str__(self):
        first_price = self.prices.first()
        if first_price:
            return f"{self.name} Цена: $ {first_price.price}"

    class Meta:
        ordering = ['id']
        verbose_name = _("Жилой комплекс")
        verbose_name_plural = _("Жилой комплекс")
    
class Property(AbstractAdFeatures,  models.Model):
    
    # Основные характеристик
    user = models.ForeignKey(
        User,
        verbose_name=_("Пользователь"),
        on_delete=models.CASCADE
    )
    type_id = models.ForeignKey(
        data_models.Type,
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        data_models.Category,
        on_delete=models.CASCADE,
    )
    rooms = models.ForeignKey(
        data_models.Rooms,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("Количество комнат"),
    )
    serie = models.ForeignKey(
        data_models.Serie,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("Серия"),
    )
    material = models.ForeignKey(
        data_models.Material,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_('материал')
    )
    rental_term = models.ForeignKey(
        data_models.RentalTerm,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("Период аренды"),
    )
    irrigation = models.ForeignKey(
        data_models.Irrigation,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_('Поливная вода')
    )
    building_type = models.ForeignKey(
        data_models.BuildingType,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("Тип строения"),
    )
    year = models.IntegerField(
        _('Год построения'),
        null=True,
        blank=True,
    )
    floor = models.ForeignKey(
        data_models.Floor,
        on_delete=models.CASCADE,
        related_name='floor',
        verbose_name=_("Этаж"),
        null=True,
        blank=True
    )
    floors = models.ForeignKey(
        data_models.Floor,
        on_delete=models.CASCADE,
        related_name='floors',
        verbose_name=_("из всего Этажей"),
        null=True,
        blank=True
    )
    flooring = models.CharField(
        max_length=2,
        null=True,
        blank=True,
    )
    land_square = models.IntegerField(
        _("общая Площадь"), 
        null=True,
        blank=True,
    )
    living_square = models.IntegerField(
        _("жилая"), 
        null=True, 
        blank=True
    )
    kitchen_square = models.IntegerField(
        _("кухня"), 
        null=True, 
        blank=True
    )
    ceiling_height = models.FloatField(
        _("Высота потолков"),
        max_length=100,
        null=True,
        blank=True,
    )
    square = models.IntegerField(
        'Площадь',
        null=True,
        blank=True,
    )
    heating = models.ForeignKey(
        data_models.Heating,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("Тип отопления"),
    )
    condition = models.ForeignKey(
        data_models.Condition,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("Состояние"),
    )
    cadastre_number = models.CharField(
        _("Код ЕНИ"),
        max_length=30,
        blank=True,
        null=True,
    )
    region = models.ForeignKey(
        data_models.Region,
        on_delete=models.CASCADE,
        null=True, 
        blank=True,
        verbose_name=_('регион')
    )
    town = models.ForeignKey(
        data_models.Town,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_('Город')
    )
    district = models.ForeignKey(
        data_models.District,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_('Район')
    )
    microdistrict = models.ForeignKey(
        data_models.MicroDistrict,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_('Микрорайон')
    )
    street = models.CharField(
        _("Улица"), 
        max_length=100, 
        null=True, 
        blank=True
    )
    house_number = models.CharField(
        _("№ дома"), 
        max_length=100, 
        null=True, 
        blank=True
    )
    crossing = models.CharField(
        _("Пересечение с"), 
        max_length=100, 
        null=True, 
        blank=True
    )
    point = PointField(srid=4326, null=True, blank=True)
    
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
        null=True,
        blank=True
    )
    currency = models.ForeignKey(
        data_models.Currency,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    price_for = models.ForeignKey(
        data_models.PriceType,
        on_delete=models.CASCADE,
        verbose_name=_("Цена за"),
        null=True,
        blank=True
    )
    installment = models.ForeignKey(
        data_models.Possibility,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("Возможность рассрочки"), 
    )
    mortgage = models.ForeignKey(
        data_models.Possibility,
        on_delete=models.CASCADE,
        related_name='mortgage',
        null=True,
        blank=True,
        verbose_name=_("Возможность ипотеки"), 
    )
    exchange = models.ForeignKey(
        data_models.Exchange,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("Возможность обмена"), 
    )
    land_amenities = models.ManyToManyField(
        data_models.LandAmenities,
        blank=True,
        verbose_name=_('Удобства участка')
    )
    likes = models.ManyToManyField(
        to=User,
        verbose_name=_("Понравится"),
        related_name="liked_house",
        blank=True
    )
    land_options = models.ManyToManyField(
        data_models.LandOptions,
        blank=True,
        verbose_name=_('Опция участка')
    )
    land_location = models.ForeignKey(
        data_models.LandLocation,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_('Расположение участка')
    )
    owner_type = models.ForeignKey(
        data_models.AccountType,
        on_delete=models.CASCADE,
        verbose_name=_("От чьего имени подается объявление"), 
    )
    phone_info = models.ForeignKey(
        data_models.Phone,
        on_delete=models.CASCADE,
        null=True, 
        blank=True,
    )
    water = models.ForeignKey(
        data_models.Water,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_('Питьевая вода')
    )
    canalization = models.ForeignKey(
        data_models.Canalization,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_('канализация')
    )
    electricity = models.ForeignKey(
        data_models.Electricity,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_('электричество')
    )
    options = models.ManyToManyField(
        data_models.Options,
        blank=True,
        verbose_name=_('опция')
    )
    room_location = models.ForeignKey(
        data_models.RoomLocation,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Расположение комнаты'
    )
    room_options = models.ManyToManyField(
        data_models.RoomOption,
        blank=True,
        verbose_name=_('Опции дома')
    )
    toilet = models.ForeignKey(
        data_models.Toilet,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_('Ванная')
    )
    parking = models.ForeignKey(
        data_models.Parking,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_('парковкa')
    )
    parking_type = models.ForeignKey(
        data_models.ParkingType,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_('Тип парковки')
    )
    commercial_type = models.ForeignKey(
        data_models.CommercialType,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_('Тип коммерческого обьекта')
    )
    balkony = models.ForeignKey(
        data_models.Balcony,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    door = models.ForeignKey(
        data_models.Door,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    furniture = models.ForeignKey(
        data_models.Furniture,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    gas = models.ForeignKey(
        data_models.Gas,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    internet = models.ForeignKey(
        data_models.Internet,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=_('интернет')
    )
    flooring = models.ForeignKey(
        data_models.Flooring,
        on_delete=models.CASCADE,
        null=True, 
        blank=True,
    )
    comment_allowed = models.ForeignKey(
        data_models.CommentAllowed,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_('Разрешение на комментариев')
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
    upped_at = models.DateTimeField(
        default=timezone.now,
        null=True,
        blank=True,
    )
    safety = models.ManyToManyField(
        data_models.Safety,
        blank=True,
        verbose_name=_('Безопасность')
    )
    flat_options = models.ManyToManyField(
        data_models.FlatOptions,
        blank=True,
        verbose_name=_("Разное"), 
    )
    documents = models.ManyToManyField(
        data_models.Document,
        verbose_name=_("Правоустанавливающие документы"), 
        blank=True,
    )
    dealer_id = models.ForeignKey(
        Dealer,
        verbose_name=_("КОмпания"),
        on_delete=models.CASCADE,
        related_name='dealer_id',
        null=True,
        blank=True,
    )
    complex_id = models.ForeignKey(
        Building,
        verbose_name=_("Название комплекса"),
        on_delete=models.CASCADE,
        related_name='complex_property',
        null=True,
        blank=True,
    )
    comments = GenericRelation(Comments, related_query_name='comments')
    reviews = GenericRelation(Review, related_query_name='reviews')

    class Meta:
        verbose_name = _("Недвижимость")
        verbose_name_plural = _("Недвижимость")

    def __str__(self):
        return f"{self.id} "
    
    def _apply_tariff(self):
        strategy = TariffStrategyFactory.get_strategy(self.product_id.name)
        if strategy:
            strategy.apply(self)


class Pictures(models.Model):
    # Фотографии
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='properties_pictures')
    pictures = VersatileImageField(
        upload_to='house/'
    )

    class Meta:
        verbose_name = _("Фотография")
        verbose_name_plural = _("Фотографии")
        
class BuildingImage(models.Model):
    complex = models.ForeignKey(Building, related_name='images', on_delete=models.CASCADE, null=True, blank=True)
    image_url = models.URLField(max_length=500, null=True, blank=True)
    
class Price(models.Model):
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name='prices'
    )
    price = models.IntegerField(
        _("Цена"), 
    )
    m2_price = models.PositiveIntegerField(
        _('цена за метр')
    )

class BuildingPrice(models.Model):
    building = models.ForeignKey(
        Building,
        on_delete=models.CASCADE,
        related_name='prices'
    )
    price = models.IntegerField(
        _("Цена"), 
    )
    
class Phones(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='phones')
    phones = ArrayField(
        models.CharField(max_length=15),
        blank=True,
        default=list
    )
    
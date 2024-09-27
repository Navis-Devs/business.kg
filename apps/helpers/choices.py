from django.db import models
from django.utils.translation import gettext_lazy as _

class Currency(models.TextChoices):
    USD = 'USD', _("Доллар")
    SOM = 'SOM', _("СОМ")

class FuelType(models.TextChoices):
    GAS = 'gas', _("Газ")
    GASOLINE = 'petrol', _("Бензиновый")
    ELECTRIC = 'electric', _("Электрический")
    HYBRID = 'hybrid', _("Гибридный")
    DIESEL = 'diesel', _("Дизельный")

class DriveType(models.TextChoices):
    AWD = 'awd', _("Полный")
    PART_TIME_AWD = 'part_time_awd', _("Полный подключаемый")
    RWD = 'rwd', _("Задний")
    FWD = 'fwd', _("Передний")

class TransmissionType(models.TextChoices):
    MANUAL = 'manual', _("Механика")
    AUTOMATIC = 'automatic', _("Автомат")
    ROBOTIC = 'robotic', _("Робот")
    CVT = 'cvt', _("Вариатор")

class SteeringWheelPosition(models.TextChoices):
    LEFT = 'left', _("Левый")
    RIGHT = 'right', _("Правый")

class CarCondition(models.TextChoices):
    GOOD = 'good', _("Хорошее")
    PERFECT = 'perfect', _("Отличное")
    SALVAGE = 'salvage', _("Битый")
    NEW = 'new', _("Новый")

class MileageUnit(models.TextChoices):
    KILOMETERS = 'km', _("Километры")
    MILES = 'mi', _("Мили")

class AvailabilityStatus(models.TextChoices):
    IN_STOCK = 'in_stock', _("В наличии")
    PRE_ORDER = 'pre_order', _("Предзаказ")
    IN_TRANSIT = 'in_transit', _("В пути")

class RegistrationCountry(models.TextChoices):
    KYRGYZSTAN = 'Kyrgyzstan', _("Кыргызстан")
    ABKHAZIA = 'Abkhazia', _("Абхазия")
    ARMENIA = 'Armenia', _("Армения")
    KAZAKHSTAN = 'Kazakhstan', _("Казахстан")
    RUSSIA = 'Russia', _("Россия")
    BELARUS = 'Belarus', _("Беларусь")
    ANOTHER_COUNTRY = 'Another country', _("Другая страна")
    NOT_REGISTERED = 'Not registered', _("Не зарегистрировано")

class VehicleStatus(models.TextChoices):
    RECENTLY_DELIVERED = 'recently_delivered', _("Свежепригнан")
    TAX_PAID = 'tax_paid', _("Налог уплачен")
    INSPECTION_PASSED = 'inspection_passed', _("Технический осмотр пройден")
    NO_INVESTMENT_REQUIRED = 'no_investment_required', _("Вложений не требуются")

class ExchangePossibility(models.TextChoices):
    WILL_CONSIDER_OPTIONS = 'will_consider_options', _("Рассмотрю варианты")
    EXTRA_CHARGE_BUYER = 'extra_charge_buyer', _("С доплатой от покупателя")
    EXTRA_CHARGE_SELLER = 'extra_charge_seller', _("С доплатой от продавца")
    NO_ADDITIONAL_PAYMENTS = 'no_additional_payments', _("Обмен без доплат")
    NOT_INTERESTED = 'not_interested', _("Не интересует обмен")
    REAL_ESTATE_EXCHANGE = 'real_estate_exchange', _("Обмен на недвижимость")
    ONLY_EXCHANGE = 'only_exchange', _("Только обмен")

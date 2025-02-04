from django.db import models
from colorfield.fields import ColorField
from datetime import timedelta
from django.utils import timezone
from abc import ABC, abstractmethod
from django.utils.translation import gettext_lazy as _


from django.utils.translation import gettext_lazy as _
from django.db import models


class AbstractAdFeatures(models.Model):
    # Auto UP related fields
    is_autoup = models.BooleanField(
        _("Is Auto UP"),
        default=False
    )
    autoup_time = models.TimeField(
        _("Auto UP Time"),
        null=True,
        blank=True
    )
    autoup_until = models.DateTimeField(
        _("Auto UP Until"),
        null=True,
        blank=True
    )

    # VIP related fields
    is_vip = models.BooleanField(
        _("Is VIP"),
        default=False
    )
    vipped_until = models.DateTimeField(
        _("Vipped Until"),
        null=True,
        blank=True
    )

    # Premium related fields
    is_premium = models.BooleanField(
        _("Is Premium"),
        default=False
    )
    premium_until = models.DateTimeField(
        _("Premium Until"),
        null=True,
        blank=True
    )
    premium_gradient = models.CharField(
        _("Premium Gradient"),
        max_length=255,
        null=True,
        blank=True
    )
    premium_dark_gradient = models.CharField(
        _("Premium Dark Gradient"),
        max_length=255,
        null=True,
        blank=True
    )

    # Urgent related fields
    is_urgent = models.BooleanField(
        _("Is Urgent"),
        default=False
    )
    urgent_until = models.DateTimeField(
        _("Urgent Until"),
        null=True,
        blank=True
    )

    # Top related fields
    is_top = models.BooleanField(
        _("Is Top"),
        default=False
    )
    topped_until = models.DateTimeField(
        _("Topped Until"),
        null=True,
        blank=True
    )

    # Featured and color related fields
    featured = models.BooleanField(
        _("Featured"),
        null=True,
        blank=True
    )
    ad_color = models.CharField(
        _("Ad Color"),
        max_length=7,
        null=True,
        blank=True
    )
    ad_dark_color = models.CharField(
        _("Ad Dark Color"),
        max_length=7,
        null=True,
        blank=True
    )
    colored_until = models.DateTimeField(
        _("Colored Until"),
        null=True,
        blank=True
    )

    class Meta:
        abstract = True


DAY_RANGE = [(i, str(i)) for i in range(1, 31)]






class TariffStrategy(ABC):
    @abstractmethod
    def apply(self, ad):
        """Применяет логику тарифа к объявлению"""
        pass
    def calculate_urgent_until(self, ad):
        """Общая логика для всех тарифов"""
        period = ad.product_id.period  
        duration = ad.product_id.plans.first().duration  

        if period == 'days':
            return timezone.now() + timedelta(days=duration)
        elif period == 'months':
            return timezone.now() + timedelta(days=duration * 30) 
        elif period == 'one_time':
            return timezone.now()  # Для одноразового тарифа можно установить сразу
        return timezone.now() 

class AutoUpStrategy(TariffStrategy):
    def apply(self, ad):
        """Логика для тарифа Auto Up"""
        ad.is_autoup = True
        ad.autoup_time = timezone.now().time() 
        ad.autoup_until = self.calculate_urgent_until(ad)

class PremiumStrategy(TariffStrategy):
    def apply(self, ad):
        """Логика для тарифа Premium"""
        ad.is_premium = True
        ad.premium_gradient = '#FACC00,#FFED9E'
        ad.premium_dark_gradient = '#6C2E01,#CC5803' 
        ad.premium_until = self.calculate_urgent_until(ad)

class UrgentStrategy(TariffStrategy):
    def apply(self, ad):
        """Логика для тарифа Срочно"""
        ad.is_urgent = True
        ad.urgent_until = self.calculate_urgent_until(ad)

class VipStrategy(TariffStrategy):
    def apply(self, ad):
        """Логика для тарифа VIP"""
        ad.is_vip = True
        ad.vipped_until = self.calculate_urgent_until(ad)


class HighlightStrategy(TariffStrategy):
    def apply(self, ad):
        """Логика для тарифа Выделить цветом"""
        ad.featured = True
        ad.colored_until =  self.calculate_urgent_until(ad)
        # ad.ad_color = '#FFC3C3'
        ad.ad_dark_color = '#c62925'


class TariffStrategyFactory:
    strategies = {
        "Авто UP": AutoUpStrategy(),
        "Метка Срочно": UrgentStrategy(),
        "Выделить цветом": HighlightStrategy(),
        "VIP объявление": VipStrategy(),
        "Премиум": PremiumStrategy(),
    }

    @staticmethod
    def get_strategy(tariff_name):
        """Получаем стратегию по названию тарифа."""
        return TariffStrategyFactory.strategies.get(tariff_name, None)

class Colors(models.Model):
    name = models.CharField(_('название Цвета'), max_length=50)
    color = ColorField(_("цвет"))
    dark_color = ColorField(_("темный цвет"))
    

class Plans(models.Model):
    price = models.PositiveBigIntegerField()
    duration = models.IntegerField(choices=DAY_RANGE)
    description=models.TextField(blank=True)
    cashback = models.CharField(blank=True, max_length=50)
    default = models.BooleanField(default=False)
    def __str__(self):
        return f"План на {self.id} месяцев с ценой {self.price}"
    class Meta:
        verbose_name = _("План")
        verbose_name_plural = _("Планы")
        ordering = ['id']


class Tariff(models.Model):
    name=models.CharField(max_length=50, verbose_name=_('Название тарифа'))
    description=models.TextField(blank=True,verbose_name=_('Описание'))
    img = models.ImageField(upload_to='img/tariffs/', null=True, blank=True)
    amount = models.PositiveBigIntegerField(verbose_name=_('Цена тарифа'), null=True, blank=True)
    period_choices = [
        ('one_time', 'one_time'),
        ('days', 'days'),
        ('months', 'months')
    ]
    colors = models.ManyToManyField(Colors, related_name='colors',  null=True, blank=True)
    period = models.CharField(_('Период тарифа'), choices=period_choices, max_length=50)
    plans = models.ManyToManyField(Plans, related_name='plans')
    
    
    def __str__(self):
        return f"{self.name} - {self.amount}"

    class Meta:
        verbose_name = _('Tariff Plan')
        verbose_name_plural = _('Tariff Plans')
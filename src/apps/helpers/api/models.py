from django.db import models

class Currency(models.Model):
    usd_course = models.FloatField('Курс доллара')
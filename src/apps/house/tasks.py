from celery import shared_task
import requests
from apps.helpers.api import models
from django.utils import timezone
from datetime import timedelta
from apps.house import models as house_models


@shared_task()
def get_current_cy():
    URL = 'https://data.fx.kg/api/v1/central'
    API_KEY = 'sPXfZDpimU9vmwpssT4EeFKIIWNDdPRGN3Orniue83ea15f8'

    headers = {
        'Authorization': f'Bearer {API_KEY}',
    }

    try:
        response = requests.get(URL, headers=headers)
        if response.status_code == 200:
            currency_list = response.json()
            usd_course = currency_list.get('usd')
            data_currency = models.Currency.objects.create(
                usd_course=usd_course,
            )
            data_currency.save()
            print(f'Succes saved: {data_currency}')
        else:
            return f'Error: {response.status_code}, {response.text}'
    except requests.exceptions.RequestException as e:
        return f'Exception: {str(e)}'


@shared_task
def delete_post(post_id):
    post_id = str(post_id)
    instance = house_models.Property.objects.get(id=post_id)
    if instance.active_post == False:
        date_now = timezone.now()
        if date_now - instance.updated_at >= timedelta(seconds=30):
            instance.delete()
        return None
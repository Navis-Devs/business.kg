from celery import shared_task
import requests
from apps.helpers.api import models


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

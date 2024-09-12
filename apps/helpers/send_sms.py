from django.conf import settings
from core.celery import app
import requests
import environ

env = environ.Env()

environ.Env.read_env(settings.BASE_DIR / '.env')

NIKITA_LOGIN = env('NIKITA_LOGIN')
NIKITA_PASSWORD = env('NIKITA_PASSWORD')
NIKITA_SENDER = env('NIKITA_SENDER')


@app.task(ignore_result=True)
def send_sms(phone, message):
    xml_data = f"""<?xml version="1.0" encoding="UTF-8"?><message><login>{NIKITA_LOGIN}</login><pwd>{NIKITA_PASSWORD}</pwd><sender>{NIKITA_SENDER}</sender><text>{message}</text><phones><phone>{phone}</phone></phones></message>"""
    headers = {"Content-Type": "application/xml"}
    url = "https://smspro.nikita.kg/api/message"
    response = requests.post(url, data=xml_data.encode("utf-8"), headers=headers)

    if response.status_code == 200:
        return True
    return False

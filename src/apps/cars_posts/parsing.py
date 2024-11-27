from bs4 import BeautifulSoup as BS
import requests
from .models import (
    CarMark,
    CarModel,
    CarType,
    CarModification,
    CarSerie,
    CarColors,
    CarPrices,
    Region,
    Towns,
    RegistrationCountry,
    CommentAllowed,
    Currency,
    Transmission, 
    Fuel,
    GearBox,
    SteeringWheel,
    CarGeneration,
    Exchange,
    Possibility,
    Exterior,
    Interior,
    Media,
    Safety,
    OtherOptions,
    Condition,
    FeaturedOption,
    GeneralOptions,
    Pictures
)
from apps.cars.models import CarColors, CarCharacteristic
from concurrent.futures import ThreadPoolExecutor
import csv
from django.core.exceptions import ObjectDoesNotExist
import logging
from django.core.files.base import ContentFile
from concurrent.futures import ThreadPoolExecutor
logger = logging.getLogger(__name__)

AUTH_KEY = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3MzIzODMzMTQsImV4cCI6MjA0Nzc0MzMxNCwidXNlcm5hbWUiOiI5OTY3MDkzNjIzNjAiLCJpcCI6IjE2Mi4xNTguMjIyLjE3MCIsImlkIjo5NjM3NzksInBob25lIjoiOTk2NzA5MzYyMzYwIiwibmFtZSI6IiJ9.PHKi7TMcBrQrtehXQjeeHE7-9iijStmiS6zjdQfd9qLC6gW1acClwmZDOWql-hz7osbXiESM2Yqma5gmvpmBBWULQQrvXawElHrYbXzpse04zPErd-IiX1xxgmIRmzIN_ylypcZyD9WMqkOyS0v_mAgymhObFMkj3HYtKPDlf2roxRLbUnngNLg46lTuJm-4mCN0XSCLMqoQM1uQ_r1udYmHEjOqsJY2ANZNcpiU0zSJ211Icug_JZgQiTL8MzWeAjGXgyU8VisvGCGXeS9ts2Onj7F58LDcqUNnZ6qT1_yvVqbUeZn2C5KHwx_dPqbraDkEI_eEJhM1SsDvbzR3MzJGW7kMdhfE9ELLFVFO7wpFherBN4HfmX4ubpeYIO5DCbrYwuAaCXSDLVuFF4vY9Ph6stknsn_ybU4XVDFASreX_c3AkGa3EeocVw1NyEDHfdTn3100esARUkhFj8ENYkc5ZX0TDotYhUCXwakSHcrjRLRO2wmAttT_hln9lt4A20e1U2JKGOj2Qf-XQYjEhQoFLiDd5dc7IQUB5lmEeZNk6FPGDhgBVht3fV_lm2sGFbUKxfPdR5ov7GT8Iyw8jz1v4q03HUCxp2__WjQgbMhG7kDub2ejSOg8tJkmSfxFVekcDqkwn1QzUopXYd4gNlmqAWAWVNa6V5XZjxc62EY'
AUTO_AUTH = 'Bearer o0DfPm0UNcXwHFJpeKcNu8DxEGulHpUwuyXUvmVuDepb45tkTEjM8M42uryf9SAVqwXN1ct5C'
BASE_URL = 'https://doubledragon.mashina.kg:443/v1/public/data'
headers = {'Authorization': f'Bearer {AUTH_KEY}', 'auto-auth': f'{AUTO_AUTH}'}

def upload_data():
    URL = 'https://doubledragon.mashina.kg:443/v1/public/data'
    
    headers = {
        'Authorization': f'Bearer {AUTH_KEY}',
        'auto-auth': f'{AUTO_AUTH}'
    }
    response = requests.get(URL, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
    else:
        print("STATUS CODE:", response.status_code)
        

# def upload_marks():
#     URL = 'https://doubledragon.mashina.kg:443/v1/public/data/'
#     response = requests.get(URL, headers=headers)
    
#     if response.status_code == 200:
#         print("Mark API\nOK..200")
#         data = response.json()
#         for data_list in data.get('data', {}).get('make', []):
            
#             instance_id = data_list.get('id')
#             instance_car_name = data_list.get('name')
#             instance_is_popular = bool(data_list.get('is_popular', 0))
#             logo = data_list.get('logo')
#             instance_car_type = CarType.objects.get(id=1)
#             instance_mark, created = CarMark.objects.get_or_create(
#                 id=instance_id, 
#                 defaults={
#                     "name": instance_car_name,
#                     "id_car_type": instance_car_type,
#                     "is_popular": instance_is_popular,
#                     "img": logo,
#                 }
#             )
#             for model_instance in data_list.get('models', []):
#                 id_model_instance = model_instance.get('id')
#                 name_model_instance = model_instance.get('name')
#                 instance_is_popular = bool(model_instance.get('is_popular', 0))
#                 created = CarModel.objects.get_or_create(
#                     id=id_model_instance, 
#                     id_car_mark=instance_mark,
#                     defaults={
#                         "name": name_model_instance,
#                         "is_popular": instance_is_popular,
#                     }
#                 )
#     else:
#         print("STATUS CODE:", response.status_code) 



def upload_data():
    response = requests.get(BASE_URL, headers=headers)
    if response.status_code == 200:
        data = response.json()
        data_list = data.get('data', {}).get('color', [])
        for colors in data_list:
            instance_name = colors.get('name', None)
            instance_color = colors.get('color', 'Черный')
            created = CarColors.objects.update_or_create(
                id=colors.get('id'),
                defaults={
                    "name": instance_name,
                    "color": instance_color,
                }
            )
            if created:
                print('Добавлено цвет:', instance_name)
                
        data_list = data.get('data', []).get('fuel')
        for fuel_data in data_list:
            fuel, created = Fuel.objects.get_or_create(
            id=fuel_data.get('id'),
            defaults={
                "name": fuel_data.get('name'),
                })
            if created:
                print('Добавлено trans: ', fuel)

        gear_boxes = data.get('data', {}).get('gear_box', [])
        for gear_box_data in gear_boxes:
            gear_box_obj, created = GearBox.objects.update_or_create(
                id=gear_box_data.get('id'),
                defaults={
                    "name": gear_box_data.get('name'),
                }
            )
            if created:
                print('Добавлена коробка передач: ', gear_box_obj)
                
        steering_wheels = data.get('data', {}).get('steering_wheel', [])
        for steering_wheels_data in steering_wheels:
            steering_wheels_obj, created = SteeringWheel.objects.update_or_create(
                id=steering_wheels_data.get('id'),
                defaults={
                    "name": steering_wheels_data.get('name'),
                }
            )
            if created:
                print('Добавлена коробка Руль управления: ', steering_wheels_obj)
                
        exterior = data.get('data', {}).get('exterior', [])
        for exterior_data in exterior:
            exterior_obj, created = Exterior.objects.update_or_create(
                id=exterior_data.get('id'),
                defaults={
                    "name": exterior_data.get('name'),
                }
            )
            if created:
                print('Добавлена exterior: ', exterior_obj)
                
                
        interior = data.get('data', {}).get('interior', [])
        for interior_data in interior:
            interior_obj, created = Interior.objects.update_or_create(
                id=interior_data.get('id'),
                defaults={
                    "name": interior_data.get('name'),
                }
            )
            if created:
                print('Добавлена interior: ', interior_obj)

        media = data.get('data', {}).get('media', [])
        for media_data in media:
            media_obj, created = Media.objects.update_or_create(
                id=media_data.get('id'),
                defaults={
                    "name": media_data.get('name'),
                }
            )
            if created:
                print('Добавлена media: ', media_obj)
                
        media = data.get('data', {}).get('media', [])
        for media_data in media:
            media_obj, created = Media.objects.update_or_create(
                id=media_data.get('id'),
                defaults={
                    "name": media_data.get('name'),
                }
            )
            if created:
                print('Добавлена media: ', media_obj)
                
        safety = data.get('data', {}).get('safety', [])
        for safety_data in safety:
            safety_obj, created = Safety.objects.update_or_create(
                id=safety_data.get('id'),
                defaults={
                    "name": safety_data.get('name'),
                }
            )
            if created:
                print('Добавлена safety: ', safety_obj)
                
        other_options = data.get('data', {}).get('other_option', [])
        for other_options_data in other_options:
            other_options_obj, created = OtherOptions.objects.update_or_create(
                id=other_options_data.get('id'),
                defaults={
                    "name": other_options_data.get('name'),
                }
            )
            if created:
                print('Добавлена other_options: ', other_options_obj)

        configuration = data.get('data', {}).get('configuration', [])
        for configuration_data in configuration:
            configuration_obj, created = GeneralOptions.objects.update_or_create(
                id=configuration_data.get('id'),
                defaults={
                    "name": configuration_data.get('name'),
                }
            )
            if created:
                print('Добавлена configuration: ', configuration_obj)

        car_condition = data.get('data', {}).get('car_condition', [])
        for car_condition_data in car_condition:
            car_condition_obj, created = Condition.objects.update_or_create(
                id=car_condition_data.get('id'),
                defaults={
                    "name": car_condition_data.get('name'),
                }
            )
            if created:
                print('Добавлена car_condition: ', car_condition_obj)

        featured_option = data.get('data', {}).get('featured_option', [])
        for featured_option_data in featured_option:
            featured_option_obj, created = FeaturedOption.objects.update_or_create(
                id=featured_option_data.get('id'),
                defaults={
                    "name": featured_option_data.get('name'),
                }
            )
            if created:
                print('Добавлена featured_option: ', featured_option_obj)

        registration_country = data.get('data', {}).get('registration_country', [])
        for registration_country_data in registration_country:
            registration_country_obj, created = RegistrationCountry.objects.update_or_create(
                id=registration_country_data.get('id'),
                defaults={
                    "name": registration_country_data.get('name'),
                }
            )
            if created:
                print('Добавлена registration_country: ', registration_country_obj)

        transmission = data.get('data', {}).get('transmission', [])
        for transmission_data in transmission:
            transmission_obj, created = Transmission.objects.update_or_create(
                id=transmission_data.get('id'),
                defaults={
                    "name": transmission_data.get('name'),
                }
            )
            if created:
                print('Добавлена transmission: ', transmission_obj)

        currency = data.get('data', {}).get('currency', [])
        for currency_data in currency:
            currency_obj, created = Currency.objects.update_or_create(
                id=currency_data.get('id'),
                defaults={
                    "name": currency_data.get('name'),
                    "sign": currency_data.get('sign'),
                    "is_default": bool(currency_data.get('is_default', 0))
                }
            )
            if created:
                print('Добавлена currency: ', currency_obj)

        comment_allowed = data.get('data', {}).get('comment_allowed', [])
        for comment_allowed_data in comment_allowed:
            comment_allowed_obj, created = CommentAllowed.objects.update_or_create(
                id=comment_allowed_data.get('id'),
                defaults={
                    "name": comment_allowed_data.get('name'),
                }
            )
            if created:
                print('Добавлена comment_allowed: ', comment_allowed_obj)

        exchange = data.get('data', {}).get('exchange', [])
        for exchange_data in exchange:
            exchange_obj, created = Exchange.objects.update_or_create(
                id=exchange_data.get('id'),
                defaults={
                    "name": exchange_data.get('name'),
                }
            )
            if created:
                print('Добавлена exchange: ', exchange_obj)

    else:
        print(response.status_code)

def upload_country():
    response = requests.get(BASE_URL, headers=headers)
    if response.status_code == 200:
        data = response.json()
        data_list = data.get('data', {}).get('region', [])
        for region in data_list:
            instance_id = region.get('id', 0)
            instance_name = region.get('name', None)
            region_instance, created = Region.objects.get_or_create(
                id=instance_id,
                defaults={
                    "name": instance_name
                }
            )
            if created:
                print(f'Добавлен регион: {instance_name}')
                
            town_list = region.get('towns')
            for town in town_list:
                town_id = town.get('id', 0)
                town_name = town.get('name', None)
                town_instance, created = Towns.objects.get_or_create(
                    id=town_id,
                    defaults={
                        "name": town_name,
                        "region": region_instance,
                    }
                )#file_name = image_url.split("/")[-1] if '/' in image_url else f"car_{model_instance.id}_{uuid.uuid4().hex[:8]}.jpg"
                if created:
                    print(f'Добавлен город: {town_name}')
    else:
        print("STATUS CODE:", response.status_code)
        
from .models import Currency, CarPrices, CarsPosts


def upload_cars():
    URL = 'https://doubledragon.mashina.kg:443/v1/ads/'
    response = requests.get(URL, headers=headers)
    if response.status_code == 200:
        data = response.json()
        datas = data.get('data', {})
        data_list = datas.get('list', [])
        for car_data in data_list:
            data = response.json()
            region = Region.objects.get(id=car_data.get('region'))
            town = Towns.objects.get(id=car_data.get('town'))
            registration_country = RegistrationCountry.objects.get(id=car_data.get('registration_country')) if car_data.get('registration_country') else None
            comment_allowed = CommentAllowed.objects.get(id=car_data.get('comment_allowed'))
            currency_id = Currency.objects.get(id=car_data.get('currency_id'))
            mark = CarMark.objects.get(id=80)
            model = CarModel.objects.get(id=753)
            car_type = CarType.objects.get(id=1)
            fuel =  Fuel.objects.get(id=car_data.get('fuel'))
            transmission = Transmission.objects.get(id=car_data.get('transmission'))
            # body == CarType Седан Хэтчбек Универсал Внедорожник итд.
            condition = Condition.objects.get(id=car_data.get('condition'))
            gear_box = GearBox.objects.get(id=car_data.get('gear_box'))
            steering_wheel = SteeringWheel.objects.get(id=car_data.get('steering_wheel'))
            generation_id = CarGeneration.objects.get(id=7236)
            modification_id = CarModification.objects.get(id=219930)
            serie_id = CarSerie.objects.get(id=53126)
            color = CarColors.objects.get(id=car_data.get('color'))
            exchange = Exchange.objects.get(id=car_data.get('exchange')) if car_data.get('exchange') else None
            featured_option = FeaturedOption.objects.get(id=car_data.get('featured_option'))
            customs = Possibility.objects.get(id=car_data.get('customs')) if car_data.get('customs') else None
            
            configuration = GeneralOptions.objects.filter(id__in=car_data.get('configuration'))
            exterior = Exterior.objects.filter(id__in=car_data.get('exterior'))
            interior = Interior.objects.filter(id__in=car_data.get('interior'))
            media = Media.objects.filter(id__in=car_data.get('media'))
            safety = Safety.objects.filter(id__in=car_data.get('safety'))
            other_option = OtherOptions.objects.filter(id__in=car_data.get('other_option'))
            
            
            
            model_instance, created = CarsPosts.objects.update_or_create(
                id=car_data.get('id'),
                defaults={
                    "region": region,
                    "town": town,
                    "registration_country": registration_country,
                    "comment_allowed": comment_allowed,
                    "currency": currency_id,
                    "mark": mark,
                    "model": model,
                    "car_type": car_type, # Седан Хэтчбек Универсал Внедорожник
                    "fuel": fuel,
                    "transmission": transmission,
                    "gear_box":  gear_box,
                    "steering_wheel": steering_wheel,
                    "generation_id": generation_id,
                    "modification_id": modification_id,
                    "serie_id": serie_id,
                    "color": color,
                    "exchange": exchange,
                    "car_condition": condition,
                    "featured_option": featured_option,
                    "customs": customs,
                    
                    "generation": car_data.get('generation'),
                    "modification": car_data.get('modification'),
                    "serie": car_data.get('serie'),
                    "year": car_data.get('year'),
                    "mileage": car_data.get('mileage'),
                    "engine_volume": car_data.get('engine_volume'),
                    "horse_power": car_data.get('horse_power'),
                    "description": car_data.get('description'),
                    
                }
            )          
                        
            for url in car_data.get('images', []):
                image_url = url.get('big') 
                if image_url:
                    save_image(image_url, model_instance)


            for price_response in car_data.get('prices', []):
                CarPrices.objects.create(
                    cars=model_instance,
                    price=price_response['price'],
                )
                
            if configuration.exists():
                model_instance.configuration.set(configuration)
            if exterior.exists():
                model_instance.exterior.set(exterior)
            if interior.exists():
                model_instance.interior.set(interior)
            if media.exists():
                model_instance.media.set(media)
            if safety.exists():
                model_instance.safety.set(safety)
            if other_option.exists():
                model_instance.other_options.set(other_option)

def save_image(image_url, model_instance):
    try:
        response = requests.get(image_url)
        
        if response.status_code == 200:
            filename = image_url.split('/')[-1]
            
            cars_picture = Pictures(cars=model_instance)
            
            cars_picture.pictures.save(filename, ContentFile(response.content), save=True)
            logger.info(f"Saved image {filename} for car {model_instance.id}")
        else:
            logger.error(f"Failed to fetch image: {image_url} (status code: {response.status_code})")
    except Exception as e:
        logger.error(f"Error saving image {image_url} for car {model_instance.id}: {e}")

from apps.cars.models import (
    CarGeneration,
    CarCharacteristic,
    CarCharacteristicValue,
    CarEquipment,
    CarModification,
    CarOptionValue,
    CarOption,
    CarSerie
    )


def upload_car_type():
    with open('database_auto/car_type.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        reader.fieldnames = [name.strip("'") for name in reader.fieldnames]
        for row in reader:
            row = {key.strip("'"): value.strip("'") for key, value in row.items()}
            CarType.objects.update_or_create(
                id=row['id_car_type'],
                defaults={'name': row['name']}
            )
            print(f"Successfully imported {row['name']}")


def upload_car_mark():
    with open('database_auto/car_mark.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        reader.fieldnames = [name.strip("'") for name in reader.fieldnames]
        for row in reader:
            row = {key.strip("'"): value.strip("'") for key, value in row.items()}
            
            car_type = CarType.objects.get(id=row['id_car_type'])
            
            CarMark.objects.update_or_create(
                id=row['id_car_mark'],
                defaults={
                    'name': row['name'],
                    'id_car_type': car_type,
                    'name_rus': row['name_rus'],
                }
            )
            print(f"Successfully imported {row['name']} ({row['name_rus']})")


def upload_car_model():
    with open('database_auto/car_model.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        reader.fieldnames = [name.strip("'") for name in reader.fieldnames]
        for row in reader:
            row = {key.strip("'"): value.strip("'") for key, value in row.items()}
            
            car_mark = CarMark.objects.get(id=row['id_car_mark'])
            car_type = CarType.objects.get(id=row['id_car_type'])
            
            CarModel.objects.update_or_create(
                id=row['id_car_model'],
                defaults={
                    'id_car_mark': car_mark,
                    'id_car_type': car_type,
                    'name': row['name'],
                    'name_rus': row['name_rus'],
                }
            )
            print(f"Successfully imported {row['name']} ({row['name_rus']})")


def upload_car_generation():
    with open('database_auto/car_generation.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        reader.fieldnames = [name.strip("'") for name in reader.fieldnames]
        for row in reader:
            row = {key.strip("'"): value.strip("'") for key, value in row.items()}
            car_model = CarModel.objects.get(id=row['id_car_model'])
            car_type = CarType.objects.get(id=row['id_car_type'])

            car_generation, created = CarGeneration.objects.update_or_create(
                id=row['id_car_generation'],
                defaults={
                    'name': row['name'],
                    'year_begin': row['year_begin'],
                    'year_end': row['year_end'],
                    'id_car_model': car_model,
                    'id_car_type': car_type
                }
            )
            
            if created:
                print(f"Created car generation: {car_generation.name}")
            else:
                print(f"Updated car generation: {car_generation.name}")


def upload_car_serie():
    with open('database_auto/car_serie.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        reader.fieldnames = [name.strip("'") for name in reader.fieldnames]
        for row in reader:
            row = {key.strip("'"): value.strip("'") for key, value in row.items()}
            car_model = CarModel.objects.get(id=row['id_car_model'])
            car_type = CarType.objects.get(id=row['id_car_type'])
            car_generation = CarGeneration.objects.get(id=row['id_car_generation'])

            car_serie, created = CarSerie.objects.update_or_create(
                id=row['id_car_serie'],
                defaults={
                    'name': row['name'],
                    'id_car_model': car_model,
                    'id_car_generation': car_generation,
                    'id_car_type': car_type
                }
            )
            
            if created:
                print(f"Created car serie: {car_serie.name}")
            else:
                print(f"Updated car serie: {car_serie.name}")


def upload_car_modification():
    with open('database_auto/car_modification.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        reader.fieldnames = [name.strip("'") for name in reader.fieldnames]
        for row in reader:
            row = {key.strip("'"): value.strip("'") for key, value in row.items()}
            car_modification_id = int(row['id_car_modification'])
            car_serie_id = int(row['id_car_serie'])
            car_model_id = int(row['id_car_model'])
            car_type_id = int(row['id_car_type'])

            car_serie = CarSerie.objects.get(id=car_serie_id)
            car_model = CarModel.objects.get(id=car_model_id)
            car_type = CarType.objects.get(id=car_type_id)

            car_modification, created = CarModification.objects.update_or_create(
                id=car_modification_id,
                defaults={
                    'name': row['name'],
                    'id_car_serie': car_serie,
                    'id_car_model': car_model,
                    'id_car_type': car_type,
                }
            )

            if created:
                print(f"Created car modification: {car_modification.name}")
            else:
                print(f"Updated car modification: {car_modification.name}")



def upload_car_equipment():
    with open('database_auto/car_equipment.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        reader.fieldnames = [name.strip("'") for name in reader.fieldnames]
        for row in reader:
            row = {key.strip("'"): value.strip("'") for key, value in row.items()}
            car_modification = CarModification.objects.get(id=row['id_car_modification'])
            car_type = CarType.objects.get(id=row['id_car_type'])

            price_min = None if row['price_min'].upper() == "NULL" else row['price_min']
            year = None if row['year'].upper() == "NULL" else row['year']

            car_equipment, created = CarEquipment.objects.update_or_create(
                id=row['id_car_equipment'],
                defaults={
                    'name': row['name'],
                    'id_car_modification': car_modification,
                    'price_min': price_min,
                    'id_car_type': car_type,
                    'year': year
                }
            )

            if created:
                print(f"Created car equipment: {car_equipment.name}")
            else:
                print(f"Updated car equipment: {car_equipment.name}")



def upload_car_option():
    with open('database_auto/car_option.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        reader.fieldnames = [name.strip("'") if isinstance(name, str) else name for name in reader.fieldnames]
        
        for row in reader:
            row = {key.strip("'") if isinstance(key, str) else key: (value.strip("'") if isinstance(value, str) else value) for key, value in row.items()}
            
            try:
                car_type = CarType.objects.get(id=row['id_car_type'])
            except CarType.DoesNotExist:
                print(f"CarType не нашлось {row['id_car_type']} с таким ID.")
                continue
            
            id_parent = None
            if row['id_parent'] != "NULL" and row['id_parent']:
                try:
                    id_parent = CarOption.objects.get(id=row['id_parent'])
                except CarOption.DoesNotExist:
                    print(f"Parent РОдительский мама ноу {row['id_parent']} для опции {row['name']}.")
                    id_parent = None  
            
            car_option, created = CarOption.objects.update_or_create(
                id=row['id_car_option'],
                defaults={
                    'name': row['name'],
                    'id_parent': id_parent,
                    'id_car_type': car_type,
                }
            )

            if created:
                print(f"Created car option: {car_option.name}")
            else:
                print(f"Updated car option: {car_option.name}")



def upload_car_option_value():
    with open('database_auto/car_option_value.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        reader.fieldnames = [name.strip("'") for name in reader.fieldnames]
        for row in reader:
            row = {key.strip("'"): value.strip("'") for key, value in row.items()}
            try:
                car_option = CarOption.objects.get(id=row['id_car_option'])
            except CarOption.DoesNotExist:
                print(f"CarOption не нашлось с ID {row['id_car_option']}")
                continue
            
            try:
                car_equipment = CarEquipment.objects.get(id=row['id_car_equipment'])
            except CarEquipment.DoesNotExist:
                print(f"CarEquipment не нашлось с ID {row['id_car_equipment']}")
                continue

            try:
                car_type = CarType.objects.get(id=row['id_car_type'])
            except CarType.DoesNotExist:
                print(f"CarType не нашлось с ID {row['id_car_type']}")
                car_type = None  
            
            car_option_value, created = CarOptionValue.objects.update_or_create(
                id=row['id_car_option_value'],
                defaults={
                    'is_base': row['is_base'],
                    'id_car_option': car_option,
                    'id_car_equipment': car_equipment,
                    'id_car_type': car_type,
                }
            )

            if created:
                print(f"Created car option value: {car_option_value.id}")
            # else:
            #     print(f"Updated car option value: {car_option_value.id}")
        
        
def upload_car_characteristic():
    with open('database_auto/car_characteristic.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        reader.fieldnames = [name.strip("'") if isinstance(name, str) else name for name in reader.fieldnames]

        for row in reader:
            row = {key.strip("'") if isinstance(key, str) else key: (value.strip("'") if isinstance(value, str) else value) for key, value in row.items()}
            
            try:
                car_type = CarType.objects.get(id=row['id_car_type'])
            except CarType.DoesNotExist:
                print(f"CarType не нашлось с ID {row['id_car_type']}")
                car_type = None  

            # Обрабатываем id_parent
            id_parent = None
            if row['id_parent'] != "NULL" and row['id_parent']:
                try:
                    id_parent = CarCharacteristic.objects.get(id=row['id_parent'])
                except CarCharacteristic.DoesNotExist:
                    print(f"Parent не нашлось с ID {row['id_parent']} для характеристики {row['name']}")
                    id_parent = None
            
            car_characteristic, created = CarCharacteristic.objects.update_or_create(
                id=row['id_car_characteristic'],
                defaults={
                    'name': row['name'],
                    'id_parent': id_parent,
                    'id_car_type': car_type,
                }
            )

            if created:
                print(f"Created car characteristic: {car_characteristic.name}")
            else:
                print(f"Updated car characteristic: {car_characteristic.name}")
                

def parse_nullable_value(value):
    """Converts 'NULL' or empty values to None."""
    return None if value in [None, 'NULL', ''] else value

def upload_car_characteristic_value():
    with open('database_auto/car_characteristic_value.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        reader.fieldnames = [name.strip("'") if isinstance(name, str) else name for name in reader.fieldnames]

        for row in reader:
            row = {key.strip("'") if isinstance(key, str) else key: (value.strip("'") if isinstance(value, str) else value) 
                   for key, value in row.items()}

            try:
                car_characteristic_id = parse_nullable_value(row['id_car_characteristic'])
                if car_characteristic_id and car_characteristic_id.isdigit():  
                    car_characteristic = CarCharacteristic.objects.get(id=car_characteristic_id)
                else:
                    raise ValueError(f"Invalid id_car_characteristic value: {row['id_car_characteristic']}")
            except (ValueError, ObjectDoesNotExist) as e:
                logging.error(f"Error with id_car_characteristic {row['id_car_characteristic']}: {e}")
                continue  

            try:
                car_type_id = parse_nullable_value(row['id_car_type'])
                if car_type_id:
                    car_type = CarType.objects.get(id=car_type_id)
                else:
                    car_type = None
            except CarType.DoesNotExist:
                logging.error(f"CarType not found with ID {row['id_car_type']}")
                car_type = None

            try:
                car_modification_id = parse_nullable_value(row['id_car_modification'])
                if car_modification_id:
                    car_modification = CarModification.objects.get(id=car_modification_id)
                else:
                    car_modification = None
            except CarModification.DoesNotExist:
                logging.error(f"CarModification not found with ID {row['id_car_modification']}")
                car_modification = None

            car_characteristic_value, created = CarCharacteristicValue.objects.update_or_create(
                id=row['id_car_characteristic_value'],
                defaults={
                    'value': row['value'],
                    'unit': parse_nullable_value(row['unit']),  
                    'id_car_characteristic': car_characteristic,
                    'id_car_modification': car_modification,
                    'id_car_type': car_type,
                }
            )

            if created:
                logging.info(f"Created car characteristic value: {car_characteristic_value.value}")
            else:
                logging.info(f"Updated car characteristic value: {car_characteristic_value.value}")
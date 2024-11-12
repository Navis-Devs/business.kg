from celery import shared_task
import requests
from django.utils import timezone
from datetime import timedelta
from apps.house import models as house_models
from apps.house import choices
from apps.house import data_models
from django.contrib.gis.geos import Point
import random
import os
from django.utils import translation
import json
from django.conf import settings
from apps.house import models
import traceback
from apps.accounts.models import User
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from django.conf import settings
import logging
from django.core.files.base import ContentFile
from concurrent.futures import ThreadPoolExecutor
from faker import Faker
import random


logger = logging.getLogger('django')
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def delete_post(post_id):
    post_id = str(post_id) 
    instance = house_models.Property.objects.get(id=post_id)
    if instance.active_post == False:
        date_now = timezone.now()
        if date_now - instance.updated_at >= timedelta(seconds=30):
            instance.delete()
        return None

@shared_task
def load_complex():
    URL = 'https://triplescotch.house.kg:443/v1/public/buildings/?limit=888'
    API_KEY = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXAiOjE3Mjk3MTEyODIsImV4cCI6MjA0NTA3MTI4MiwidXNlcm5hbWUiOiI5OTY3MDkzNjIzNjAiLCJpcCI6IjQ2LjI1MS4yMDYuNzkiLCJpZCI6OTM1ODYzLCJwaG9uZSI6Ijk5NjcwOTM2MjM2MCIsIm5hbWUiOiJlcmhlIn0.FQVM0c06xgSEiU8ttB3Kz3SXOgKmTUrRqVIME9Ox9WyqMRD1pi_gp5wzBJlv6HBBPWNcsZ_oAo2CCqsfdZ4HrV1X6bdfO62x-lP7nQkpIJwLCJcKkZ4aDJPZANC5ZeT8_lP-_pK9l6GQr-gGyrBbFaaRXjUZal-SqRzsVJapgI2Q3Rf7u97DKK6Bvfe2g6KHZ1cehG0g4LuexHp_o12i9OGoagRChX10OtDjCCbURC1gfYAVB7QNqJQOJTfN7PlpOhN83U-RcSY7pOPiht71_CSKrToXU7G_njF3gCTPAP3wASJwZRJjLrAAfYlo5z44GV0s39Rp6kWPRJ84YKmvEjb8GKymAAichW6Hai61bB9dltXjQ3arQds0qBTXJdZZwlRWezOEphEx5eriR9NEHHHSphh9_HV3xkWlVRFmYIdUIpjJTCGikJmch2q6J1iz9Kl6Dw81UVc1u33R0qNGJMsvYiWA5CCWIPyyR-ydjWPxs2YAzsoCcRHiicBrWGmaV11V2UDI0hx0mO73WwUsYh0zHn0PkGQpvxf2H9IP3b0QFQAmB_Wr1VAFyT8hw3h8mWM6iPvurpaep3dxc_qO0fRBvGm2OT2DuRvAQHR-oM2zq5hBOsyg7N90a8apGF1KrFDTZDBtHr5agfB8NcZxCC5ADJnZjfQvzFZQ5QuAtvM'
    AUTO_AUTH = 'o0DfPm0UNcXwHFJpeKcNu8DxEGulHpUwuyXUvmVuDepb45tkTEjM8M42uryf9SAVqwXN1ct5C'
    
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'auto-auth': AUTO_AUTH,
        'locale': 'ru',
    }
    response = requests.get(URL, headers=headers)
    
    if response.status_code == 200:
        data_list = response.json()
        
        complexes = data_list.get('data', {}).get('list', [])
                
        for complex in complexes:
            if isinstance(complex, dict):
                name = complex.get('name')
                latitude = complex.get('latitude')
                longitude = complex.get('longitude')
                floors = complex.get('floors')
                address = complex.get('address')
                street = complex.get('street')
                house_number= complex.get('house_number')
                crossing = complex.get('crossing')
                ceiling_height = complex.get('ceiling_height')
                serie = models.Serie.objects.get(id=complex.get('serie')) if complex.get('serie') else None
                type_heating = models.Heating.objects.get(id=complex.get('heating')) if complex.get('heating') else None
                completion_date = complex.get('completion_date')
                description = complex.get('description')
                object_state = models.BuildingState.objects.get(id=complex.get('state')) if complex.get('state') else None
                class_id = models.BuildingClass.objects.get(id=complex.get('class')) if complex.get('class') else None
                website = complex.get('website')
                updated_at = complex.get('updated_at')
                video = complex.get('video')
                cadastre_number = complex.get('cadastre_number')
                
                images = complex.get('images', [])
                
                image_url = images[0]['url'] if images else None
                try:
                    complex_list = house_models.Building.objects.create(
                        name=name,
                        crossing=crossing,
                        ceiling_height=ceiling_height,
                        about_complex=description,
                        object_state=object_state,
                        building_class=class_id,
                        website=website,
                        updated_at=updated_at,
                        media=video,
                        cadastre_number=cadastre_number,
                        heating=type_heating,
                        lat=latitude,
                        lon=longitude,
                        floors=floors,
                        address=address,
                        street=street,
                        serie=serie,
                        house_number=house_number,
                        completion_date=completion_date,
                    )
                    complex_list.save()
                    for price_response in complex['prices']:
                        if price_response:
                            models.BuildingPrice.objects.create(
                                building=complex_list,
                                price=price_response['price'],
                            )
                        else:
                            continue
                    for image in images:
                        image_url = image.get('url')
                        if image_url:
                            house_models.BuildingImage.objects.create(
                                complex=complex_list, 
                                image_url=image_url
                            )
                        else: 
                            continue
                except Exception as e:
                    print(f"Ошибка при создании Building: {e}")
            else:
                print(f"Ошибка: ожидается словарь, но получена {type(complex).__name__}: {complex}")
    else:
        print(f"Server stopped {response.status_code} with error: {response.text}")
        

@shared_task
def load_data(languages):
    URL = 'https://triplescotch.house.kg:443/v1/public/data'
    API_KEY = 'o0DfPm0UNcXwHFJpeKcNu8DxEGulHpUwuyXUvmVuDepb45tkTEjM8M42uryf9SAVqwXN1ct5C'
    
    headers = {
        "auto-auth": f"Bearer {API_KEY}",
    }
    
    models_mapping = {
        'type': data_models.Type,
        'category': data_models.Category,
        'account_type': data_models.AccountType,
        'floor': data_models.Floor,
        'serie': data_models.Serie,
        'material': data_models.Material,
        'building': models.Building,
        'options': data_models.Options,
        'rooms': data_models.Rooms,
        'condition': data_models.Condition,
        'document': data_models.Document,
        'phone_info': data_models.Phone,
        'internet': data_models.Internet,
        'toilet': data_models.Toilet,
        'canalization': data_models.Canalization,
        'water': data_models.Water,
        'electricity': data_models.Electricity,
        'heating': data_models.Heating,
        'gas': data_models.Gas,
        'balcony': data_models.Balcony,
        'currency': data_models.Currency,
        'door': data_models.Door,
        'parking': data_models.Parking,
        'safety': data_models.Safety,
        'furniture': data_models.Furniture,
        'flooring': data_models.Flooring,
        'exchange': data_models.Exchange,
        'rental_term': data_models.RentalTerm,
        'comment_allowed': data_models.CommentAllowed,
        'building_type': data_models.BuildingType,
        'irrigation': data_models.Irrigation,
        'land_amenities': data_models.LandAmenities,
        'land_location': data_models.LandLocation,
        'land_options': data_models.LandOptions,
        'building_class': data_models.BuildingClass,
        'building_state': data_models.BuildingState,
        'finishing': data_models.Finishing,
        'parking_type': data_models.ParkingType,
        'commercial_type': data_models.CommercialType,
        'installment': data_models.Installment,
        'room_location': data_models.RoomLocation,
        'room_option': data_models.RoomOption,
        'flat_options': data_models.FlatOptions,
        
    }
    for language in languages:
        headers["locale"] = language  
        
        response = requests.get(URL, headers=headers)
        try:
            if response.status_code == 200:
                data = response.json()
                for model_key, model_class in models_mapping.items():
                    items = data.get('data', {}).get(model_key, [])
                    for item in items:
                        translation.activate(language)  
                        # print(model_class.__name__) для отладки имя модели которое происходит ограничение
                        obj, created = model_class.objects.get_or_create(
                            id=item['id'], 
                        )
                        if created:
                            obj.set_current_language(language)
                            obj.name = item['name']
                            obj.save()
                        else:
                            obj.set_current_language(language)
                            obj.name = item['name']
                            obj.save()
                        
                        if model_key == 'currency':
                            obj.name = item.get('name', '')
                            obj.sign = item.get('sign', '')
                            obj.is_default = item.get('is_default', 0)
                            obj.save()
                            
                    translation.deactivate()  
            else:
                print('Диннах', response.status_code)
        except Exception as e:
            print(f"error occured: {e}")

@shared_task
def load_location():
    URL = 'https://triplescotch.house.kg:443/v1/public/data'
    API_KEY = 'o0DfPm0UNcXwHFJpeKcNu8DxEGulHpUwuyXUvmVuDepb45tkTEjM8M42uryf9SAVqwXN1ct5C'
    
    headers = {
        "auto-auth": f"Bearer {API_KEY}",
        'locale': 'ru'
    }
    
    try:
        response = requests.get(URL, headers=headers)
        response.raise_for_status() 
        
        data = response.json()

        regions = data.get('data', {}).get('region', [])

        for region_data in regions:
            region, _ = data_models.Region.objects.get_or_create(
                id=region_data['id'],
                defaults={
                    'name': region_data['name'],
                    'slug': region_data['slug'],
                    'status': bool(region_data['status']),
                    'latitude': region_data['latitude'],
                    'longitude': region_data['longitude'],
                    'zoom': region_data['zoom'],
                    'map': region_data['map'],
                }
            )

            for town_data in region_data.get('towns', []):
                town, _ = data_models.Town.objects.get_or_create(
                    id=town_data['id'],
                    defaults={
                        'name': town_data['name'],
                        'slug': town_data['slug'],
                        'status': bool(town_data['status']),
                        'latitude': town_data['latitude'],
                        'longitude': town_data['longitude'],
                        'zoom': town_data['zoom'],
                        'map': town_data['map'],
                        'region': region
                    }
                )

                for district_data in town_data.get('districts', []):
                    district, _ = data_models.District.objects.get_or_create(
                        id=district_data['id'],
                        defaults={
                            'name': district_data['name'],
                            'slug': district_data['slug'],
                            'status': bool(district_data['status']),
                            'latitude': district_data['latitude'],
                            'longitude': district_data['longitude'],
                            'zoom': district_data['zoom'],
                            'town': town
                        }
                    )

                    for micro_district_data in district_data.get('micro_districts', []):
                        data_models.MicroDistrict.objects.get_or_create(
                            id=micro_district_data['id'],
                            defaults={
                                'name': micro_district_data['name'],
                                'slug': micro_district_data.get('slug'),
                                'status': bool(micro_district_data['status']),
                                'latitude': micro_district_data['latitude'],
                                'longitude': micro_district_data['longitude'],
                                'zoom': micro_district_data['zoom'],
                                'district': district
                            }
                        )

    except requests.exceptions.RequestException as e:
        print(f"Error request data from API: {e}")
        

@shared_task
def load_properties():
    URL = 'http://triplescotch.house.kg/v1/ads/?limit=100000'
    API_KEY = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3Mjk3MTEyODIsImV4cCI6MjA0NTA3MTI4MiwidXNlcm5hbWUiOiI5OTY3MDkzNjIzNjAiLCJpcCI6IjQ2LjI1MS4yMDYuNzkiLCJpZCI6OTM1ODYzLCJwaG9uZSI6Ijk5NjcwOTM2MjM2MCIsIm5hbWUiOiJlcmhlIn0.FQVM0c06xgSEiU8ttB3Kz3SXOgKmTUrRqVIME9Ox9WyqMRD1pi_gp5wzBJlv6HBBPWNcsZ_oAo2CCqsfdZ4HrV1X6bdfO62x-lP7nQkpIJwLCJcKkZ4aDJPZANC5ZeT8_lP-_pK9l6GQr-gGyrBbFaaRXjUZal-SqRzsVJapgI2Q3Rf7u97DKK6Bvfe2g6KHZ1cehG0g4LuexHp_o12i9OGoagRChX10OtDjCCbURC1gfYAVB7QNqJQOJTfN7PlpOhN83U-RcSY7pOPiht71_CSKrToXU7G_njF3gCTPAP3wASJwZRJjLrAAfYlo5z44GV0s39Rp6kWPRJ84YKmvEjb8GKymAAichW6Hai61bB9dltXjQ3arQds0qBTXJdZZwlRWezOEphEx5eriR9NEHHHSphh9_HV3xkWlVRFmYIdUIpjJTCGikJmch2q6J1iz9Kl6Dw81UVc1u33R0qNGJMsvYiWA5CCWIPyyR-ydjWPxs2YAzsoCcRHiicBrWGmaV11V2UDI0hx0mO73WwUsYh0zHn0PkGQpvxf2H9IP3b0QFQAmB_Wr1VAFyT8hw3h8mWM6iPvurpaep3dxc_qO0fRBvGm2OT2DuRvAQHR-oM2zq5hBOsyg7N90a8apGF1KrFDTZDBtHr5agfB8NcZxCC5ADJnZjfQvzFZQ5QuAtvM'
    AUTO_AUTH = 'o0DfPm0UNcXwHFJpeKcNu8DxEGulHpUwuyXUvmVuDepb45tkTEjM8M42uryf9SAVqwXN1ct5C'
    
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'auto-auth': AUTO_AUTH,
    }
    response = requests.get(URL, headers=headers)
    try:
        if response.status_code == 200:
            data_list = response.json()
            properties = data_list.get('data', {}).get('list', [])
            for property in properties:
                user_ids = list(User.objects.values_list('id', flat=True))
                random_user_id = random.choice(user_ids)
                category_instance = models.Category.objects.get(id=property.get('category'))
                type_instance = models.Type.objects.get(id=property.get('type_id'))
                rooms_instance = models.Rooms.objects.get(id=property.get('rooms')) if property.get('rooms') else None 
                serie_instance = models.Serie.objects.get(id=property.get('serie')) if property.get('serie') else None
                material_instance = models.Material.objects.get(id=property.get('material')) if property.get('material') else None
                rental_term_instance = models.RentalTerm.objects.get(id=property.get('rental_term')) if property.get('rental_term') else None
                water_instance = models.Water.objects.get(id=property.get('water')) if property.get('water') else None
                irrigation_instance = models.Irrigation.objects.get(id=property.get('irrigation')) if property.get('irrigation') else None
                building_type_instance = models.BuildingType.objects.get(id=property.get('building_type')) if property.get('building_type') else None
                floor_instance = models.Floor.objects.get(id=property.get('floor')) if property.get('floor') else None
                floors_instance = models.Floor.objects.get(id=property.get('floors')) if property.get('floors') else None
                flooring_instance = models.Flooring.objects.get(id=property.get('flooring')) if property.get('flooring') else None
                heating_instance = models.Heating.objects.get(id=property.get('heating')) if property.get('heating') else None
                condition_instance = models.Condition.objects.get(id=property.get('condition')) if property.get('condition') else None
                region_instance = models.Region.objects.get(id=property.get('region')) if property.get('region') else None
                town_instance = models.Town.objects.get(id=property.get('town')) if property.get('town') else None
                district_instance = models.District.objects.get(id=property.get('district')) if property.get('district') else None
                microdistrict_instance = models.MicroDistrict.objects.get(id=property.get('micro_district')) if property.get('micro_district') else None
                currency_instance = models.Currency.objects.get(id=property.get('currency_id')) if property.get('currency_id') else None
                exchange_instance = models.Exchange.objects.get(id=property.get('exchange')) if property.get('exchange') else None
                installment_instance = models.Possibility.objects.get(id=property.get('installment')) if property.get('installment') else None
                mortgage_instance = models.Possibility.objects.get(id=property.get('mortgage')) if property.get('mortgage') else None
                owner_type_instance = models.AccountType.objects.get(id=property.get('owner_type')) if property.get('owner_type') else None
                price_for_instance = models.PriceType.objects.get(id=random.randint(1, 2))
                complex_instance = models.Building.objects.get(id=property.get('building_id')) if property.get('building_id') else None
                land_amenities_instance = models.LandAmenities.objects.filter(id__in=property.get('land_amenities')) if property.get('land_amenities') else None
                document_instance = models.Document.objects.filter(id__in=property.get('document')) if property.get('document') else None
                phone_info_instance = models.Phone.objects.get(id=property.get('phone_info')) if property.get('phone_info') else None
                canalization_instance = models.Canalization.objects.get(id=property.get('canalization')) if property.get('canalization') else None
                electricity_instance = models.Electricity.objects.get(id=property.get('electricity')) if property.get('electricity') else None
                room_location_instance = models.RoomLocation.objects.get(id=property.get('room_location')) if property.get('room_location') else None
                toilet_instance = models.Toilet.objects.get(id=property.get('toilet')) if property.get('toilet') else None
                parking_instance = models.Parking.objects.get(id=property.get('parking')) if property.get('parking') else None
                parking_type_instance = models.ParkingType.objects.get(id=property.get('parking_type')) if property.get('parking_type') else None
                door_instance = models.Door.objects.get(id=property.get('door')) if property.get('door') else None
                comment_allowed_instance = models.CommentAllowed.objects.get(id=property.get('comment_allowed')) if property.get('comment_allowed') else None
                commercial_type_instance = models.CommercialType.objects.get(id=property.get('commercial_type')) if property.get('commercial_type') else None
                internet_instance = models.Internet.objects.get(id=property.get('internet')) if property.get('internet') else None
                gas_instance = models.Gas.objects.get(id=property.get('gas')) if property.get('gas') else None
                balcony_instance = models.Balcony.objects.get(id=property.get('balcony')) if property.get('balcony') else None
                furniture_instance = models.Furniture.objects.get(id=property.get('furniture')) if property.get('furniture') else None
                
                options_instance = models.Options.objects.filter(id__in=property.get('options')) if property.get('options') else None
                room_options_instance = models.RoomOption.objects.filter(id__in=property.get('room_option')) if property.get('room_option') else None
                safety_instance = models.Safety.objects.filter(id__in=property.get('safety')) if property.get('safety') else None
                flat_options_instance = models.FlatOptions.objects.filter(id__in=property.get('flat_options')) if property.get('flat_options') else None
                land_options_instance = models.LandOptions.objects.filter(id__in=property.get('land_options')) if property.get('land_options') else None
                land_location_instance = models.LandLocation.objects.get(id=property.get('land_location')) if property.get('land_location') else None
                longitude = property.get('longitude')
                latitude = property.get('latitude')
                phones = property.get('phones', [])
                point = Point(longitude, latitude)
                property_instance = models.Property.objects.create(
                    user_id=random_user_id,
                    type_id=type_instance,
                    category=category_instance,
                    rooms=rooms_instance,
                    material=material_instance,
                    water=water_instance,
                    irrigation=irrigation_instance,
                    rental_term=rental_term_instance,
                    owner_type=owner_type_instance,
                    floor=floor_instance,
                    floors=floors_instance,
                    complex_id=complex_instance,
                    building_type=building_type_instance,
                    serie=serie_instance,
                    price_for=price_for_instance,
                    flooring=flooring_instance,
                    heating=heating_instance,
                    condition=condition_instance,
                    region=region_instance,
                    district=district_instance,
                    town=town_instance,
                    microdistrict=microdistrict_instance,
                    point=point,
                    currency=currency_instance,
                    mortgage=mortgage_instance,
                    installment=installment_instance,
                    exchange=exchange_instance,
                    land_location=land_location_instance,
                    phone_info=phone_info_instance,
                    canalization=canalization_instance,
                    electricity=electricity_instance,
                    room_location=room_location_instance,
                    toilet=toilet_instance,
                    parking=parking_instance,
                    parking_type=parking_type_instance,
                    door=door_instance,
                    comment_allowed=comment_allowed_instance,
                    commercial_type=commercial_type_instance,
                    internet=internet_instance,
                    gas=gas_instance,
                    balkony=balcony_instance,
                    furniture=furniture_instance,
                    land_square=property.get('land_square'),
                    living_square=property.get('living_square'),
                    kitchen_square=property.get('kitchen_square'),
                    ceiling_height=property.get('ceiling_height'),
                    square=property.get('square'),
                    year=property.get('year'),
                    cadastre_number=property.get('cadastre_number'),
                    house_number=property.get('house_number'),
                    crossing=property.get('crossing'),
                    youtube_url=property.get('video_url'),
                    description=property.get('description'),
                    street=property.get('address')
                )
                
                def save_image(cleaned_url, property_instance):
                    response = requests.get(cleaned_url)
                    if response.status_code == 200:
                        filename = cleaned_url.split('/')[-1]
                        property_picture = models.Pictures.objects.create(property=property_instance)
                        property_picture.pictures.save(filename, ContentFile(response.content), save=True)
                with ThreadPoolExecutor(max_workers=5) as executor:
                    executor.map(lambda url: save_image(url, property_instance), [img['big'] for img in property['images']])
                  
                for price_response in property['prices']:
                    models.Price.objects.create(
                        property=property_instance,
                        price=price_response['price'],
                        m2_price=price_response['m2_price']
                    )
                if phones:
                    models.Phones.objects.create(
                        property=property_instance,
                        phones=phones 
                    )
                
                property_instance.options.set(options_instance)
                property_instance.land_amenities.set(land_amenities_instance)
                property_instance.safety.set(safety_instance)
                property_instance.room_options.set(room_options_instance)
                property_instance.land_options.set(land_options_instance)
                property_instance.documents.set(document_instance),
                property_instance.flat_options.set(flat_options_instance)

            #     # user #
                
                
                # fake = Faker()
                # user_image = property.get('user_image')
                # user_name = property.get('user_name')
                # fake_email = fake.ascii_email()
                # fake_username = fake.name()
                # avatar = user_image if user_image else None
                
                # User.objects.get_or_create(
                #     phone=phone,
                #     name=user_name,
                #     defaults={
                #         'email': fake_email,
                #         '_avatar': avatar,
                #         'is_active': True,
                #         'username': f"{fake_username} - {random.randint(111_111, 999_999)}"
                #     }
                # )
                
                
                
    except Exception as e:
        traceback.print_exc() 
        print(f'Братан что то упустил: \n {e}')
# from bs4 import BeautifulSoup as BS
# import re
# import requests
# from django.contrib.auth import get_user_model
# from .models import CarsPosts, Exterior, Interior, Media, Security, GeneralOptions
# from apps.cars.models import CarColors, CarMark, CarModel, CarType
# from apps.helpers.choices import *
# User = get_user_model()

# fuel_type_map = {
#     "Бензин": FuelType.GASOLINE,
#     "Газ": FuelType.GAS,
#     "Дизель": FuelType.DIESEL,
#     "Гибрид": FuelType.HYBRID,
#     "Электро": FuelType.ELECTRIC,
# }

# drive_type_map = {
#     "Полный": DriveType.AWD,
#     "Полный подключаемый": DriveType.PART_TIME_AWD,
#     "Задний": DriveType.RWD,
#     "Передний": DriveType.FWD
# }

# transmission_type_map = {
#     "Механика": TransmissionType.MANUAL,
#     "Автомат": TransmissionType.AUTOMATIC,
#     "Робот": TransmissionType.ROBOTIC,
#     "Вариатор": TransmissionType.CVT,
# }

# condition_type_map = {
#     "хорошее": CarCondition.GOOD,
#     "идеальное": CarCondition.PERFECT,
#     "аварийное / не на ходу": CarCondition.SALVAGE,
#     "новое": CarCondition.NEW
# }

# availability_status_map = {
#     "в наличии": AvailabilityStatus.IN_STOCK,
#     "на заказ": AvailabilityStatus.PRE_ORDER,
#     "в пути": AvailabilityStatus.IN_TRANSIT,
# }

# def core():
#     url = "https://doubledragon.mashina.kg:443/v1/ads?filter=%7B%22type_id%22:[%7B%22value%22:%221%22,%22operator%22:%22=%22%7D]%7D&limit=50&source=1&orderby=created_date&sort=desc&offset=20"
#     url_detail = "https://doubledragon.mashina.kg:443/v1/ads/2418392"
#     header = {
#         "locale": "ru",
#         "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3MzIzODMzMTQsImV4cCI6MjA0Nzc0MzMxNCwidXNlcm5hbWUiOiI5OTY3MDkzNjIzNjAiLCJpcCI6IjE2Mi4xNTguMjIyLjE3MCIsImlkIjo5NjM3NzksInBob25lIjoiOTk2NzA5MzYyMzYwIiwibmFtZSI6IiJ9.PHKi7TMcBrQrtehXQjeeHE7-9iijStmiS6zjdQfd9qLC6gW1acClwmZDOWql-hz7osbXiESM2Yqma5gmvpmBBWULQQrvXawElHrYbXzpse04zPErd-IiX1xxgmIRmzIN_ylypcZyD9WMqkOyS0v_mAgymhObFMkj3HYtKPDlf2roxRLbUnngNLg46lTuJm-4mCN0XSCLMqoQM1uQ_r1udYmHEjOqsJY2ANZNcpiU0zSJ211Icug_JZgQiTL8MzWeAjGXgyU8VisvGCGXeS9ts2Onj7F58LDcqUNnZ6qT1_yvVqbUeZn2C5KHwx_dPqbraDkEI_eEJhM1SsDvbzR3MzJGW7kMdhfE9ELLFVFO7wpFherBN4HfmX4ubpeYIO5DCbrYwuAaCXSDLVuFF4vY9Ph6stknsn_ybU4XVDFASreX_c3AkGa3EeocVw1NyEDHfdTn3100esARUkhFj8ENYkc5ZX0TDotYhUCXwakSHcrjRLRO2wmAttT_hln9lt4A20e1U2JKGOj2Qf-XQYjEhQoFLiDd5dc7IQUB5lmEeZNk6FPGDhgBVht3fV_lm2sGFbUKxfPdR5ov7GT8Iyw8jz1v4q03HUCxp2__WjQgbMhG7kDub2ejSOg8tJkmSfxFVekcDqkwn1QzUopXYd4gNlmqAWAWVNa6V5XZjxc62EY",
#         "auto-auth": "Bearer o0DfPm0UNcXwHFJpeKcNu8DxEGulHpUwuyXUvmVuDepb45tkTEjM8M42uryf9SAVqwXN1ct5C"
#     }

#     response = requests.get(url=url_detail, headers=header).json()
#     print(response)
#     my_data = {}

#     if response.get("outcome") != "success":
#         print("Not success request")
#     else:
#         data = response.get("data")
#         if data.get("status") == 5:
#             # parsing from html
#             html_url = f"https://www.mashina.kg/details/{data.get('slug')}"
#             html_response = requests.get(html_url)
#             soup = BS(html_response.text, 'lxml')
#             items = soup.find('div', class_="tab-pane fade in active")
#             breadcrumbs = soup.find('ol', class_='breadcrumbs details-breadcrumb')
#             if breadcrumbs:
#                 third_element = breadcrumbs.find_all('li')[2]
#                 mark = third_element.find('span', itemprop='name').text if third_element else None

#             if breadcrumbs:
#                 third_element = breadcrumbs.find_all('li')[3]
#                 model = third_element.find('span', itemprop='name').text if third_element else None

#             if items:
#                 color_row = items.find_all("div", class_="field-row clr")[3]
#                 field_value = color_row.find("div", class_="field-value")
#                 if field_value:
#                     color_icon = field_value.find("i", class_="color-icon")
#                     color_name = field_value.text.strip()
#                     color_code = color_icon['data-color']


#             ''' personal info '''
#             id = data.get("id")
#             user_id = data.get("user_hash")
#             user_name = data.get("user_name")
#             user_phone = int(data.get("phone"))
#             print("ID:", id)

#             ''' car info '''
#             registration = "Kyrgyzstan" if data.get("registration_country") == 1 else "Another country"
#             # my_data["images"] = [i.get("medium") for i in data.get("images")]
#             currency = "USD" if data.get("currency_id") == 2 else "SOM"
#             price = next((i.get('price') for i in data.get("prices") if i.get('id') == data.get("currency_id")), None)

#             year = data.get("year")
#             serie = next((char.get("value") for char in data.get("characteristics", []) if char.get("name") == "Тип кузова"), None)
#             serie = re.sub(r'\s*\d+\s*дв\.', '', serie)
#             engine = next((char.get("value") for char in data.get("characteristics", []) if char.get("name") == "Тип двигателя"), None)
#             engine = fuel_type_map.get(engine)
#             drivetype = next((char.get("value") for char in data.get("characteristics", []) if char.get("name") == "Привод"), None)
#             drivetype = drive_type_map.get(drivetype)
#             if items:
#                 gear_row = items.find_all("div", class_="field-row clr")[5]
#                 field_value = gear_row.find('div', class_="field-value")
#                 if field_value:
#                     gear_box = field_value.text.strip().capitalize()
#                     gear_box = transmission_type_map.get(gear_box)
#             steering_wheel = SteeringWheelPosition.LEFT if data.get("steering_wheel") == 1 else SteeringWheelPosition.RIGHT
#             if items:
#                 condition_row = items.find_all("div", class_="field-row clr")[8]
#                 field_value = condition_row.find('div', class_="field-value")
#                 if field_value:
#                     condition = field_value.text.strip()
#                     condition = condition_type_map.get(condition)
#             mileage = data.get("mileage")
#             if items:
#                 mileage_row = items.find_all("div", class_="field-row clr")[1]
#                 field_value = mileage_row.find('div', class_="field-value")
#                 if field_value:
#                     mileage_unit = MileageUnit.KILOMETERS if field_value.text.strip()[-2:] == "км" else MileageUnit.MILES
#             description = data.get("description")
#             if items:
#                 available_row = items.find_all("div", class_="field-row clr")[11]
#                 field_value = available_row.find('div', class_="field-value")
#                 if field_value:
#                     availability = field_value.text.strip()
#                     availability = availability_status_map.get(availability)
#             if items:
#                 cc_row = items.find_all("div", class_="field-row clr")[9]
#                 field_value = cc_row.find('div', class_="field-value")
#                 if field_value:
#                     cc = field_value.text.strip()
#                     cc = True if cc == "растаможен" else False


#             ''' USER '''
#             user, created = User.objects.get_or_create(
#                 mkg_id=user_id,
#                 defaults={'phone': user_phone, 'name': user_name}
#             )
#             if created:
#                 user.username = User.generate_unique_username()
#                 user.save()


#             ''' OBJECTS '''
#             car_type = CarType.objects.get(name="легковые")
#             mark = CarMark.objects.get(name=mark)
#             model = CarModel.objects.get(name=model)
#             color, created = CarColors.objects.get_or_create(id=color_code, name=color_name)


#             exterior = Exterior.objects.create()
#             interior = Interior.objects.create()
#             media = Media.objects.create()
#             security = Security.objects.create()
#             options = GeneralOptions.objects.create()

#             car, created = CarsPosts.objects.update_or_create(
#                 mkg_id=id, user=user,
#                 defaults=
#                 {
#                     "registration": registration,
#                     "currency": currency,
#                     "price": price,

#                     "car_type": car_type,
#                     "mark": mark,
#                     "model": model,
#                     "year": year,
#                     "serie": serie,
#                     "engine": engine,
#                     "drive": drivetype,
#                     "transmission": gear_box,
#                     "steering_wheel": steering_wheel,
#                     "color": color,
#                     "condition": condition,
#                     "mileage": mileage,
#                     "mileage_unit": mileage_unit,
#                     "description": description,
#                     "availability": availability,
#                     "customs_cleared": cc,

#                     "exterior": exterior,
#                     "interior": interior,
#                     "media": media,
#                     "security": security,
#                     "options": options
#                 }
#             )
#         else:
#             None

#     print(my_data)

# docker exec -it web python manage.py shell -c "from apps.cars_posts.parsing_v2 import core; core()"
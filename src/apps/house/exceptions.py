# from apps.house import data_serializers
# from django.utils import translation
# from apps.house import data_models
# translation.activate('en')

# rooms_queryset = data_models.Rooms.objects.all()
# rooms_serialized = data_serializers.RoomsSerializer(rooms_queryset, many=True).data
# rooms_data = [{'id': item['id'], 'name': item['name']} for item in rooms_serialized]

# material_queryset = data_models.Material.objects.all()
# material_serialized = data_serializers.MaterialSerializer(material_queryset, many=True).data
# material_data = [{'id': item['id'], 'name': item['name']} for item in material_serialized]

# floors_queryset = data_models.Floor.objects.all()
# floors_serialized = data_serializers.FloorsSerializer(floors_queryset, many=True).data
# floors_data = [{'id': item['id'], 'name': item['name']} for item in floors_serialized]

# condition_queryset = data_models.Condition.objects.all()
# condition_serialized = data_serializers.ConditionSerializer(condition_queryset, many=True).data
# condition_data = [{'id': item['id'], 'name': item['name']} for item in condition_serialized]

# owner_queryset = data_models.AccountType.objects.all()
# owner_serialized = data_serializers.OwnerSerializer(owner_queryset, many=True).data
# owner_data = [{'id': item['id'], 'name': item['name']} for item in owner_serialized]

# heating_queryset = data_models.Heating.objects.all()
# heating_serialized = data_serializers.HeatingSerializer(heating_queryset, many=True).data
# heating_data = [{'id': item['id'], 'name': item['name']} for item in heating_serialized]

# phone_info_queryset = data_models.Phone.objects.all()
# phone_info_serialized = data_serializers.PhoneInfoSerializer(phone_info_queryset, many=True).data
# phone_info_data = [{'id': item['id'], 'name': item['name']} for item in phone_info_serialized]

# internet_queryset = data_models.Internet.objects.all()
# internet_serialized = data_serializers.InternetSerializer(internet_queryset, many=True).data
# internet_data = [{'id': item['id'], 'name': item['name']} for item in internet_serialized]

# toilet_queryset = data_models.Toilet.objects.all()
# toilet_serialized = data_serializers.ToiletSerializer(toilet_queryset, many=True).data
# toilet_data = [{'id': item['id'], 'name': item['name']} for item in toilet_serialized]

# gas_queryset = data_models.Gas.objects.all()
# gas_serialized = data_serializers.GasSerializer(gas_queryset, many=True).data
# gas_data = [{'id': item['id'], 'name': item['name']} for item in gas_serialized]

# balcony_queryset = data_models.Balcony.objects.all()
# balcony_serialized = data_serializers.BalconySerializer(balcony_queryset, many=True).data
# balcony_data = [{'id': item['id'], 'name': item['name']} for item in balcony_serialized]

# door_queryset = data_models.Door.objects.all()
# door_serialized = data_serializers.DoorSerializer(door_queryset, many=True).data
# door_data = [{'id': item['id'], 'name': item['name']} for item in door_serialized]

# price_type_queryset = data_models.PriceType.objects.all()
# price_type_serialized = data_serializers.PriceTypeSerializer(price_type_queryset, many=True).data
# price_type_data = [{'id': item['id'], 'name': item['name']} for item in price_type_serialized]

# parking_queryset = data_models.Parking.objects.all()
# parking_serialized = data_serializers.ParkingSerializer(parking_queryset, many=True).data
# parking_data = [{'id': item['id'], 'name': item['name']} for item in parking_serialized]

# flooring_queryset = data_models.Flooring.objects.all()
# flooring_serialized = data_serializers.FlooringSerializer(flooring_queryset, many=True).data
# flooring_data = [{'id': item['id'], 'name': item['name']} for item in flooring_serialized]

# flooring_queryset = data_models.Flooring.objects.all()
# flooring_serialized = data_serializers.FlooringSerializer(flooring_queryset, many=True).data
# flooring_data = [{'id': item['id'], 'name': item['name']} for item in flooring_serialized]

# furniture_queryset = data_models.Furniture.objects.all()
# furniture_serialized = data_serializers.FurnitureSerializer(furniture_queryset, many=True).data
# furniture_data = [{'id': item['id'], 'name': item['name']} for item in furniture_serialized]

# safety_queryset = data_models.Safety.objects.all()
# safety_serialized = data_serializers.FurnitureSerializer(safety_queryset, many=True).data
# safety_data = [{'id': item['id'], 'name': item['name']} for item in safety_serialized]

# flat_options_queryset = data_models.FlatOptions.objects.all()
# flat_options_serialized = data_serializers.FlatOptionsSerializer(flat_options_queryset, many=True).data
# flat_options_data = [{'id': item['id'], 'name': item['name']} for item in flat_options_serialized]

# document_queryset = data_models.Document.objects.all()
# document_serialized = data_serializers.DocumentSerializer(flat_options_queryset, many=True).data
# document_data = [{'id': item['id'], 'name': item['name']} for item in document_serialized]

# comment_allowed_queryset = data_models.CommentAllowed.objects.all()
# comment_allowed_serialized = data_serializers.DocumentSerializer(comment_allowed_queryset, many=True).data
# commed_allowed_data = [{'id': item['id'], 'name': item['name']} for item in comment_allowed_serialized]

# exchange_queryset = data_models.Exchange.objects.all()
# exchange_serialized = data_serializers.ExchangeSerializer(exchange_queryset, many=True).data
# exchange_data = [{'id': item['id'], 'name': item['name']} for item in exchange_serialized]

# currency_queryset = data_models.Currency.objects.all()
# currency_serialized = data_serializers.CurrencySerializer(currency_queryset, many=True).data
# currency_data = [{'id': item['id'], 'name': item['name'], 'sign': item['sign']} for item in currency_serialized]

# possibility_queryset = data_models.Possibility.objects.all()
# possibility_serialized = data_serializers.PosibilitySerializer(possibility_queryset, many=True).data
# possibility_data = [{'id': item['id'], 'name': item['name']} for item in possibility_serialized]

# regions_queryset = data_models.Region.objects.all()
# regions_data = data_serializers.RegionsSerializer(regions_queryset, many=True).data


# def get_town_data(region_id):
#     """Возвращает данные о городах по region_id"""
#     if not region_id:
#         return []

#     town_queryset = data_models.Town.objects.filter(region_id=region_id)
#     town_data = data_serializers.TownsSerializer(town_queryset, many=True).data
#     return town_data

# def get_disctrict_data(town_id):
#     """Возвращает данные о районах по town_id"""
#     if not town_id:
#         return None
#     disctrict_queryset = data_models.District.objects.filter(town_id=town_id)
#     disctrict_data = data_serializers.DistrictSerializer(disctrict_queryset, many=True).data
#     return disctrict_data

# def get_validation_rules(region_id, town_id=None):
#     """Возвращает правила валидации, включая данные по городам и районам"""
#     district_required = False   
#     disctrict_data = []
    
#      # Если town_id задан, проверяем наличие районов и получаем данные cвязаннные обьекты с этим
#     if town_id:
#         district_required = data_models.District.objects.filter(town_id=town_id).exists()
#         disctrict_data = get_disctrict_data(town_id)
    
#     # Получаем данные о городах по region_id #
#     town_data = get_town_data(region_id)
    
#     # ПРИМЕР ЗАПРОСА: &region_id=1(Чуйская область)&town_id=2 # Бишкек
    
#     return {
#     'sell': {
#         'house': [
#             {'name': 'rooms', 'type': 'integer', "required": True, 'data': rooms_data},
#             {'name': 'material', 'type': 'integer', "required": True, 'data': material_data},
#             {'name': 'floor', 'type': 'integer', "required": False, 'data': floors_data},
#             {'name': 'year', 'type': 'integer', "required": False, 'data': None},
#             {'name': 'land_square', 'type': 'integer', "required": True, 'data': None},
#             {'name': 'living_square', 'type': 'integer', "required": False, 'data': None},
#             {'name': 'kitchen_square', 'type': 'integer', "required": False, 'data': None},
#             {'name': 'square', 'type': 'integer', "required": True, 'data': None},
#             {'name': 'condition', 'type': 'integer', "required": True, 'data': condition_data},
#             {'name': 'heating', 'type': 'integer', "required": False, 'data': heating_data},
#             {'name': 'cadastre_number', 'type': 'integer', 'required': False, "data": None},
#             {'name': 'region', 'type': 'integer', 'required': True, "data": regions_data},
#             {'name': 'town', 'type': 'integer', 'required': True, "data": town_data},
#             {'name': 'disctrict', 'type': 'integer', 'required': district_required, "data": disctrict_data},
#             {'name': 'street', 'type': 'string', 'required': False, "data": None},
#             {'name': 'house_number', 'type': 'string', 'required': False, "data": None},
#             {'name': 'crossing', 'type': 'string', 'required': False, "data": None},
#             {'name': 'phone_info', 'type': 'integer', 'required': False, "data": phone_info_data},
#             {'name': 'internet', 'type': 'integer', 'required': False, "data": internet_data},
#             {'name': 'toilet', 'type': 'integer', 'required': False, "data": toilet_data},
#             {'name': 'balkony', 'type': 'integer', 'required': False, "data": balcony_data},
#             {'name': 'door', 'type': 'integer', 'required': False, "data": door_data},
#             {'name': 'parking', 'type': 'integer', 'required': False, "data": parking_data},
#             {'name': 'gas', 'type': 'integer', 'required': False, "data": gas_data},
#             {'name': 'balkony', 'type': 'integer', 'required': False, "data": balcony_data},
#             {'name': 'parking', 'type': 'integer', 'required': False, "data": parking_data},
#             {'name': 'furniture', 'type': 'integer', 'required': False, "data": furniture_data},
#             {'name': 'flooring', 'type': 'integer', 'required': False, "data": flooring_data},
#             {'name': 'ceiling_height', 'type': 'float', 'required': False, "data": None},
#             {'name': 'safety', 'type': 'integer', 'required': False, "data": safety_data},
#             {'name': 'flat_options', 'type': 'integer', 'required': False, "data": flat_options_data},
#             {'name': 'documents', 'type': 'integer', 'required': False, "data": document_data},
#             {'name': 'description', 'type': 'string', 'required': True, "data": None},
#             {'name': 'price', 'type': 'integer', "required": True, 'data': None},
#             {'name': 'currency', 'type': 'integer', "required": True, 'data': currency_data},
#             {'name': 'price_for', 'type': 'integer', "required": True, 'data': price_type_data},
#             {'name': 'installment', 'type': 'integer', "required": False, 'data': possibility_data},
#             {'name': 'mortgage', 'type': 'integer', "required": False, 'data': possibility_data},
#             {'name': 'exchange', 'type': 'integer', "required": False, 'data': exchange_data},
#             {'name': 'owner_type', 'type': 'integer', "required": True, "data": owner_data},
#             {'name': 'comment_allowed', 'type': 'integer', "required": False, 'data': commed_allowed_data},
#         ],
#         'apartment': [
#             {'name': 'rooms', 'type': 'integer', "required": True, 'data': rooms_data},
#             {'name': 'material', 'type': 'integer', "required": True, 'data': material_data},
#             {'name': 'floor', 'type': 'integer', "required": False, 'data': floors_data},
#             {'name': 'complex_id', 'type': 'integer', "required": False, 'data': None},
#             {'name': 'year', 'type': 'integer', "required": False, 'data': None},
#             {'name': 'land_square', 'type': 'integer', "required": True, 'data': None},
#             {'name': 'living_square', 'type': 'integer', "required": False, 'data': None},
#             {'name': 'kitchen_square', 'type': 'integer', "required": False, 'data': None},
#             {'name': 'square', 'type': 'integer', "required": True, 'data': None},
#             {'name': 'condition', 'type': 'integer', "required": True, 'data': condition_data},
#             {'name': 'heating', 'type': 'integer', "required": False, 'data': heating_data},
#             {'name': 'cadastre_number', 'type': 'integer', 'required': False, "data": None},
#             {'name': 'region', 'type': 'integer', 'required': True, "data": regions_data},
#             {'name': 'town', 'type': 'integer', 'required': True, "data": town_data},
#             {'name': 'disctrict', 'type': 'integer', 'required': district_required, "data": disctrict_data},
#             {'name': 'street', 'type': 'string', 'required': False, "data": None},
#             {'name': 'house_number', 'type': 'string', 'required': False, "data": None},
#             {'name': 'crossing', 'type': 'string', 'required': False, "data": None},
#             {'name': 'phone_info', 'type': 'integer', 'required': False, "data": phone_info_data},
#             {'name': 'internet', 'type': 'integer', 'required': False, "data": internet_data},
#             {'name': 'toilet', 'type': 'integer', 'required': False, "data": toilet_data},
#             {'name': 'balkony', 'type': 'integer', 'required': False, "data": balcony_data},
#             {'name': 'door', 'type': 'integer', 'required': False, "data": door_data},
#             {'name': 'parking', 'type': 'integer', 'required': False, "data": parking_data},
#             {'name': 'gas', 'type': 'integer', 'required': False, "data": gas_data},
#             {'name': 'balkony', 'type': 'integer', 'required': False, "data": balcony_data},
#             {'name': 'parking', 'type': 'integer', 'required': False, "data": parking_data},
#             {'name': 'furniture', 'type': 'integer', 'required': False, "data": furniture_data},
#             {'name': 'flooring', 'type': 'integer', 'required': False, "data": flooring_data},
#             {'name': 'ceiling_height', 'type': 'float', 'required': False, "data": None},
#             {'name': 'safety', 'type': 'integer', 'required': False, "data": safety_data},
#             {'name': 'flat_options', 'type': 'integer', 'required': False, "data": flat_options_data},
#             {'name': 'documents', 'type': 'integer', 'required': False, "data": document_data},
#             {'name': 'description', 'type': 'string', 'required': True, "data": None},
#             {'name': 'price', 'type': 'integer', "required": True, 'data': None},
#             {'name': 'currency', 'type': 'integer', "required": True, 'data': currency_data},
#             {'name': 'price_for', 'type': 'integer', "required": True, 'data': price_type_data},
#             {'name': 'installment', 'type': 'integer', "required": False, 'data': possibility_data},
#             {'name': 'mortgage', 'type': 'integer', "required": False, 'data': possibility_data},
#             {'name': 'exchange', 'type': 'integer', "required": False, 'data': exchange_data},
#             {'name': 'owner_type', 'type': 'integer', "required": True, "data": owner_data},
#             {'name': 'comment_allowed', 'type': 'integer', "required": False, 'data': commed_allowed_data},
#         ],
#     }
# }
# #         'land': [
# #             {'name': 'land_area', 'type': 'float'},
# #             {'name': 'price', 'type': 'float'},
# #             {'name': 'currency', 'type': 'string', 'choices': [currency[0] for currency in choices.CURRENCY_TYPE]},
# #         ],
# #         'summer_house': [
# #             {'name': 'room_count', 'type': 'string', 'choices': [room[0] for room in choices.ROOM_COUNT_OPTIONS]},
# #             {'name': 'land_area', 'type': 'float'},
# #             {'name': 'price', 'type': 'float'},
# #             {'name': 'currency', 'type': 'string', 'choices': [currency[0] for currency in choices.CURRENCY_TYPE]},
# #         ],
# #         'parking_garage': [
# #             {'name': 'price', 'type': 'float'},
# #             {'name': 'currency', 'type': 'string', 'choices': [currency[0] for currency in choices.CURRENCY_TYPE]},
# #             {'name': 'parking', 'type': 'string', 'choices': [choice[0] for choice in choices.PARKING_CHOICES]},
# #         ],
# #     },
# #     'sell': {
# #         'house': [
# #             {'name': 'room_count', 'type': 'string', 'choices': [room[0] for room in choices.ROOM_COUNT_OPTIONS]},
# #             {'name': 'type_building', 'type': 'string', 'choices': [building[0] for building in choices.BUILDING_TYPE_CHOICES]},
# #             {'name': 'land_area', 'type': 'float'},
# #             {'name': 'price', 'type': 'float'},
# #             {'name': 'currency', 'type': 'string', 'choices': [currency[0] for currency in choices.CURRENCY_TYPE]},
# #         ],
# #         # Добавьте аналогичные параметры для других типов недвижимости
# #     }
# # }

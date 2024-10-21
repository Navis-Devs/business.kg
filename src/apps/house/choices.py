import datetime

TYPE_DEAL = [
    ('Sell', 'Продажа'),
    ('Rental', 'Аренда'),
]

INSTALLMENT_OPTIONS = [
    ('Yes', 'Жок'),
    ('No', 'Нет'),
]

MORTGAGE_OPTIONS = [
    ('Yes', 'Есть'),
    ('No', 'Нет'),
]

EXCHANGE_OPTIONS = [
    ('Open to options', 'Рассмотрю варианты'),
    ('With buyers extra payment', 'С доплатой покупателя'),
    ('With sellers extra payment', 'С доплатой продавца'),
    ('Key for key', 'Ключ на ключ'),
    ('No exchange offers', 'Обмен не предлагать'),
    ('Exchange for a car', 'Обмен на авто'),
]

ADVERTISER_OPTIONS = [
    ('proprietor', 'Собственник'),
    ('Agent', 'Агент'),
]

PROPERTY_TYPE_OPTIONS = [
    ('House', 'Дом'),
    ('Apartment', 'Квартира'),
    ('Commercial property', 'Коммерческая недвижимость'),
    ('Land plot', 'Участок'),
    ('Cottage', 'Дача'),
    ('Parking/Garage', 'Паркинг/Гараж'),
]

ROOM_COUNT_OPTIONS = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6 or more', '6 и более'),
    ('Open plan', 'Свободная планировка'),
]

SERIES_CHOICES = [
    ('102 series', '102 серия'),
    ('104 series', '104 серия'),
    ('Improved 104 series', '104 серия улучшенная'),
    ('105 series', '105 серия'),
    ('Improved 105 series', '105 серия улучшенная'),
    ('106 series', '106 серия'),
    ('Improved 106 series', '106 серия улучшенная'),
    ('Stalinka', 'Сталинка'),
    ('Khrushchevka', 'Хрущевка'),
    ('Individual layout', 'Индивид. планировка'),
]

BUILDING_TYPE_CHOICES = [
    ('Brick', 'Кирпичный'),
    ('Panel', 'Панельный'),
    ('Monolith', 'Монолитный'),
]

CONDITION_CHOICES = [
    ('Under finishing', 'Под самоотделку'),
    ('Euro renovation', 'Евроремонт'),
    ('Good', 'Хорошее'),
    ('Average', 'Среднее'),
    ('Not finished', 'Не достроено'),
]

CURRENCY_TYPE = [
    ('USD', 'Доллар'),
    ('SOM', 'Сом'),
]

PRICE_FOR = [
    ('For the whole', 'За все'),
    ('Per meter', 'За метр'),
]

# Характеристики 


FLOOR_CHOICES = [
    ('Linoleum', 'Линолеум'),
    ('Parquet', 'Паркет'),
    ('Laminate', 'Ламинат'),
    ('Wood', 'Дерево'),
    ('Carpet', 'Ковролин'),
    ('Tile', 'Плитка'),
    ('Cork flooring', 'Пробковое'),
]

ENTRANCE_DOOR_CHOICES = [
    ('Wooden', 'Деревянная'),
    ('Metal', 'Металлическая'),
    ('Armored', 'Бронированная'),
    ('No door', 'Нет'),
]

PARKING_CHOICES = [
    ('Parking', 'Паркинг'),
    ('Garage', 'Гараж'),
    ('Nearby guarded parking', 'Рядом охраняемая стоянка'),
]

FURNITURE_CHOICES = [
    ('Fully furnished', 'Полностью меблирована'),
    ('Partially furnished', 'Частично меблирована'),
    ('Unfurnished', 'Пустая'),
]

BALCONY_CHOICES = [
    ('Balcony', 'Балкон'),
    ('Glazed balcony', 'Застекленный балкон'),
    ('Loggia', 'Лоджия'),
    ('No balcony', 'Нет'),
]

HEATING_CHOICES = [
    ('Central', 'Центральное'),
    ('Gas', 'На газе'),
    ('Electric', 'Электрическое'),
    ('Mixed', 'Смешанное'),
    ('Solid fuel', 'На твердом топливе'),
    ('Liquid fuel', 'На жидком топливе'),
    ('No heating', 'Без отопления'),
    ('Autonomous', 'Автономное'),
]

PHONE_CHOICES = [
    ('Available', 'Есть'),
    ('Possible connection', 'Возможно подключение'),
    ('Not available', 'Нет'),
]

INTERNET_CHOICES = [
    ('ADSL', 'ADSL'),
    ('Wired', 'Проводной'),
    ('Fiber optic', 'Оптика'),
]

BATHROOM_CHOICES = [
    ('Separate', 'Раздельный'),
    ('Combined', 'Совмещенный'),
    ('2 or more bathrooms', '2 с/у и более'),
    ('No bathroom', 'Нет'),
]

GAS_CHOICES = [
    ('Main pipeline', 'Магистральный'),
    ('Autonomous', 'Автономный'),
    ('Possible connection', 'Возможно подключение'),
    ('No gas', 'Нет'),
]
SEWAGE_CHOICES = [
    ('central', 'Центральная'),
    ('possible_connection', 'Возможно подведение'),
    ('septic', 'Септик'),
    ('no', 'Нет'),
]

DRINKING_WATER_CHOICES = [
    ('central_water_supply', 'Центральное водоснабжение'),
    ('possible_connection', 'Возможно подведение'),
    ('well', 'Скважина'),
    ('no', 'Нет'),
]

ELECTRICITY_CHOICES = [
    ('yes', 'Есть'),
    ('possible_connection', 'Возможно подведение'),
    ('no', 'Нет'),
]

OBJECT_STATE = [
    ('scheduled', 'запланирован'),
    ('under construction', 'строится'),
    ('finalized', 'завершен'),
    ('commissioned', 'сдан в эксплуатацию'),
    ('frozen', 'заморожен')
]

LOCATION_CHOICES = [
    ('in_city', 'В городе'),
    ('along_road', 'Вдоль трассы'),
    ('in_hills', 'В предгорьях'),
    ('in_suburbs', 'В пригороде'),
    ('near_water', 'Возле водоема'),
    ('in_summer_cottage_area', 'В дачном массиве'),
]

HOUSING_CLASS = [
    ('econom', 'эконом'),
    ('comfort', 'комфорт'),
    ('business', 'бизнес'),
    ('premuim', 'премуим'),
]

def year_choices():
    return [(r,r) for r in range(1950, datetime.date.today().year+1)]

def current_year():
    return datetime.date.today().year
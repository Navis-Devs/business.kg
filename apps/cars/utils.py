import csv
from apps.cars.models import (
    CarType, CarMark, CarModel, CarGeneration, CarSerie, CarModification,
    CarCharacteristic, CarCharacteristicValue, CarEquipment, CarOption, CarOptionValue
)

dir = "BusinessData/Cars/DBDemo/"

def CarTypeLoad():
    file_path = f'{dir}car_type.csv'

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            cleaned_row = {key.strip("'"): value.strip("'") for key, value in row.items()}

            print(cleaned_row)

            CarType.objects.create(
                id=cleaned_row.get("id_car_type"),
                name=cleaned_row.get("name"),
            )


def CarMarkLoad():
    file_path = f'{dir}car_mark.csv'

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

    for row in reader:
        cleaned_row = {key.strip("'"): value.strip("'") for key, value in row.items()}

        print(cleaned_row)

        CarMark.objects.create(
            id=cleaned_row.get("id_car_mark"),
            name=cleaned_row.get("name"),
            id_car_type=cleaned_row.get("id_car_type"),
            name_rus=cleaned_row.get("name_rus")
        )

def CarModelLoad():
    file_path = f'{dir}car_model.csv'

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

    for row in reader:
        cleaned_row = {key.strip("'"): value.strip("'") for key, value in row.items()}

        print(cleaned_row)

        CarModel.objects.create(
            id=cleaned_row.get("id_car_model"),
            id_car_mark=cleaned_row.get("id_car_mark"),
            name=cleaned_row.get("name"),
            id_car_type=cleaned_row.get("id_car_type"),
            name_rus=cleaned_row.get("name_rus")
        )

def CarGenerationLoad():
    file_path = f'{dir}car_generation.csv'

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

    for row in reader:
        cleaned_row = {key.strip("'"): value.strip("'") for key, value in row.items()}

        print(cleaned_row)

        CarGeneration.objects.create(
            id=cleaned_row.get("id_car_generation"),
            name=cleaned_row.get("name"),
            id_car_model=cleaned_row.get("id_car_model"),
            year_begin=cleaned_row.get("year_begin"),
            year_end=cleaned_row.get("year_end"),
            id_car_type=cleaned_row.get("id_car_type"),
        )


def CarSerieLoad():
    file_path = f'{dir}car_serie.csv'

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

    for row in reader:
        cleaned_row = {key.strip("'"): value.strip("'") for key, value in row.items()}

        print(cleaned_row)

        CarSerie.objects.create(
            id=cleaned_row.get("id_car_serie"),
            id_car_model=cleaned_row.get("id_car_model"),
            name=cleaned_row.get("name"),
            id_car_generation=cleaned_row.get("id_car_generation"),
            id_car_type=cleaned_row.get("id_car_type"),
        )


def CarModificationLoad():
    file_path = f'{dir}car_modification.csv'

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

    for row in reader:
        cleaned_row = {key.strip("'"): value.strip("'") for key, value in row.items()}

        print(cleaned_row)

        CarModification.objects.create(
            id=cleaned_row.get("id_car_modification"),
            id_car_serie=cleaned_row.get("id_car_serie"),
            id_car_model=cleaned_row.get("id_car_model"),
            name=cleaned_row.get("name"),
            id_car_type=cleaned_row.get("id_car_type"),
        )


def CarCharacteristicLoad():
    file_path = f'{dir}car_characteristic.csv'

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

    for row in reader:
        cleaned_row = {key.strip("'"): value.strip("'") for key, value in row.items()}

        print(cleaned_row)

        CarCharacteristic.objects.create(
            id=cleaned_row.get("id_car_characteristic"),
            name=cleaned_row.get("name"),
            id_parent=cleaned_row.get("id_parent"),
            id_car_type=cleaned_row.get("id_car_type"),
        )


def CarCharacteristicValueLoad():
    file_path = f'{dir}car_characteristic_value.csv'

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

    for row in reader:
        cleaned_row = {key.strip("'"): value.strip("'") for key, value in row.items()}

        print(cleaned_row)

        CarCharacteristicValue.objects.create(
            id=cleaned_row.get("id_car_characteristic_value"),
            value=cleaned_row.get("value"),
            unit=cleaned_row.get("unit"),
            id_car_characteristic=cleaned_row.get("id_car_characteristic"),
            id_car_modification=cleaned_row.get("id_car_modification"),
            id_car_type=cleaned_row.get("id_car_type"),
        )


def CarEquipmentLoad():
    file_path = f'{dir}car_equipment.csv'

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

    for row in reader:
        cleaned_row = {key.strip("'"): value.strip("'") for key, value in row.items()}

        print(cleaned_row)

        CarEquipment.objects.create(
            id=cleaned_row.get("id_car_equipment"),
            name=cleaned_row.get("name"),
            id_car_modification=cleaned_row.get("id_car_modification"),
            price_min=cleaned_row.get("price_min"),
            id_car_type=cleaned_row.get("id_car_type"),
            year=cleaned_row.get("year")
        )


def CarOptionLoad():
    file_path = f'{dir}car_option.csv'

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

    for row in reader:
        cleaned_row = {key.strip("'"): value.strip("'") for key, value in row.items()}

        print(cleaned_row)

        CarOption.objects.create(
            id=cleaned_row.get("id_car_option"),
            name=cleaned_row.get("name"),
            id_parent=cleaned_row.get("id_parent"),
            id_car_type=cleaned_row.get("id_car_type"),
        )


def CarOptionValueLoad():
    file_path = f'{dir}car_option_value.csv'

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

    for row in reader:
        cleaned_row = {key.strip("'"): value.strip("'") for key, value in row.items()}

        print(cleaned_row)

        CarOptionValue.objects.create(
            id=cleaned_row.get("id_car_option_value"),
            is_base=cleaned_row.get("is_base"),
            id_car_option=cleaned_row.get("id_car_option"),
            id_car_equipment=cleaned_row.get("id_car_equipment"),
            id_car_type=cleaned_row.get("id_car_type"),
        )

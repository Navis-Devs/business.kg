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
            cleaned_row = {key.strip("'"): (value.strip("'") if value and value != 'NULL' else None) for key, value in row.items()}

            print(cleaned_row)

            CarType.objects.get_or_create(
                id=cleaned_row.get("id_car_type"),
                name=cleaned_row.get("name"),
            )


def CarMarkLoad():
    file_path = f'{dir}car_mark.csv'

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            cleaned_row = {key.strip("'"): (value.strip("'") if value and value != 'NULL' else None) for key, value in row.items()}

            print(cleaned_row)

            CarMark.objects.get_or_create(
                id=cleaned_row.get("id_car_mark"),
                name=cleaned_row.get("name"),
                id_car_type=CarType.objects.get(id=cleaned_row.get("id_car_type")),
                name_rus=cleaned_row.get("name_rus")
            )

def CarModelLoad():
    file_path = f'{dir}car_model.csv'

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            cleaned_row = {key.strip("'"): (value.strip("'") if value and value != 'NULL' else None) for key, value in row.items()}

            print(cleaned_row)

            CarModel.objects.get_or_create(
                id=cleaned_row.get("id_car_model"),
                id_car_mark=CarMark.objects.get(id=cleaned_row.get("id_car_mark")),
                name=cleaned_row.get("name"),
                id_car_type=CarType.objects.get(id=cleaned_row.get("id_car_type")),
                name_rus=cleaned_row.get("name_rus")
            )

def CarGenerationLoad():
    file_path = f'{dir}car_generation.csv'

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            cleaned_row = {key.strip("'"): (value.strip("'") if value and value != 'NULL' else None) for key, value in row.items()}

            print(cleaned_row)

            CarGeneration.objects.get_or_create(
                id=cleaned_row.get("id_car_generation"),
                name=cleaned_row.get("name"),
                id_car_model=CarModel.objects.get(id=cleaned_row.get("id_car_model")),
                year_begin=cleaned_row.get("year_begin"),
                year_end=cleaned_row.get("year_end"),
                id_car_type=CarType.objects.get(id=cleaned_row.get("id_car_type")),
            )


def CarSerieLoad():
    file_path = f'{dir}car_serie.csv'

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            cleaned_row = {key.strip("'"): (value.strip("'") if value and value != 'NULL' else None) for key, value in row.items()}

            print(cleaned_row)

            CarSerie.objects.get_or_create(
                id=cleaned_row.get("id_car_serie"),
                id_car_model=CarModel.objects.get(id=cleaned_row.get("id_car_model")),
                name=cleaned_row.get("name"),
                id_car_generation=CarGeneration.objects.get(id=cleaned_row.get("id_car_generation")),
                id_car_type=CarType.objects.get(id=cleaned_row.get("id_car_type")),
            )


def CarModificationLoad():
    file_path = f'{dir}car_modification.csv'

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            cleaned_row = {key.strip("'"): (value.strip("'") if value and value != 'NULL' else None) for key, value in row.items()}

            print(cleaned_row)

            CarModification.objects.get_or_create(
                id=cleaned_row.get("id_car_modification"),
                id_car_serie=CarSerie.objects.get(id=cleaned_row.get("id_car_serie")),
                id_car_model=CarModel.objects.get(id=cleaned_row.get("id_car_model")),
                name=cleaned_row.get("name"),
                id_car_type=CarType.objects.get(id=cleaned_row.get("id_car_type")),
            )

def get_or_none(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return None

def CarCharacteristicLoad():
    file_path = f'{dir}car_characteristic.csv'

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            cleaned_row = {key.strip("'"): (value.strip("'") if value and value != 'NULL' else None) for key, value in row.items()}

            print(cleaned_row)

            # Handle 'NULL' and empty values
            id_parent = cleaned_row.get("id_parent")
            id_car_type = cleaned_row.get("id_car_type")

            parent_instance = get_or_none(CarCharacteristic, id=id_parent) if id_parent and id_parent != 'NULL' else None
            car_type_instance = get_or_none(CarType, id=id_car_type) if id_car_type and id_car_type != 'NULL' else None

            CarCharacteristic.objects.get_or_create(
                id=cleaned_row.get("id_car_characteristic"),
                name=cleaned_row.get("name"),
                id_parent=parent_instance,
                id_car_type=car_type_instance,
            )


def CarCharacteristicValueLoad():
    file_path = f'{dir}car_characteristic_value.csv'

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            cleaned_row = {}
            for key, value in row.items():
                key = key.strip("'") if key else key
                value = value.strip("'") if value and isinstance(value, str) else value
                value = None if value == 'NULL' else value

                # Convert numeric fields to integers
                if key in ["id", "id_car_characteristic", "id_car_modification", "id_car_type"]:
                    try:
                        value = int(value) if value is not None else None
                    except ValueError:
                        value = None

                cleaned_row[key] = value

            print(cleaned_row)

            # Fetch related instances safely
            id_car_characteristic = cleaned_row.get("id_car_characteristic")
            id_car_modification = cleaned_row.get("id_car_modification")
            id_car_type = cleaned_row.get("id_car_type")

            car_characteristic_instance = CarCharacteristic.objects.filter(id=id_car_characteristic).first()
            car_modification_instance = CarModification.objects.filter(id=id_car_modification).first()
            car_type_instance = CarType.objects.filter(id=id_car_type).first()

            # Create or update the CarCharacteristicValue instance
            CarCharacteristicValue.objects.get_or_create(
                id=cleaned_row.get("id_car_characteristic_value"),
                defaults={
                    'value': cleaned_row.get("value"),
                    'unit': cleaned_row.get("unit"),
                    'id_car_characteristic': car_characteristic_instance,
                    'id_car_modification': car_modification_instance,
                    'id_car_type': car_type_instance,
                }
            )


def CarEquipmentLoad():
    file_path = f'{dir}car_equipment.csv'

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            cleaned_row = {key.strip("'"): (value.strip("'") if value and value != 'NULL' else None) for key, value in row.items()}

            print(cleaned_row)

            CarEquipment.objects.get_or_create(
                id=cleaned_row.get("id_car_equipment"),
                name=cleaned_row.get("name"),
                id_car_modification=CarModification.objects.get(id=cleaned_row.get("id_car_modification")),
                price_min=cleaned_row.get("price_min"),
                id_car_type=CarType.objects.get(id=cleaned_row.get("id_car_type")),
                year=cleaned_row.get("year")
            )


def CarOptionLoad():
    file_path = f'{dir}car_option.csv'

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            cleaned_row = {}
            for key, value in row.items():
                if key and isinstance(key, str):
                    key = key.strip("'")
                if value and isinstance(value, str):
                    value = value.strip("'") if value != 'NULL' else None

                    if key in ["id", "id_parent", "id_car_type"]:
                        try:
                            value = int(value)
                        except ValueError:
                            value = None

                cleaned_row[key] = value

            print(cleaned_row)

            id_parent = cleaned_row.get("id_parent")
            id_car_type = cleaned_row.get("id_car_type")

            parent_instance = get_or_none(CarOption, id=id_parent) if id_parent and id_parent != 'NULL' else None
            car_type_instance = get_or_none(CarType, id=id_car_type) if id_car_type and id_car_type != 'NULL' else None

            CarOption.objects.get_or_create(
                id=cleaned_row.get("id_car_option"),
                name=cleaned_row.get("name"),
                id_parent=parent_instance,
                id_car_type=car_type_instance,
            )

def CarOptionValueLoad():
    file_path = f'{dir}car_option_value.csv'

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            cleaned_row = {key.strip("'"): (value.strip("'") if value and value != 'NULL' else None) for key, value in row.items()}

            print(cleaned_row)

            CarOptionValue.objects.get_or_create(
                id=cleaned_row.get("id_car_option_value"),
                is_base=cleaned_row.get("is_base"),
                id_car_option=CarOption.objects.get(id=cleaned_row.get("id_car_option")),
                id_car_equipment=CarEquipment.objects.get(id=cleaned_row.get("id_car_equipment")),
                id_car_type=CarType.objects.get(id=cleaned_row.get("id_car_type")),
            )

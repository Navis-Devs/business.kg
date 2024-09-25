import time
from django.db import connection
import os
import sys
import django

sys.path.append(os.path.join(os.path.dirname(__file__), 'core'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

django.setup()

from apps.cars import models


def measure_query(queryset):
    start_time = time.time()

    list(queryset)

    execution_time = time.time() - start_time
    num_queries = len(connection.queries)

    print(f"Время выполнения: {execution_time} секунд")
    print(f"Количество запросов: {num_queries}")


# Запрос с objects.all()
print("Без select_related:")
measure_query(models.CarMark.objects.all())

# Запрос с select_related()
print("\С использованием select_related:")
measure_query(models.CarMark.objects.select_related('id_car_type').all())

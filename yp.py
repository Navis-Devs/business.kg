import time
from django.db import connection
import os
import sys
import django

sys.path.append(os.path.join(os.path.dirname(__file__), 'core'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

django.setup()

# import subprocess
# import time
# import string
# import random
#
#
# # Функция для выполнения команды в терминале
# def run_command(command):
#     try:
#         result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#         return result.stdout.decode('utf-8')
#     except subprocess.CalledProcessError as e:
#         return f"Error: {e.stderr.decode('utf-8')}"
#
#
# # Цикл для многократного выполнения команды
# while True:
#     letters = string.ascii_letters
#     world = ''.join(random.choice(letters) for i in range(10))
#     command = f"cp -R  {world}.txt"  # замените 'file_name' на нужный путь
#     output = run_command(command)
#     print(output)
#
#     time.sleep(5)  # Задержка в 5 секунд перед повторным запуском

# from apps.cars import models
#
#
# def measure_query(queryset):
#     start_time = time.time()
#
#     list(queryset)
#
#     execution_time = time.time() - start_time
#     num_queries = len(connection.queries)
#
#     print(f"Время выполнения: {execution_time} секунд")
#     print(f"Количество запросов: {num_queries}")
#
#
# # Запрос с objects.all()
# print("Без select_related:")
# measure_query(models.CarMark.objects.all())
#
# # Запрос с select_related()
# print("\С использованием select_related:")
# measure_query(models.CarMark.objects.select_related('id_car_type').all())



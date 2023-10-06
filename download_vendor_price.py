import urllib.request               # Для скачивания необходимого файла на локальный ПК
from datetime import datetime       # Для перименования файла, так как скачка будет раз в  час 
import pandas as pd                 # Для работы с pandas
import csv                          # Отдельно для работы с csv
import numpy as np                  # Для работы с numpy


# Переменные
dict_vendor = {}

  
# Получаем текущую дату и время на момент формирования файла
def get_current_date(current_date_time, date_now):
    date_now = current_date_time.strftime("%d.%m.%Y_%H%M%S")   
    return date_now  


# Формируем путь и имя файла куда положить файл
def get_dir_name_file_local(local_puth, name_file, full_path_file):
    full_path_file = local_puth + name_file + current_date_time_result + ".csv"
    return full_path_file    


# Вызываем функцию получения текущей даты и времени
current_date_time_result = get_current_date(datetime.now(), '')


# Вызываем функцию получения директории и имени файла для дальнешего скачивания
download_csv_file_name = get_dir_name_file_local('C:/projects/project_final/', 'p5s_assort_', '')


# Скачиваем файл в указанную директорию
urllib.request.urlretrieve("http://stripmag.ru/datafeed/p5s_assort.csv", download_csv_file_name)


# Открываем файл поставщика с помощью функции csv
with open(download_csv_file_name, 'r', encoding='utf-8') as vendor_file:
    vendor_file_reader = csv.DictReader(vendor_file, delimiter = ";")
    for row in vendor_file_reader:
       dict_vendor[row["Артикул производителя"]] = row["Цена (Розница)"]
#       print(dict_vendor) 
         

# Открываем файл интернет-магазина с помощью функции csv
with open('C:\projects\Project_final\intim_product.csv', 'r', encoding='utf-8') as base_file:
    base_file_reader = csv.DictReader(base_file, delimiter = ";")
    for row in base_file_reader:
        for key, val in dict_vendor.items():
            if key == row["barcode"]:
               row["cost_original_val"] = val 
               #print(f'Произведена замена в {key}')
               break 
            if key == '1156-01-BX': break # прайс большой поэтому ограничила для теста 20-ю строками


# Вызываем функцию получения текущей даты и времени
current_date_time_result = get_current_date(datetime.now(), '')


# Вызываем функцию получения директории и имени файла для формирования файла базы
upload_csv_file_name = get_dir_name_file_local('C:/projects/project_final/', 'output_file_', '')


# Выгружаем полученный словарь с актуальными ценами в файл выгрузки для базы
with open(upload_csv_file_name, 'w') as csv_file:
    for key in dict_vendor.keys():
        csv_file.write("%s; %s\n" %(key, dict_vendor[key]))
# Надо будет подумать, здесь я как-то не так подошла к выгрузке данных, так как мне нужны будут все поля, которые есть в исходном базы
# а по факту апдейтить только два-три поля


print("Актуализация данных завершена!")  
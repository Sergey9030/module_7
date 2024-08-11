import os
import time


directory = os.getcwd()
for root, dirs, files in os.walk(directory):
    for file in files:
        print()
        filename = file
        print('Обнаружен файл: ', filename)
        filepath = os.path.join(root, *[], file)
        print('Путь: ', filepath)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        print('Время изменения: ', formatted_time)
        parent_dir = os.path.dirname(root)
        print('Родительская директория: ', parent_dir)

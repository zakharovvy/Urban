import os
import time
for root, dirs, files in os.walk(".."):
  for file in files:
    filepath = os.path.join(root, file)
    filesize = os.path.getsize(filepath)
    formatted_time = os.path.getmtime(filepath)
    formatted_time = time.ctime(formatted_time)
    parent_dir = os.path.dirname(os.getcwd())
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, '
          f'Родительская директория: {parent_dir}')
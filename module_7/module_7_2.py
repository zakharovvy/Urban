def custom_write(file_name, strings):
    file = open(file_name,'w', encoding='utf-8')
    strings_positions = {}
    for string_number, string in enumerate(strings,start=1):
        byte_position = file.tell()
        file.write(f'{string}\n')
        strings_positions[(string_number, byte_position)] = string #Создание единого словаря из ключа-кортежа и значения
    file.close()                                                   #строки
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)



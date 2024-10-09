calls = 0
def count_calls ():
    global calls
    calls = calls + 1
    return calls
def string_info (string: str) -> tuple:
    count_calls()
    res_1 = list((len(string), string.upper(), string.lower()))
    res_2 = tuple (res_1)
    return res_2

def is_contains(string: str, list_to_search: list) -> bool:
    count_calls()
    upper_list = []
    for word in list_to_search:
        upper_list.append(word.upper())
    string_2 = string.upper ()
    if string_2 in upper_list:
        return True
    else:
        return False

print(string_info('ТетрагидрокАннаБинОЛ'))
print(string_info('ДихлордиФЕНИЛтрихлорэтан'))
print(is_contains('Вода', ['ЗЕМлЯ', 'огонЬ', 'ВОДА']))
print(is_contains('гидро', ['Тетраметилдитиоксид', 'Гидроксикобаламин', 'Декстрометорфан ']))
print(calls)






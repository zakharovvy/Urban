def add_everything_up(a:int|float,b:int|float|str):
    try:
        result = a+b
        result = round(result,3)
    except TypeError:
        a = str(a)
        b = str(b)
        result = a+b
    return result

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

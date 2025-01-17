def get_multiplied_digits (number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

result_digit = get_multiplied_digits(int(input('Введите любое целое число')))
print(result_digit)
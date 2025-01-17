#1 Задание
def print_params (a = 1, b = 'строка', c = True):
    print (a, b, c)


print_params()
print_params(5)
print_params(5, False)
print_params('Буква', 15.25, False)
print_params(b = 25)
print_params(c = [1,2,3])

# 2 Задание
values_list = ["Смола", 342, 468.90]
values_dict = {'a': 678, 'b': False, 'c': 'Money'}
print_params(*values_dict)
print_params(**values_dict)

#3 Задание
values_list_2 = ['Bank', False]
print_params(*values_list_2, 42)
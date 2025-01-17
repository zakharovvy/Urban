first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (abs(len(x) - len(y)) for x, y in zip(first, second) if len(x) != len(y))

second_result = [len(first[x]) == len(second[x]) for x in range(min(len(first), len(second)))]
#Использование min необходимо чтобы не выйти за предел списка
print(list(first_result))
print(list(second_result))
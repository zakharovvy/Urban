#Проверку на простоту украл со StackoverFlow, но вроде работает нормально
#Добавлены проверки на 0 и 1 (обозначил, что это не простые числа)
def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if result == 0 or result == 1:
            print(result)
            return "не простое"
        for i in range(2, (result // 2) + 1):
            if result % i == 0:
                print(result)
                return "Составное"
        print(result)
        return "Простое"
    return wrapper

@is_prime
def sum_three(a:int,b:int,c:int):
    return a+b+c

#Порядок выдачи ответов такой же как в образце: сначала число, потом характеристика
result = sum_three(2, 3, 6)
print(result)

result2 = sum_three(0, 0, 1)
print(result2)

result3 = sum_three(0, 0, 0)
print(result3)

result4 = sum_three(5, 10, 1)
print(result4)


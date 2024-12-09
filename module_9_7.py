#Проверку на простоту украл со StackoverFlow, но вроде работает нормально
def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        for i in range(2, (result // 2) + 1):
            if result % i == 0:
                print(result)
                return "Не простое"
        print(result)
        return "Простое"
    return wrapper

@is_prime
def sum_three(a:int,b:int,c:int):
    return a+b+c

result = sum_three(2, 3, 6)
print(result)

result2 = sum_three(2, 5, 9)
print(result2)

result3 = sum_three(86, 3, 3)
print(result3)

result4 = sum_three(77, 0, 1)
print(result4)

result5 = sum_three(2, 0, 109)
print(result5)

result6 = sum_three(450, 81, 500)
print(result6)

result7 = sum_three(1234,5678,3679)
print(result7)

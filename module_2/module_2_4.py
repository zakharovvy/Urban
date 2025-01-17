numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
j = 0
for i in numbers:
    if i == 1:
        continue
    simple = True # Использую переменную симпл потому
    for j in range (2, i):  #что ее название мне больше нравится
        if i % j != 0:
            simple = simple&True       #Это необходимо для накопления и для очистки цикла.
        else:
            simple = False&simple   #Это необходимо для накопления.
    if simple:
        primes.append(i)
    else:
        not_primes.append(i)
print(primes)
print(not_primes)

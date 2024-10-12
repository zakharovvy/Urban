
#Тот, кто придумал эту задачу настоящий садист. Я убил на нее суммарно более 8 часов. Это говнокод,но он работает.
# Проверял с помощью асертов, потому что это невозможно в ручную проверить.

def search_pairs (summ: int) -> list[tuple[int, int]]:
    list_of_pairs = []
    for i in range(1, (summ + 1) // 2):               #Функция, которая получает входящее число, а выдает нам
        list_of_pairs.append((i, summ - i))           #список в котором пары чисел, сумма которых равна указанному
    return list_of_pairs


def result(n: int) -> str:
    list_of_dividers = div(n)                #Главная функция, именно она выполняет объединение и выдает
    list_result = []                         #итоговый результат
    for d in list_of_dividers:
        list_result.extend(search_pairs (d))
    list_result.sort()
    return format(list_result)


def div(a: int) -> list[int]:
    dividers = []                      #Функция, которая находит делители определенного числа
    for i in range(2, a):              #Потом она добавляет их в список dividers. Это нужно для функции result
        if a % i == 0:
            dividers.append(i)
    dividers.append(a)

    return dividers


def format(list_of_tuples: list[tuple[int, int]]) -> str:
    res_2 = ''                                                       #Функция которая была создана из-за того функция
    for t in list_of_tuples:                                         #search_pairs выдает не тот формат, что нужен
        res_2 = res_2 + str(t[0]) + str(t[1])
    return res_2


res = result(int(input('Введите любое число')))
print(res)


def test_result ():
    assert result(3) == "12"
    assert result(4) == "13"
    assert result(5) == "1423"
    assert result(6) == "121524"
    assert result(7) == "162534"
    assert result(8) == "13172635"
    assert result(9) == "1218273645"
    assert result(10) == "141923283746"
    assert result(11) == "11029384756"
    assert result(12) == "12131511124210394857"
    assert result(13) == "112211310495867"
    assert result(14) == "1611325212343114105968"
    assert result(15) == "1214114232133124115106978"
    assert result(16) == "1317115262143531341251161079"
    assert result(17) == "11621531441351261171089"
    assert result(18) == "12151811724272163631545414513612711810"
    assert result(19) == "118217316415514613712811910"
    assert result(20) == "13141911923282183731746416515614713812911"
test_result()
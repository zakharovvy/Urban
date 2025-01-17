#Садистское задание. В конце есть комментарии с пояснением как работает код

def all_variants(text):
    for l in range(1,len(text)+1): #range(1,4)
        for i in range(len(text) - l + 1): 
            yield text[i:i+l]


a = all_variants("abc")
for i in a:
    print(i)


# l = 1, i = 3 - первый уровень внешнего цикла
# l = 1, i = 0: 0:1 a
# l = 1, i = 1: 1:2 b
# l = 1, i = 2: 2:3 c
# l = 2, i = 2 - второй уровень внешнего цикла
# l = 2, i = 0: 0:2 ab
# l = 2, i = 1: 1:3 bc
# l = 3, i = 1 - третий уровень внешнего цикла
# l = 3, i = 0: 0:3 abc


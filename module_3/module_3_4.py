
def single_root_words (root_word: str, *other_words: str) -> list:
    same_words = []
    new_root = root_word.upper()
    for i in other_words:
        j = i.upper ()
        if new_root in j or j in new_root:
            same_words.append(i)
    return same_words

result1 = single_root_words('вод', 'вода', 'аквапарк', 'ВОДОПРОВОД', 'родник')
result2 = single_root_words('МосОблГаз', 'гор', 'газ', 'МОС', 'Рег')
print(result1)
print(result2)

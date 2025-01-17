
class WordsFinder:
    def __init__(self, *file_name):
        self.file_names = list(file_name)

    def get_all_words (self):
        all_words = {}
        for file_ in self.file_names:
            with open(file_, encoding='utf-8') as file:
                text = file.read()
                text = text.lower()
                i = 0
                while i < len(text):
                    if text[i] in (',', '.', '=', '!', '?', ';', ':', ' - '):
                        text = text[:i] + text[i + 1:]
                    else:
                        i += 1
                words = text.split()
            all_words[file_] = words
        return all_words


    def find(self, word:str):
        result = {}
        word = word.lower()
        for key, value in self.get_all_words().items(): #мне использование key, value просто удобнее чем
            if word in value:                                      #другие слова
                result [key] = value.index(word) + 1
        return result

    def count(self, word:str):
        counter = 0
        result = {}
        word = word.lower()
        for key, value in self.get_all_words().items():
            counter = value.count(word)
            result [key] = counter
        return result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

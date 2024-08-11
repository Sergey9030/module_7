SEPARATORS = [', ', ',', '.', '=', '!', '?', ';', ':', ' - ', '\n']


def replase_separators(gs):  # Замменяет в строке gs разделители из SEPARATORS на пробел.
    s = gs
    for i in SEPARATORS:
        s = s.replace(i, ' ')
    return s


class WordsFinder:
    def __init__(self, *args):
        self.file_names = args

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, 'r', encoding='utf-8') as file:
                rr = replase_separators(file.read().lower())
                rr = rr.split()
                all_words.update({i: rr})
        return all_words

    def find(self, word):
        fw = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                fw.update({name: words.index(word.lower())+1})
        return fw

    def count(self, word):
        fw = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                fw.update({name: words.count(word.lower())})
        return fw

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

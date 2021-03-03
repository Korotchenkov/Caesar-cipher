import re

class Cesar_class:

    ALPHA = {chr(j): j - 1072 for j in range(1072, 1104)}

    def __init__(self, messege, shift):
        self.messege=messege
        self.shift = shift
        self.coding_alpha = {}
        for k,v in Cesar_class.ALPHA.items():
            if v>=self.shift:
                self.coding_alpha[k]=v-self.shift
            else:
                self.coding_alpha[k] =len(Cesar_class.ALPHA) - self.shift+v
        self.matching_letters=dict(zip(Cesar_class.ALPHA.keys(), [k for k,_ in sorted(self.coding_alpha.items(), key=lambda x:x[1])]))
        self.words=self.tokenization_on_words(self.messege)

    def tokenization_on_words(self, string):
        return re.findall(r'\b([-\w]+)\b', string)

    def code(self):
        return ' '.join([''.join([self.matching_letters[ch] for ch in word.lower()]) for word in self.words])

    def decode(self):
        self.decoding_alpha = {}
        for k,v in self.matching_letters.items():
            self.decoding_alpha[v]=k
        return ' '.join([''.join([self.decoding_alpha[ch] for ch in word.lower()]) for word in self.words])

if __name__=='__main__':
    instance=Cesar_class(input('Введите строку, которую нужно закодировать'),15)

    print(instance.code())

if __name__!='__main__':
    print('Модуль декодирования и кодирования импортирован успешно')








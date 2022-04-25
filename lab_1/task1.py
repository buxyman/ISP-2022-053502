import statistics
from statistics import median
class Task:
    text = ""
    dictionary = {}
    amount_of_sentences = 0
    amount_of_word = 0
    average_of_words = 0
    words_in_sentences = []
    median_word_amount = 0
    top_ngram = {}

    def __init__(self):
        self.text_input()
        self.amount_of_words()
        self.average()
        self.top_n_gram()
        pass

    def text_input(self):
        self.text = input("please input text: ")
        self.text = self.text.replace("!", ".")
        self.text = self.text.replace("?", ".")
        self.text = self.text.replace("...", ".")
        self.text = self.text.replace(",", " ")
        self.text = self.text.replace(" - ", " ")
        self.text = self.text.replace("-", " ")
        self.text = self.text.lower()
        pass

    def amount_of_words(self):
        sentences = self.text.split('.')
        for s in sentences:
            self.words_in_sentences.append(0)
        i = -1
        for sentences_count in sentences:
            i += 1
            self.amount_of_sentences += 1

            words = sentences_count.split()
            for word in words:
                self.words_in_sentences[i] += 1
                self.amount_of_word += 1
                if word in self.dictionary.keys():
                    self.dictionary[word] += 1
                else:
                    self.dictionary[word] = 1

        pass

    def top_n_gram (self):
        print('k = 10; n = 4')
        chose = input("y/n:")
        if chose == 'n':
            k = int(input('k = '))
            n = int(input('n = '))
        elif chose == 'y':
            k = 10
            n = 4
        else:
            print('wrong')
            return self.top_n_gram()
        # print('n', n)
        mas = sorted(self.dictionary.values(), reverse=True)
        d = {}
        for i in mas:
            for j in self.dictionary.keys():
                if self.dictionary[j] == i:
                    d[j] = self.dictionary[j]

        self.top_ngram = d.copy()

        for p in self.top_ngram.keys():
            if len(p) != n:
                d.pop(p)

        l = 0
        print('top ', k, 'n-gram:')
        for key in d.keys():
            l += 1
            print(key, ': ', self.top_ngram.get(key))

            if l == k:
                break




        pass

    def average(self):
        self.average_of_words = self.amount_of_word/self.amount_of_sentences
        self.median_word_amount = statistics.median(self.words_in_sentences)
        pass

    def output(self):
        print('dictionary:', sorted(self.dictionary.items(), reverse=True))
        print('average of words:', self.average_of_words)
        print('median word amount:', self.median_word_amount)


        pass


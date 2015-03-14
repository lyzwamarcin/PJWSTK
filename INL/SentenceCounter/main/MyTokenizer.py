# import nltk


class MyTokenizer:

    pos = 0
    len = 0

    def __init__(self, text):
        self.__text = text
        # self.__tokenized_text = nltk.word_tokenize(self.__text)
        self.__tokenized_text = text.split()
        self.len = len(self.__tokenized_text)

    def word_tokenizer(self):
        return self.__tokenized_text

    def get_token(self):
        self.pos += 1
        return self.__tokenized_text[self.pos - 1]

    def get_next_token(self):
        if self.has_next():
            return self.__tokenized_text[self.pos]
        else:
            return None

    def get_prev_token(self):
        if self.pos <= self.len:
            return self.__tokenized_text[self.pos - 2]
        else:
            return None

    def has_next(self):
        return self.pos <= self.len - 1

    def has_prev(self):
        return self.pos > 0
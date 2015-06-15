# -*- coding: utf-8 -*-
import codecs
import string
import nltk
import re

raw_input_file = []
word_regexp_dict = {}
noun_list = []
verb_list = []
adj_list = []
dictionary_list = []


def read_file(file_path):
    f = codecs.open(file_path, 'r', 'utf-8')

    file_content = f.read()
    f.close()
    return file_content


def load_data():
    global noun_list, verb_list, adj_list, dictionary_list
    noun_list = read_file("../data/noun.data").split()
    verb_list = read_file("../data/verb.data").split()
    adj_list = read_file("../data/adj.data").split()
    dictionary_list = noun_list + verb_list + adj_list


def normalize(s):
    global raw_input_file
    for p in string.punctuation:
        s = s.replace(p, '')
    return s.lower().strip()


def load_input_file():
    global raw_input_file
    raw_input_file = read_file("../input/text.txt").split('\n')
    return


def create_regexprs():
    global word_regexp_dict
    for sentence in raw_input_file:
        for token in nltk.word_tokenize(sentence):
            if token not in string.punctuation:
                regex_token = ".*".join(token)
                regex_token = ".*" + regex_token + ".*"
                word_regexp_dict[token] = regex_token


def find_similarities(pattern_string):
    pattern = re.compile(pattern_string)
    similarities = [x for i, x in enumerate(noun_list) if re.search(pattern, x)]
    return similarities


def fuzzy_match(s1, s2, max_dist=5):
    return nltk.metrics.edit_distance(normalize(s1), normalize(s2)) <= max_dist


def find_hints(dict_word_regexp):
    hints_dict = {}
    for word in word_regexp_dict:
        if word not in dictionary_list:
        #jezeli brak podobienstw to szukaj w wiktionary i cos zrob :)
            hints = []
            pattern = word_regexp_dict[word]
            similarities = find_similarities(pattern)
            for similaritiy in similarities:
                if fuzzy_match(word, similaritiy) is True:
                    hints.append(similaritiy)
            hints_dict[word] = hints
    return hints_dict


def main():
    load_data() # wczytuje wszystkie slowniki
    load_input_file() # wczytuje plik do analizy

    create_regexprs()
    find_hints(word_regexp_dict)


main()
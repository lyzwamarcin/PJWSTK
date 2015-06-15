# -*- coding: utf-8 -*-
import codecs

raw_input_file = ""
noun_list = []
verb_list = []
adj_list = []


def read_file(file_path):
    f = codecs.open(file_path, 'r', 'utf-8')

    file_content = f.read()
    f.close()
    return file_content


def load_data():
    global noun_list, verb_list, adj_list
    noun_list = read_file("../data/noun.data").split()
    verb_list = read_file("../data/verb.data").split()
    adj_list = read_file("../data/adj.data").split()


def load_input_file():
    global raw_input_file
    raw_input_file = read_file("../input/text.txt")


def main():
    load_data() # wczytuje wszystkie slowniki
    load_input_file() # wczytuje plik do analizy


main()
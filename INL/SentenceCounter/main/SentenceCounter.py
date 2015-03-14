# coding=utf-8
import os.path
import codecs
import MyTokenizer
import re

__NEWLINE__ = '\n'
EXCLAMATION_QUESTION_MARK = r'.+[?!]'
DOT = '[\.…]+$'
MULTI_DOT = '[\.…]+$'
QUOTATION_MARK_BEGIN = u'^["„].*'
QUOTATION_MARK_END = u'["”]'
QUOTATION_AND_DOT = '["”]\.+$'
QUOTATION_BEGIN_OR_DIAL = u'^["„-]'


class SentenceCounter:
    def __init__(self, shortcut_file_path, content_file_path):
        self.shortcut_file_path = shortcut_file_path
        self.content_file_path = content_file_path

        self.shortcuts_tab = self.__load_shortcuts()
        self.file_content = self.__load_text()

        self.sentences_list = []

    def __load_shortcuts(self):
        if not os.path.exists(self.shortcut_file_path):
            raise IOError('File ' + self.shortcut_file_path + ' not found!')

        shortcuts_file = open(self.shortcut_file_path, 'r').read()
        shortcuts_tab = shortcuts_file.split(__NEWLINE__)

        if len(shortcuts_tab) <= 1 and shortcuts_tab[0] == '':
            print 'Shortcuts file does not contains any element!'
            exit(-1)
        return shortcuts_tab

    def __load_text(self):
        if not os.path.exists(self.content_file_path):
            raise IOError('File ' + self.content_file_path + ' not found!')

        f = codecs.open(self.content_file_path, 'r', 'utf-8')

        file_content = f.read()
        f.close()
        return file_content

    def process_text(self):
        tokenizer = MyTokenizer.MyTokenizer(self.file_content)

        sentence = ''
        quotation = False
        while tokenizer.has_next():
            token = tokenizer.get_token().encode('utf-8')
            # print  token

            if re.search(QUOTATION_MARK_END, token.decode('utf-8')):
                quotation = False

            if re.search(QUOTATION_MARK_BEGIN, token.decode('utf-8')):
                quotation = True

            if not quotation:
                if re.search(EXCLAMATION_QUESTION_MARK, token) is not None and not quotation:
                    self.sentences_list.append(sentence + ' ' + token)
                    sentence = ''
                    continue

                if re.search(DOT, token) \
                        and re.sub('[^A-Za-z0-9.]+', '', token.lower()).encode('utf-8') not in self.shortcuts_tab \
                        and (tokenizer.get_next_token()[0].isupper() if tokenizer.get_next_token() is not None else False) \
                        and not quotation:
                    self.sentences_list.append(sentence + token)
                    sentence = ''
                    continue

                if re.search(DOT, token) \
                        and re.sub('[^A-Za-z0-9.]+', '', token.lower()).encode('utf-8') not in self.shortcuts_tab:
                    self.sentences_list.append(sentence + token)
                    sentence = ''
                    continue

            sentence += token.strip() + ' '
        if len(sentence) > 0:
            self.sentences_list.append(sentence)

        return self.sentences_list
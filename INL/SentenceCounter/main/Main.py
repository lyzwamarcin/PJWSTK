from main import SentenceCounter
from main import XMLBuilder

__SHORTCUTS_FILE_PATH__ = '..\data\\abbreviations.txt'
__TEXT_SOURCE_FILE__ = '..\data\\text.txt'
__OUTPUT_FILE_PATH__ = '..\data\output.xml'

class Main:

    def __init__(self):
        self.main()
        pass

    def main(self):
        xml = XMLBuilder.XMLBuilder()
        sentenceCounter = SentenceCounter.SentenceCounter(__SHORTCUTS_FILE_PATH__, __TEXT_SOURCE_FILE__)

        sentences = sentenceCounter.process_text()
        for sentence, i in zip(sentences, range(len(sentences))):
            print i, sentence
            xml.add_child('s', sentence.decode('utf-8'), {'xml:id': str(i+1) + '-s'})

        xml.save_to_file(__OUTPUT_FILE_PATH__)


m = Main()

import sys
import re
import enchant
from enchant.tokenize import get_tokenizer
from input import *

Phone_Directory = {
				 '2': ['A', 'B', 'C'],
                 '3': ['D', 'E', 'F'],
                 '4': ['G', 'G', 'I'],
                 '5': ['J', 'K', 'L'],
                 '6': ['M', 'N', 'O'],
                 '7': ['P', 'Q', 'R', 'S'],
                 '8': ['T', 'U', 'V'],
                 '9': ['W', 'X', 'Y', 'Z']}

Check_Word = enchant.Dict("en_US")

class Telephone_Book:
    def __init__(self, string):
        self.string = string

    def get_word(sub_string):
        return Check_Word.check(sub_string)


    def all_wordifications(self):
        # decode the string by removing all unnecessary chars
        clean_words = self.decoding()
        # if the string input is not a telephone, exit program
        if not clean_words:
            sys.exit("Wrong Input len or char, retry")
    

    







    def decoding(self):
        x = re.sub('[\W_]+', '', self.string)
        return x if len(x) == 10 or len(x) == 11 else False


    def encoding_numbers(self, raw_string):
        # 876-678-1000
        if len(raw_string) == 10:
            return raw_string[0:3] + '-' + raw_string[3:6] + '-' + raw_string[6:]
        # 1-876-678-1000
        else:
            return raw_string[0] + '-' + raw_string[1:4] + '-' + raw_string[4:7] + '-' + raw_string[7:]

    def words_to_number(self):
        # decode the string by removing all unnecessary chars
        clean_words = self.decoding()
        # if the string input is not a telephone, exit program
        if not clean_words:
            sys.exit("Wrong Input len or char, retry")

        string_list = [s for s in clean_words]
        for index in range(len(string_list)):
            for number, letter in Phone_Directory.items():
                if string_list[index] in letter:
                    string_list[index] = number
        return self.encoding_numbers(''.join(string_list))

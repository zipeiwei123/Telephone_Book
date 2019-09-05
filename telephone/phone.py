import sys
import re
import enchant
from enchant.tokenize import get_tokenizer
from input import *

Phone_Directory = {
				 '0': '',
     			 '1': '',
				 '2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

class Telephone_Book:
    def __init__(self, string):
        self.string = string

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

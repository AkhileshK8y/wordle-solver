
# importing sys
from curses.ascii import isalpha
import sys
  
# adding Folder_2 to the system path
sys.path.insert(0, './')

from utils.get_words_from_file import get_words_from_file, write_five_letter_words_to_file


def is_all_alpha_chars(word):
    for character in word:
        if not isalpha(character):
            return False
    return True


def filter_5_letter_words(word_list):
    five_letter_words = [word for word in word_list if len(word) == 5 and is_all_alpha_chars(word)]
    return five_letter_words


# Defining main function
def main():
    word_list = get_words_from_file('./word_base/words.txt')
    five_letter_words = filter_5_letter_words(word_list)
    write_five_letter_words_to_file(five_letter_words, './word_base/5_letter_words.txt')


# Using the special variable
# __name__
if __name__=="__main__":
	main()

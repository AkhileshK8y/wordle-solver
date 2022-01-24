from asyncore import read
from shutil import copyfile
import os
from utils.get_words_from_file import get_words_from_file, write_five_letter_words_to_file

def create_all_probable_words_file():
    source_file = os.path.join(os.getcwd(), "word_base", "5_letter_words.txt")
    probable_file = os.path.join(os.getcwd(), "probable_words.txt")
    copyfile(source_file, probable_file)


def filter_words_not_containing_character(character, probable_word_list):
    return [word for word in probable_word_list if character not in word]


def filter_words_containing_character(character, position, probable_word_list):
    return [word for word in probable_word_list if character in word and character != word[position]]


def filter_words_containing_character_at_position(character, position, probable_word_list):
    return [word for word in probable_word_list if character == word[position]]


def eliminate_words(tried_word, probable_word_list):
    position = 0
    for character in tried_word:
        val = input("\n\n🕵️  -> What is the tile color for character " + character + "\n ENTER 0 for Gray, 1 for Yellow and 2 for Green...\n" )
        if val == '0':
            probable_word_list = filter_words_not_containing_character(character, probable_word_list)
        elif val == '1':
            probable_word_list = filter_words_containing_character(character, position, probable_word_list)
        elif val == '2':
            probable_word_list = filter_words_containing_character_at_position(character, position, probable_word_list)
        else:
            raise Exception("Invalid Input!!!")
        position = position + 1
    return probable_word_list


def main():
    create_all_probable_words_file()
    print("Hello I am Wordle Solver!!! 🕵️ \nI am here to help you solve the wordle game today.. \n")
    tries = 0
    solution_found = False
    probable_word_list = get_words_from_file('./probable_words.txt')
    while tries < 6:
        print("\n\n🕵️  -> Currently words in our solution space is : " + str(len(probable_word_list)))
        print("\n🕵️  -> Probable words can be found in probable_words.txt...")
        tried_word = input("\n\n🕵️  -> Enter the word number " + str(tries+1) + " : \n")
        if len(tried_word) != 5:
            print("\n\n\n🕵️  -> Length of this word is not equal to 5... Did you enter correct word?? Check and re enter it boy... ")
            continue
        tries = tries + 1
        result = input("\n🕵️  -> Is this the correct answer?? If yes then, ENTER y/Y  else ENTER n/N...")
        if result == 'y' or result == 'Y':
            solution_found = True
            break
        probable_word_list = eliminate_words(tried_word.lower(), probable_word_list)
        write_five_letter_words_to_file(probable_word_list, './probable_words.txt')
    if solution_found:
        print("\n🕵️  ->  Congrats Buddy!!! We did it... 🤘 ")
    else:
        print("\n🕵️  -> Sorry buddy.. I will ask my creator to better me")



if __name__=="__main__":
	main()
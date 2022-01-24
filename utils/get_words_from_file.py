def get_words_from_file(file):
    word_list = []
    with open(file) as f:
        for line in f:
            word_list.append(line.strip('\n').lower())
    return word_list


def write_five_letter_words_to_file(five_letter_word_list, file):
    five_letter_word_file = open(file, 'w')
    for word in five_letter_word_list:
        five_letter_word_file.write(word + '\n')
    five_letter_word_file.close()
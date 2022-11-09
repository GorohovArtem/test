import string
# -*- coding:utf-8 -*-
def remove_symbols_in_file():
    str_punc = string.punctuation
    name_1 = input('Введите имя файла: ')
    stack = []

    with open(name_1, 'r+', encoding='utf-8') as f1:
        for line in f1:
            line_ready = line.split('\n')
            for words in line_ready:
                stack.extend(words.split(' '))

    for i in stack:
        if i == '':
            stack.remove('')

    for word in stack:
        for i in range(0, len(str_punc)):
            if word.find(str_punc[i]) != -1:
                correct_word = (stack[stack.index(word)]).replace(str_punc[i], '')
                stack[stack.index(word)] = correct_word

    return stack


def count_same_words(words):
    d = {}

    for w in range(0, len(words)):
        words[w] = words[w].lower()
        d[words[w]] = words.count(words[w])

    print('Топ повторяющихся слов: ')

    for key, value in d.items():
        if value >= 5:
            print(key, ':', value)


count_same_words(remove_symbols_in_file())
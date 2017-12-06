# -*- coding: utf-8 -*-

import chardet

def show_top_words():
    file_name = input('Введите имя файла:')
    try:
        with open(file_name, 'rb') as file:
            data = file.read()
            result = chardet.detect(data)
            text = data.decode(result['encoding'])
            text = text.split(' ')
            long_words = []
            for word in text:
                if '\n' in word:
                    word = word.replace('\n','')
                if len(word) > 6:
                    long_words.append(word)
            dict_of_words = dict((word, long_words.count(word)) for word in long_words)
            sorted_words = sorted(dict_of_words.items(), key=lambda x: x[1], reverse=True)
            for word in sorted_words[0:9]:
                print('{}: {}'.format(word[0], word[1]))
    except FileNotFoundError:
        print('Нет такого файла.')

if __name__ == '__main__':
    while True:
        show_top_words()

# -*- coding: utf-8 -*-
import random


IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
'''] #lista Constante

WORDS = ['love', 'home', 'smile', 'happy', 'computer', 'locura', 'tea']




def random_word():
    rand_num = random.randint(0,len(WORDS) - 1)
    word = WORDS[rand_num]
    return word


def display_game(word, tries):
    print(IMAGES[tries])
    print(tries)
    print(word)
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')


def game():
    #select a rando word form the array
    word = random_word()
    print(word)
    hiden_word = ['-'] * len(word)
    print(hiden_word)
    num_tries = 0 #contador

    while True:
        display_game(hiden_word, num_tries)
        current_letter = str(input('Give me a letter:'))

        letter_indexes = []
        for i in range(len(word)):
            if word[i] == current_letter:
                letter_indexes.append(i)


        if len(letter_indexes) == 0:
            num_tries += 1
            if num_tries == len(WORDS):
                display_game(hiden_word, num_tries)
                print('')
                print('Loser. the word was: {}'.format(word))
                break
        else:
            for j in letter_indexes:
                hiden_word[j] = current_letter

            letter_indexes = []


        try:
            hiden_word.index('-') #index return the index where the - is located inside the string/array
            #index also return a error if no index value is found
        except ValueError as e:
            print('')
            print('YAY, you won. Word is: {}'.format(word))
            print('')
            break




if __name__ == '__main__':
    print('Welcome to my hangman game! :)')
    game()

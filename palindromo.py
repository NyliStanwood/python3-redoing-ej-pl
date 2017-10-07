
def myfun():
    word = str(input('Write a word: '))
    res = palindrome(word)
    if res is True:
        print('{} si es un palindromo'.format(word))
    else:
        print('{} no es palindromo')


def palindrome(w):
    #give me the string from indice inicial al final en saldos de -1.... resulta en voltear la palabra
    #also_reversed_letters[::-1]
    reversed_letters = []

    for letter in w:
        reversed_letters.insert( 0 , letter )


    reversed_word = ''.join(reversed_letters)
    if reversed_word == w:
        return True
    else:
        return False



if __name__ == '__main__':
    myfun()

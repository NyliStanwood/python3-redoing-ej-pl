KEYS = { 'a': 'w', 'b': 'E', 'c': 'x', 'd': '1',
    'e': 'a', 'f': 't', 'g': '0', 'h': 'C', 'i': 'b',
    'j': '!', 'k': 'z', 'l': '8', 'm': 'M', 'n': 'I',
    'o': 'd', 'p': '.', 'q': 'U', 'r': 'Y', 's': 'i',
    't': '3', 'u': ',', 'v': 'J', 'w': 'N', 'x': 'f',
    'y': 'm', 'z': 'W', 'A': 'G', 'B': 'S', 'C': 'j',
    'D': 'n', 'E': 's', 'F': 'Q', 'G': 'o', 'H': 'e',
    'I': 'u', 'J': 'g', 'K': '2', 'L': '9', 'M': 'A',
    'N': '5', 'O': '4', 'P': '?', 'Q': 'c', 'R': 'r',
    'S': 'O', 'T': 'P', 'U': 'h', 'V': '6', 'W': 'q',
    'X': 'H', 'Y': 'R', 'Z': 'l', '0': 'k', '1': '7',
    '2': 'X', '3': 'L', '4': 'p', '5': 'v', '6': 'T',
    '7': 'V', '8': 'y', '9': 'K', '.': 'Z', ',': 'D',
    '?': 'F', '!': 'B', }


def cypher(msg):
    words = msg.split(' ')
    result = []
    for w in words:
        current_word = ''
        for letter in w:
            current_word += KEYS[letter]


        result.append(current_word)


    return ' '.join(result)


def decypher(msg):
    words = msg.split(' ')
    result = []
    for w in words:
        current_word = ''
        for letter in w:
            for key, value in KEYS.items():
                if value == letter:
                    current_word += key


        result.append(current_word)

    return ' '.join(result)


def run():
    while True:
        option = str(input('''--- * --- * --- * --- * --- * --- * --- * ---

            Welcome. What do you want to do?

            [e] encrypt message
            [d] decrypt message
            [x] exit
        '''))
        if option == 'e':
            print('Encrypt Message')
            message = str(input('message: '))
            encrypted_msg = cypher(message)
            print('')
            print(encrypted_msg)
        elif option == 'd':
            print('Decrypt Message')
            message = str(input('message: '))
            decrypted_msg = decypher(message)
            print('')
            print(decrypted_msg)
        elif option == 'x':
            print('Exit')
            break
        else:
            print('Exit')
            break



if __name__ == '__main__':
    print('Encripted Messages')
    run()

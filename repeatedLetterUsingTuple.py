"""
"abacabad" c
"abacabaabacaba" _
"abcdefghijklmnopqrstuvwxyziflskecznslkjfabe" d
"bcccccccccccccyb" y
"""


def first_not_repeating_char(sequence):
    seen_letters = {}
    # enumerate(sequence) returns a list with the characters in the sequence
    for index , current_letter in enumerate(sequence):
        #si la letra a ctual no esta en la lista de las letras vistas
        if current_letter not in seen_letters:
            #agregamos la letra al dictionary de letras vistas
            # = guardamos una tupla con el indice en el que la vimos y el numero de veces que la he visto
            seen_letters[current_letter] = ( index , 1 )# 1 because its the first time
        else:
            #ya vimos la letra, entonces encontramos y actualizamos(reemplazamos la tupla) en el diccionario...
            #creamos una nueva tupla con los valores de entrar al diccionario seen_letters[current_letter] y luego al primer valor de la tupla [0] y despues al segundo valor [1] que es int y le agregamos 1
            seen_letters[current_letter] = ( seen_letters[current_letter][0], seen_letters[current_letter][1] + 1 )


    final_letters = []
    for idx_key, tupla_value in seen_letters.items():
        if tupla_value[1] == 1:
            #append a new tupla con el index y el valor de veces repetidas
            final_letters.append( ( idx_key, tupla_value[0])) #[('a', 3), ('b', 7)] 3 y 7 son el indice en la cadena de caracteres

    not_repeated_letters = sorted(final_letters , key=lambda tupla_value: tupla_value[1])
    #lambda value: value[1] // lambda function recibe una tupla y regresa el primer valor de la tupla
    #def sort_order(value):
    #    return value[1]

    if not_repeated_letters:
        return not_repeated_letters[0][0]
    else:
        return '_'



if __name__ == '__main__':
    char_sequence = str(input('Give me a char sequence: '))
    res = first_not_repeating_char(char_sequence)
    if res == '_':
        print('All characters are repeated')
    else:
        print('The first character not repeated is {}'.format(res))

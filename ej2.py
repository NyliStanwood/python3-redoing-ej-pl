# -*- coding: utf-8 -*-
import random
import os

name = str(input('nombre?'))
print('Hola ' + name)

def sumaa(x , y):
    return x + y

res = sumaa(5 , 5)
print(res)

my_string = 'marilyn'

lenght = len(my_string)
print(my_string)
print(lenght)

#to acces the caracters

my_string[0]
my_string[1]
my_string[2]

last_caracter = my_string[len(my_string) - 1] #porque empieza en 0
print(last_caracter)

my_string_UPPER = my_string.upper()
print(my_string_UPPER)
my_string_Lower = my_string.lower()
print(my_string_Lower)

positionNum = my_string.find('y') #encuentra la posicion de este caracter en el string
print(positionNum)

#slices ....

# give me string drom caracter in 2nd position to the end
my_string[1:]

#give me the string from indice 1 al indice 3 (sin incluir el 3)
my_string[1:3]

#give me the string from indice 1 al indice 6 en saltos de 2
my_string[1:6:2]

#give me the string from indice inicial al final en saldos de -1.... resulta en voltear la palabra
my_string[::-1]

#receta_string[inicio:final:pasos]

#crea una sequencia de 5 items del 0 al 4
list(range(5))

#list(range(inicio:final:pasos))
#genera una sequencia del 5 al 40 de 3 en 3
list(range(5,40,3))

for i in range(30):
    if i % 3 != 0:
        continue
    else:
        print('num' + str(i) + 'al cuadrado=' + str(i**2) )



for x in range(30):
    if x % 3 == 0:
        continue
    elif x == 20:
        break
    else:
        print(x)


my_string = "this is a very long string yay yay yay"

for letter in my_string:
    print(letter)


i = 10
while i > 0:
    print('here in the loop')
    i = i - 1


found = False
random_num = random.randint(0, 20)

while not found:
    os.system('clear') #Clear the console
    num = int(input('Intenta un num'))
    if num == random_num:
        print('yay, you found it!')
        found = True
        #break
    elif num < random_num:
        print('num is <')
    else:
        print('num is >')

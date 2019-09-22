amigos = list()
#saber el typo de dato de una variable
type(amigos)
amigos2 = [] #lista vacia

amigos.append('bicho') #agrega al final
amigos.append('nery')
amigos.append('tava')

#se puede acceder con el indice
amigos[2]
#EDITAR lista
amigos[0] = 'david' #reemplaza bicho por david
friend = amigos.pop() #elimina el ultimo amigo tava y lo salva en mi variable friend

familia = ['annie', 'brian', 'june', 'joe']
amigos.extend(familia)
#>>> print(amigos)
#['david', 'nery', 'annie', 'brian', 'june', 'joe']

#SORT
anotherList = [6,8,3,5,8,0,3,4]
anotherList.sort()
#>>> anotherList
#[0, 3, 3, 4, 5, 6, 8, 8]


#DELETING
#['david', 'nery', 'annie', 'brian', 'june', 'joe']
del amigos[0]
#borrara el item 0 (david)
#['nery', 'annie', 'brian', 'june', 'joe']




# STRING TO LIST - LIST TO string
str_casa = 'casa'
list_casa = list(str_casa)
#>>> list_casa
#['c', 'a', 's', 'a']
joined_casa = ''.join(list_casa)
#>>> joined_casa
#'casa'

joined_casa = ''.join(list_casa)

mi_lista_a = ['a', 'b', 'c']
mi_lista_b = [1, 2, 3]

lista3 = mi_lista_a + mi_lista_b

lista_c = ['a']

lista4 = lista_c * 10
#>>> lista4
#['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']

list_nums = list(range(5,20))
list_nums
#>>>[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
list_nums[1:]
#no incluye la primera posisicon hasta el final
#>>>[6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
list_nums[1:3]
#de la segunda posicion a la cuarta
#>>>[6, 7]
list_nums[1:10:2]
#de la 2nda posicion a la 9vena posicion de 2 en 2
#>>>[6, 8, 10, 12, 14]
list_nums[::-1]
#en reversa
#>>>[19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5]

#==================================================
#  TUPLAS
tupla1 = (1,)
tupla2 = (5,6,7)

newt = tupla1 + (2,3,4)



def average_temp(t):
    sum_t = 0
    for i in t:
        sum_t += float(i)


    return sum_t / len(t)

if __name__ == '__main__':
    temps = list(range(21,35))
    a = average_temp(temps)

    print('average temp {}'.format(a))

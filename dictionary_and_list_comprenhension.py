#sintactic sugar

#find pares in a list of numbers
list1 = list(range(1,31))

def pares_func(l):
    pares = []
    for value in l:
        if value % 2 == 0:
            pares.append(value)


    return pares


pares_list = pares_func(list1)
print(pares_list)


#same code as before!!!!! OMG
even = [num for num in range(1, 31) if num % 2 == 0 ]


#============================================
#Dictionary

def dict_num_square(l):
    dicti = {}
    for value in l:
        dicti[value] = value**2


    return dicti


squares = dict_num_square(list1)
print(squares)

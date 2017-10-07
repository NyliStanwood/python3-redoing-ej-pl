
my_dictionary = {}
dictionary2 = dict()

my_dictionary['element_one'] = 'hello'
my_dictionary['element_two'] = 'bye'
my_dictionary['element_three'] = 'boo'

#to access the values we use the keys

#iterating over a dictionary

grades = {}
grades['spanish'] = 9
grades['math'] = 7
grades['prog 101'] = 10
grades['web 101'] = 8
grades['algorithms'] = 6

for key in grades:
    print(key)


for value in grades.values():
    print(value)


for key, value in grades.items(): #.iteritems in p2
    print('key: {}, valor: {}'.format(key, value))

sum_grades = 0
for eachGrade in grades.values():
    sum_grades += eachGrade


avg = sum_grades / len(grades.values())
print('average = ' + str(avg))

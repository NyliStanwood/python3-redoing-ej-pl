"""
File: ejemplo_inicial.py

"""

import turtle


def main():
    window = turtle.Screen()

    nyli = turtle.Turtle()
    make_square(nyli)
    turtle.mainloop()


def make_square(nyli):
    lenght_of_line = int(input('Tamanio?:'))
    for i in range(4):
        make_line_and_turn(nyli, lenght_of_line)
    

def make_line_and_turn(nyli, lenght_of_line):
    nyli.forward(lenght_of_line)
    nyli.left(90)


if __name__ == '__main__':
    main()

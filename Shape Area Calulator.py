import math
from math import pi

def print_options():
    print("****Please choose one of the following*******")
    print(" p - print options")
    print(" c - work out area of a circle")
    print(" s - work out area of a square")
    print(" r - work out area of a rectangle")
    print(" q - quit the program")

print_options()
choice = input("Option: ")

def calc_circle():
    radiusCircle = float(input ("Input the radius of the circle : "))
    print ("The area of the circle is " + str(pi * radiusCircle**2))

def calc_square():
    length = float(input ("Input the height of the square : "))
    print("The area of the square is " + str(length*length))

def calc_rectangle():
    height = float(input("Input the height : "))
    width = float(input("Input the width : "))
    print("The area of the rectangle is " + str(width*height))


while choice != "q":

    if choice == "c":
        calc_circle()
        
    elif choice == "s":
        calc_square()

    elif choice == "r":
        calc_rectangle()

    elif choice == "p":
        print_options()
        choice = input("option: ")

    else:
        print("an invalid choice has been entered, please try again")

    print_options()
    choice = input("Option: ")

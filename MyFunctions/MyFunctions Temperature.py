# MyFunctions Program
# By Kyle Joyce

def print_options():
    print("****Please choose one of the following*******")
    print(" p - print options")
    print(" c - convert FROM celsius")
    print(" f - convert FROM fahrenheit")
    print(" q - quit the program")

def celsius_to_fahrenheit(c_temp):
    return 9.0 / 5.0 * c_temp + 32

def fahrenheit_to_celsius(f_temp):
    return (f_temp - 32.0) * 5.0 / 9.0

print_options()
choice = input("Option: ")
while choice != "q":

    if choice == "c":
        c_temp = float(input("Celsius temperature: "))
        print("the fahrenheit temperature is", celsius_to_fahrenheit(c_temp))

    elif choice == "f":
        f_temp = float(input("Fahrenheit temperature: "))
        print("The celsius temperature is", fahrenheit_to_celsius(f_temp))

    elif choice == "p":
        print_options()

    else:
        print("an invalid choice has been entered, please try again")

    print_options()
    choice = input("Option: ")

print("Goodbye")

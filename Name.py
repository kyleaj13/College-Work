def test():
        working = input("Is this correct? Yes/No ").capitalize()
        if working == ("Yes"):
            print("My code is working! ")
        elif working == ("No"):
            print("Then you typed it wrong! ")
        else :
            print("That is not a valid answer")
            restart = input("Would you like to restart? Yes/No ").capitalize()
            if restart == "Yes":
                print("")
                print("So your name is", name, surname, "and you are", age, "years old.")
                test()
            else:
                print("Ok, thanks for using my program!")

def program():
    name = input("What is your first name? ")
    surname = input("What is your surname? ")
    age = input("How old are you? ")
    print("So your name is", name, surname, "and you are", age, "years old.")
    print(age + 1)
    test()
    
program()
varA = input("Would you like to restart? Yes/No ").capitalize()
if varA == "Yes":
    program()
else:
    import sys
    sys.exit()
        

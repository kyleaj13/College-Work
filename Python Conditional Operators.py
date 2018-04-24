age = int(input("What is your age? "))
if age >= 18:
    print("You are old enough to vote!")
else:
    print("You are not old enough to vote.")
    print("You will be able to vote in", int(18) - int(age), "year(s)")

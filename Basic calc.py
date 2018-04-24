number_one = int(input("First Number: "))
operator = input(": ")
number_two = int(input("Second Number: "))
def add_numbers(x, y):
    return x + y

total = add_numbers(12, 2)
print(total)

def times_numbers(i, z):
    return i * z

total = times_numbers(number_one, number_two)
print(total)

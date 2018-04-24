# MyFunctions Program
# By Kyle Joyce

def calculate(num1,num2):
    num3 = num1 + num2
    if num3 > 100:
        return "The sum value is over 100"
    else:
        return "The sum value is less than 100"

print(calculate (10, 100))

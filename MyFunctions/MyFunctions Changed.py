# MyFunctions Program
# By Kyle Joyce

def changeme(myList):
    myList.append(1)
    print("Values in the function:", myList)
    return

myList = [10,11,12]
changeme(myList)
print("Values outside the function:", myList)

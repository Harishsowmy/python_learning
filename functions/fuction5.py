def add(number_1,number_2):
    return number_1+number_2

def subtract(number_1,number_2):
    return number_1-number_2

def multiply(number_1,number_2):
    return number_1*number_2

def divide(number_1,number_2):
    return number_1/number_2

print("name of the file is", __name__)
if __name__=="__main__":
    addition=add(12,34)
    subtraction=subtract(34,12)
    multiplycation=multiply(50,50)
    divison=divide(30,6)

    print("addtion:",addition)
    print("subtraction:",subtraction)
    print("divison:",divison)
    print("multiply:",multiplycation)

    what=add(addition, subtract(subtraction, multiply(multiplycation,divide(divison,2))))
    print("what:",what)
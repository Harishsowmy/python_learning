from fuction5 import add,subtract,divide,multiply

def calculator(op, nuber1,nuber2):
    if op=="add":
        return add(nuber1,nuber2)
    elif  op=="subtract":
        return subtract(nuber1, nuber2)
    elif op=="multiply":
        return multiply(nuber1,nuber2)
    elif op=="divide":
        return divide(nuber1,nuber2)
    else:
        return "wrong oprition"

print("name of this file", __name__)
if  __name__ == "__main__":
    
    nuber1=10
    nuber2=20
    print(calculator("add", nuber1,nuber2))
    print(calculator("subtract",nuber1,nuber2))
    print(calculator("multiply",nuber1,nuber2))
    print(calculator("divide",nuber1,nuber2))
    print(calculator("addition",nuber1,nuber2))
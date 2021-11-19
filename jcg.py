import math560 as m

def get_inputs():
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    
    added = m.addition(a, b)
    subtracted = m.subtract(a, b)
    multiplied = m.multiply(a, b)
    divided = m.divide(a, b)
    exponent = m.exponent(a, b)
    root = m.squareRoot(a)

    print("a + b =", added)
    print("a - b =", subtracted)
    print("a * b =", multiplied)
    print("a / b =", divided)
    print("a ^ b =", exponent)
    print("a ^ (1/b) =", root)

get_inputs()
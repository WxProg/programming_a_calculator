#Calculator 
from art import logo

def add(n1, n2):
    return n1 + n2
    
def subtract(n1, n2):
    return n1 - n2
    
def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

def exponent (n1, n2):
    return n1 ** n2

operators = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
    "**": exponent,

}

def calcuator():
    print(logo)
    
    num1 = float(input("What's the first number?: "))
    for key in operators:
        print(key)
    should_continue = True
    
    while should_continue:
        operators_key = input("Pick an operator: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operators[operators_key]
        answer = calculation_function(num1,num2)
        
        print(f"{num1} {operators_key} {num2} = {answer}")
    
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation ") == "y":
            num1 = answer
        else:
            should_continue = False
            calcuator()
            
calcuator()
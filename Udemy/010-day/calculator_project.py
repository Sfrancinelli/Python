# Calculator

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
"+" : add, 
"-" : substract, 
"*" : multiply, 
"/" : divide
}

num1 = float(input("What's the first number?: \n")) 

for symbol in operations:
    print(symbol)
function = input("Pick an operation from the lines above: \n")

num2 = float(input("What's the second number?: \n")) 

for symbol in operations:
    if function == symbol:
        answer = operations[symbol](num1,num2)

print(f"{num1} {function} {num2} = {answer}")

keep_going = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: \n").lower()

while keep_going == 'y' or keep_going == 'n':

    function = input("Pick an operation: \n")
    num3 = float(input("What's the next number?: \n"))

    total = answer

    answer = operations[function](total, num3)

    print(f"{total} {function} {num3} = {answer}")
    keep_going = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: \n").lower()
    if keep_going == 'n':
        asnwer = 0
        num1 = float(input("What's the first number?: \n"))
        function = input("Pick an operation: \n")
        num2 = float(input("What's the second number?: \n")) 
        answer = operations[function](num1,num2)
        print(f"{num1} {function} {num2} = {answer}") 
        keep_going = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: \n").lower()

print("Goodbye!")
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

num1 = int(input("What's the first number?: \n")) 

for symbol in operations:
    print(symbol)
function = input("Pick an operation from the lines above: \n")

num2 = int(input("What's the second number?: \n")) 

# for symbol in operations:
#     if function == symbol and function == "+":
#         answer = add(num1,num2)
#     elif function == symbol and function == "-":
#         answer = substract(num1,num2)
#     elif function == symbol and function == "*":
#         answer = multiply(num1,num2)
#     elif function == symbol and function == "/":
#         answer = divide(num1,num2)

for symbol in operations:
    if function == symbol:
        answer = operations[symbol](num1,num2)

total = answer

print(f"{num1} {function} {num2} = {answer}")

keep_going = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: \n").lower()

while keep_going == 'y':

    function = input("Pick another operation: \n")
    num3 = int(input("What's the next number?: \n"))

    total = answer

    answer = operations[function](total, num3)

    print(f"{total} {function} {num3} = {answer}")
    keep_going = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: \n").lower()

print("Goodbye!")
#Write your code below this line 👇

# def prime_checker(number):
#     if number == 1 or number == 2 or number == 3 or number == 5 or number == 7:
#         print("It's a prime number.")
#     elif number % 2 == 0 or number % 3 == 0 or number % 4 == 0 or number % 5 == 0 or number % 6 == 0 or number % 7 == 0 or number % 8 == 0 or number % 9 == 0:
#         print("It's not a prime number.")
#     else: 
#         print("It's a prime number.")

# Code above 👆 working but inefficient

def prime_checker(number):
    prime = True
    for i in range(2,number):
        if number % i == 0:
            prime = False
    
    if prime:
        print("It's a prime number.")
    elif not prime:
        print("It's not a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
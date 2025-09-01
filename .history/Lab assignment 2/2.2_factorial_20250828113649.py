def factorial(x):
    return x*factorial(x-1)
user_input=int(input("Enter the number to find factorial"))
factorial(user_input)
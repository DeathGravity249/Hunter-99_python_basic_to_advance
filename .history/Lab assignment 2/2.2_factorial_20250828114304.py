def factorial(x):
    if x==0:
        return 1
    result =x*factorial(x-1)
    print(result)
user_input=int(input("Enter the number to find factorial : "))
Solution =factorial(user_input)

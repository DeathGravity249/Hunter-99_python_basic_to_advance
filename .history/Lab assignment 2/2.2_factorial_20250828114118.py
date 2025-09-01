def factorial(x):
    if factorial(x)==0:
        return 
    result =x*factorial(x-1)
    print(result)
user_input=int(input("Enter the number to find factorial : "))
Solution =factorial(user_input)

def factorial(x):
    if x==0:
        return 1
    
    return x*factorial(x-1)
    
user_input=int(input("Enter the number to find factorial : "))
Solution =factorial(user_input)
print(Solution)

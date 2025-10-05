def check_is_prime(x):
    i=0
    while(i<x):
        if(x%i==0):
            print("the given no is prime ")
            break
        
x=int(input("Enter the number : "))
check_is_prime(x)
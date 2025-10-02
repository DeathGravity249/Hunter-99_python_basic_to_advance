def check_is_prime(x):
    i=0
    while(i<x):
        if(x%i==0):
            print("the given not is prime ")
            break
        i+=1
    return P
x=int(input("Enter the number : "))
check_is_prime(x)
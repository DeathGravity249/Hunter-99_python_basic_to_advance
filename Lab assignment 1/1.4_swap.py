def swap (a,b):
    a=a+b 
    b=a-b
    a=a-b
    return a,b

    
x=int(input("Enter the no 1 : "))
y=int(input("Enter the no 2 : "))
swap(x,y)

print("After the swap: ",swap(x,y))
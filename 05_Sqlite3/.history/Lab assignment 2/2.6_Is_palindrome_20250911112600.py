def reverse(x):
    number=0
    while(x!=0):
        digit=x%10
        number=number*10+digit
        x/10
return number

x=int(input("Enter the number : "))
reverse(x)
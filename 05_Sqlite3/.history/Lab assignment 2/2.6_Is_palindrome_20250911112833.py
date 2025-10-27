def reverse(x):
    number=0
    while(x!=0):
        digit=x%10
        number=number*10+digit
        x/10
    return number

x=int(input("Enter the number : "))
result=reverse(x)
if(x==result):
    print("The number is palindrome  ")
else:
    print("The is not palindrome ") 
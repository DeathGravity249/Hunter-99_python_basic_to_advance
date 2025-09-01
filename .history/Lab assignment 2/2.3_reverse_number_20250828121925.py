def reverse(x):
    while(x!=0):
        digit=x%10
        reversing_num=digit*10+reversing_num
        
x=int(input("Enter the number to be reversed : "))
reverse(x)
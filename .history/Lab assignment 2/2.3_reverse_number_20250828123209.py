def reverse(x):
    reversing_num=0
    while(x!=0):
        digit=x%10
        reversing_num=reversing_num*10+digit
       
    print (reversing_num)
x=int(input("Enter the number to be reversed : "))
reverse(x)
## In cpp / perform integer division , 123/10=12 (decimal part get truncated)
## IN python /->perfomrm folating point division , 123/10=12.3 ( dont get truncated )
## 
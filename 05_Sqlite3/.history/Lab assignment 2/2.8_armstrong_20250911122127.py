## armstrong number n->no of digit , is is number whose each digit nth time square
## and its sums is equalt to the same number 
def armstrong_nums(x):
    sum=0
    nums_digit=len
    while(x!=0):
        nums=0
        digit=x%10
        nums = digit**
        sum=sum + nums
        x=x//10
    return sum 
    
x=int(input( "Enter number : "))
y=x
result =armstrong_nums(x)
if(result==y):
    print("The input number is armstrong no. ")
else :
    print("The number is not armstrong number ")
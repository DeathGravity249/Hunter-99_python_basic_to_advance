## WE can alternatively use the return in place of print and print outside the funcion 
def even_or_odd(num):
    if num<0 :
         print("You entered negative number ")
    elif num%2==0 :
        print("Entered number is even number : ")
    else :
        print("The number is odd number ")
num=int(input("Enter the number : "))
even_or_odd(num) 
# Write a program that asks the user to input a number and prints whether the number is positive and even, positive and odd
input_num=int(input("Enter the number : "))
if(input_num>0):
    print("The input number is positive ")
elif(input_num<0):
    print("The input number is negative ")
else:
    if(input_num==0):
        print("The input number is zero ")
    else :
        print("Invaild input !! ")

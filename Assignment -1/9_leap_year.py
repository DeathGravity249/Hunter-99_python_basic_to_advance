input_year=int(input("Enter the  year : "))
if(input_year%4==0):
    if(input_year%100==0):
        if(input_year%400==0):
            print("The above year is leap year ")
        else:
            print("The above year provide is not leap year")
    else:
         print("The above year provide is not leap year")
else:
    print("The above year provide is not leap year")
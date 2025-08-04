def is_km_or_mile(unit):
    if unit.lower()=="km":
        print("Entered value is in km")
        return 1
    elif unit.lower()=="miles":
        print("Entered value is in Miles")
        return -1
    else :
        print("Invalid input")
num=float(input("Enter the input "))
unit=input("Enter the unit KM or Mile : ")
result =is_km_or_mile(unit)
if (result==1):
    num*=0.0621
    print("Km to Miles",num)
elif(result==-1):
    num*=1.609
    print("miles to km",num)
else :
    print("Invalid input !")
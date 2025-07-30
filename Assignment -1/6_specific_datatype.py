# Else cannot not have codition so we need to use elif
x=3.5
if ((isinstance(x,int))):
    print("It is integer ")
elif(isinstance(x,str)):
    print(" It is string  ")
elif isinstance(x,float):
    print("It is float no.")
else :
    print(" It is of some other type")
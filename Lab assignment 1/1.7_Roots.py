def roots(a,b,c):
    if a==0 :
        return "Root is not defined"
    elif (b**2-4*a*c)<0:
        return "No real roots : "
    else:
        root1=(-b+(b**2-4*a*c)**0.5)/(2*a)
        root2=(-b-(b**2-4*a*c)**0.5)/(2*a)
        return(root1,root2)
    
a=int(input("Enter the coeffcient of x^2: "))
b=int(input("Enter the coefficient of x: "))
c=int(input("Enter the constant : "))

print("Roots are : ",roots(a,b,c))
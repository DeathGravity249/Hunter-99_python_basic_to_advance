def emi_calculation(p,r,n):
    Emi=(p*r*(1+r)**n)/((1+r)**n-1) ## Here it is treated like formula
    print(f"The Total EMI : {Emi:.2f}")
    total_payment=Emi*n
    print(f"The total amount payable : {total_payment:.2f}")

p=float(input("Enter the principal :  "))
r=float(input("Enter the rate :  "))
r/=(12*100)
n=float(input(" Total montly installment input -> years :  "))
n*=12
emi_calculation(p,r,n)


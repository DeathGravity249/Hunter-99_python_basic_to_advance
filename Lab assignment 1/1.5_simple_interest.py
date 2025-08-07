def simple_interest(p,r,t):
    interest=(p*r*t)/100
    total_amount=p+interest
    print("The amount after simple interest : ",total_amount)

def compound_interest(p2,r2,n,t2):
    Final_amount=p2*(1+(r2/n))**(n*t2)
    print("The Final amount after CI : ",Final_amount)

p=float(input("Enter the principal : "))
t=float(input("Enter the year  : "))
r =float(input("Enter the rate : "))
simple_interest(p,r,t)
# compound_interest(p,r,t)
print("Now enter info for comppund interest : ")
p2=float(input("Enter the principal : "))
r2=float(input("Enter the rate in "))
r2/=100
n=int(input("Enter the no of time p2 is compounded "))
t2=float(input("Enter the time in years : "))
compound_interest(p2,r2,n,t2)


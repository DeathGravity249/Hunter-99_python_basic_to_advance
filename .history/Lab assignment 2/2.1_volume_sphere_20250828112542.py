## creating a program to calculate volume of the sphere when radius is given in double form
## In programming double means 
def Volume_sphere(r):
     result=(4/3)*(22/7)*(r**3)
     print(result)
input=float(input("Enter the value in double form : "))
radius=input/2
Volume_sphere(radius)
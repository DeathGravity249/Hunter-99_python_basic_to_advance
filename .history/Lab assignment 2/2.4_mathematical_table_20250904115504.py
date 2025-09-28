def table(n):
    if n==0:
        return 1
    for i in range(n):
        print(f"the table of {n} :")
         
n=int(input("Enter the number n : "))
table(n)
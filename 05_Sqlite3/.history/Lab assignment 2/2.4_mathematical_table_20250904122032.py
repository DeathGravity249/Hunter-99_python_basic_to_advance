def table(n):
    for i in range(n):
        print(f"the table of {i} is : ")
        for j in range(1,11):
           print(f"{i*j}")


n=int(input("Enter the number n : "))
table(n)
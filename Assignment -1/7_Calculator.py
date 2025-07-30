x = int(input("Enter the number : "))
y = int(input("Enter the second number : "))
operator = input("Enter the operator: ")
result=None
if operator == '+':
    result = x + y
    print("Result:", result)
elif operator == '-':
    result = x - y
    print("Result:", result)
elif operator == '*':
    result = x * y
    print("Result:", result)
elif operator == '/':
    if y == 0:
        print("Error! Division by zero.")
        
    else:
        result = x / y
        print("Result:", result)
else:
    print("Invalid operation")

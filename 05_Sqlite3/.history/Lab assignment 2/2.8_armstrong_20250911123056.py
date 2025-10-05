## armstrong number n->no of digit , is is number whose each digit nth time square
## and its sums is equalt to the same number 
def armstrong_nums(x):
    sum = 0
    nums_digit = len(str(x))
    temp = x  # Save the original number
    while temp != 0:
        digit = temp % 10
        sum += digit ** nums_digit
        temp = temp // 10
    return sum

x = int(input("Enter number: "))
result = armstrong_nums(x)

if result == x:
    print("The input number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")


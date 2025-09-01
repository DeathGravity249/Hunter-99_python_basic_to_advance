def reverse(x):
    reversing_num=0
    while(x!=0):
        digit=x%10
        reversing_num=reversing_num*10+digit
       
    print (reversing_num)
x=int(input("Enter the number to be reversed : "))
reverse(x)
In C++:
/ performs integer division when both operands are integers

123 / 10 gives 12 (decimal part truncated)

In Python:
/ always performs floating-point division (returns float)

123 / 10 gives 12.3 (does NOT truncate)

// performs integer division (truncates decimal part)

123 // 10 gives 12

Comparison:
Operation	C++ Result	Python Result	What you need
123 / 10	12 (int)	12.3 (float)	❌ Wrong for this case
123 // 10	12 (int)	12 (int)	✅ Correct for this case

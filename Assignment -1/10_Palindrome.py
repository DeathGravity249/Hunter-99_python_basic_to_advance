input_str=input("Enter the string ")
lst1=input_str[0:]
lst2=input_str[::-1]
if(lst1==lst2):
    print("The Entered string is palindrome")
else:
    print("The above string is not palindrome ")
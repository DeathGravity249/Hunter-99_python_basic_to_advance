def conversion_to_years(days):
    if days==0 :
        return "No. of days empty"
    # year=int(days/365) # for simple division
    year=int(days//365)  # floor division
    return year
def conversion_to_months(days):
    if days==0:
        return "No. of days empty"
    count=0
    while days!=0:
        if days>31:
            count+=1
            days-=31    
        if days>30:
            days/30
            count+=1
            days-=30  
        else :
            break
        return f"The total months are : {count}" 
    return f"The total month are: {count}"

days=int(input("Enter the total days : "))
print("the total year : ",conversion_to_years(days))
print("The total perfect months are : ",conversion_to_months(days))

## Below is the gpt version concise one 

# def conversion(days):
#     if days == 0:
#         return "No. of days entered"

#     years = days // 365   # how many full years
#     days = days % 365     # leftover days after years

#     months = days // 30   # how many full months from leftover days
#     days = days % 30      # leftover days after months

#     return f"Years: {years}, Months: {months}, Days: {days}"

# # input
# days = int(input("Enter the total days: "))

# print(conversion(days))

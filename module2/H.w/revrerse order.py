#Get the input from the user
number=input("enter a number:")
#If the number is negative remove the '-' sign so it isn't counted as a digit
number=number.replace("-","")
#calculate the length of the string
count=len(number)
print(f"The number of digits is:{count}")
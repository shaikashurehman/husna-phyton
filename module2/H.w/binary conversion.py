#The number we want to convert
number=int(input("enter a number:"))
binary=""
#keep dividing by 2 until the number becomes 0
while number > 0:
    remainder=number%2
    binary=str(remainder)+binary
    number=number//2
print("the binary result is:",binary)
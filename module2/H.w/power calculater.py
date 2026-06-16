#program to calculate power using a for loop
base=int(input("enter the base number:"))
exponent=int(input("enter the exponent"))
result=1
#using a for loop to multiply the base by itself 'exponent' times
for i in range(exponent):
    result=result*base
print(f"{base} raised to the poewer of {exponent} is {result}")
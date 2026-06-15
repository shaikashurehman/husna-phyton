# 1) Display a menu asking the user to select a ride:

# - 1 for Bike

# - 2 for Car

# 2) Take the user’s input and store it in `choice`.

# 3) If `choice` is 1 (Bike):

# a) Show bike options (Scooty / Scooter)

# b) Take the user’s input for bike type and store it in `choice2`

# c) If `choice2` is 1, print "you have selected scooty"

# Else, print "you have selected scooter"

# 4) Else if `choice` is 2 (Car):

# a) Show car options (Sedan / XUV)

# b) Take the user’s input for car type and store it in `choice3`

# c) If `choice3` is 1, print "you have selected sedan"

# Else, print "you have selected XUV"

# 5) Else (if `choice` is not 1 or 2):

# Print "Wrong choice!"

print("select ur ride 1.bike 2.car")
choice=int(input("enter ur choice"))
if choice==1:
    print("select what type of bike 1.scooty 2.scooter")
    choice2=int(input("enter ur choice"))
    if choice2==1:
        print("enjy ur scooty")
    else:
        print("enjoy ur scooter")

else:
    print("select ur car 1.maruthi 2.xuv")
    choice2=int(input("enter ur choice"))
    if choice2==1:
        print("enjy ur maruthi")
    else:
        print("enjoy ur xuv")
           
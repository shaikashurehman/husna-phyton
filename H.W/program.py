#A simple program to check if an input character is an alphabet
#1.Get input from the user
user_char=input("enter a single character:")
#2.Add some safety to check if they entered more than one char,to match the problem description
if len(user_char)!=1:
    print("invalid input.please enter exactly one character.")
else:
    #3.peform the check using comparison opertors(">="and"<=") and logical operators("and","or")
    #In python,you can compare strings/characters directly using standard comparisons.
    #We check if the character is between'A'and'Z' inclusive, or between'a' and 'z' inclusive.
    if('A'<= user_char<='Z') or ('a'<= user_char<='z'):
        print(f"'{user_char}' is an alphabet letter.")
    else:
        #4.if neither condition is met,it;s not a letter.
        print(f"'{user_char}' is NOT an alphabet letter.")
#5.Program ends gracefully
print("Check complete.")     
    
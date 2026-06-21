secret=27
attempts=0
maxattempts=5
while attempts<maxattempts:
    guess=int(input("guess a number"))
    atempts=attempts+1
    if guess==secret:
        print("you win")
    else:
        print("try again")


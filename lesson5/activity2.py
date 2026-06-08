cp=int(input("enter the cp"))
sp=int(input("enter the sp"))
if sp>cp:
    profit=sp-cp
    print("profit=",profit)
else:
    loss=cp-sp
    print("losss",loss)    
print("Press 1 for Pizza")
print("Press 2 for Maggie")
print("Press 3 for burger")
print("Press 4 for Burrito")
dishno= int(input("enter dishno=>"))
if dishno==1:
    print("price of pizza 400")
    qty=int(input("Enter qty of Pizza =>"))
    print("Bill of Pizza = ",qty*400)
elif dishno==2:
    print("price of maggie 300")
    qty= int(input("enter qty of maggie =>"))
    print("bill of maggie =" , qty*300)
elif dishno==3:
    print("price of burger 230")
    qty=int(input("enter qty of burger"))
    print("bill of burger=" , qty*230)
elif dishno==4:
    print("price of burrito 250")
    qty=int(input("enter qty of burrito =>"))
    print("bill of burrito=",qty*250)
else: print("not available")



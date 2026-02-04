print("Press p for Pizza")
print("Press m for Maggie")
print("Press b for burger")
print("Press c for Burrito")
dishno=input("enter dishno=>")
if dishno=="p" or dishno=="P":
    print("price of pizza 400")
    qty=int(input("Enter qty of Pizza =>"))
    print("Bill of Pizza = ",qty*400)
elif dishno=="m" or dishno=="M":
    print("price of maggie 300")
    qty= int(input("enter qty of maggie =>"))
    print("bill of maggie =" , qty*300)
elif dishno=="b" or dishno=="B":
    print("price of burger 230")
    qty=int(input("enter qty of burger"))
    print("bill of burger=" , qty*230)
elif dishno=="c" or dishno=="C":
    print("price of burrito 250")
    qty=int(input("enter qty of burrito =>"))
    print("bill of burrito=",qty*250)
else: print("not available")



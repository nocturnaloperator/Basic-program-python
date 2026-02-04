print("Press pizza")
print("Press maggie")
print("Press burger")
print("Press burrito")
dishno=input("enter dishno=>").lower()
if dishno=="pizza":
    print("price of pizza 400")
    qty=int(input("Enter qty of Pizza =>"))
    print("Bill of Pizza = ",qty*400)
elif dishno=="maggie":
    print("price of maggie 300")
    qty= int(input("enter qty of maggie =>"))
    print("bill of maggie =" , qty*300)
elif dishno=="burger":
    print("price of burger 230")
    qty=int(input("enter qty of burger"))
    print("bill of burger=" , qty*230)
elif dishno=="burrito":
    print("price of burrito 250")
    qty=int(input("enter qty of burrito =>"))
    print("bill of burrito=",qty*250)
else: print("not available")



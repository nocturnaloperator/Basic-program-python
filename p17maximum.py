num1=int(input("enter number =>"))
num2=int(input("enter number =>"))
num3= int(input("enter number =>"))
if num1>num2 and num1>num3:
    print(" number1 is maximum ")
elif num2>num1 and num2>num3:
    print(" number2 is greater")
elif num3>num2 and num3>num1:
    print(" number3 is greater")
else:
    print("All are equal")
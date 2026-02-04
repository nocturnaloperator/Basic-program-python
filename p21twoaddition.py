print("press 1 for addition")
print("press 2 for sub")
print("press 3 for multiplication")
print("press 4 for division")
choice=int(input("enter any number=> "))
if choice==1:
    number1=int(input("Enter number1 =>"))
    number2=int(input("enter number2 =>"))
    print("num1+num2 => ",number1+number2)
elif choice==2:
    number1 = int(input("Enter number1 =>"))
    number2 = int(input("enter number2 =>"))
    print("num1-num2=> ", number1-number2)
elif choice==3:
    number1 = int(input("Enter number1 =>"))
    number2 = int(input("enter number2 =>"))
    print("num2*num1=> ", number2*number1)
elif choice==4:
    number1 = int(input("Enter number1 =>"))
    number2 = int(input("enter number2 =>"))
    print("num1/num2=> ", number1/number2)
else: print("none")
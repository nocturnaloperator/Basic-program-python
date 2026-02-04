print("press + for addition")
print("press - for sub")
print("press m for multiplication")
print("press div for division")
choice=input("enter any number=> ")
if choice=="+":
    number1=int(input("Enter number1 =>"))
    number2=int(input("enter number2 =>"))
    print("num1+num2 => ",number1+number2)
elif choice=="-":
    number1 = int(input("Enter number1 =>"))
    number2 = int(input("enter number2 =>"))
    print("num1-num2=> ", number1-number2)
elif choice=="m":
    number1 = int(input("Enter number1 =>"))
    number2 = int(input("enter number2 =>"))
    print("num2*num1=> ", number2*number1)
elif choice=="div":
    number1 = int(input("Enter number1 =>"))
    number2 = int(input("enter number2 =>"))
    print("num1/num2=> ", number1/number2)
else: print("none")
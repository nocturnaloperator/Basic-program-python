salary=int(input("enter salary=>"))
gender=input("Enter gender =>")

if gender=="female":
    print("good salary")
else:
    if salary>15000:
        print("good salary for male")
    else:
        print("poor salary")
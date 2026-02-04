ch=input("Enter any character=>")
if ch.isupper():
    print(ch.lower())
elif ch.islower():
    print(ch.upper())
else:
    print(ch)
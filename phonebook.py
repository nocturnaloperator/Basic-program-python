people = [
    {"Name": "Harsh", "Number":"992654320"},
    {"Name":"Aditya", "Number":"626252150"},
    {"Name": "Unnati", "Number":"8871250455"},
]

name = input("Name :")

for person in people:
    if person["Name"]==name:
        Number = person["Number"]
        print(f"Found:{Number}")
        break
    else:
        print("not found")

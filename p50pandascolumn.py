import pandas as pd
data = {
"Name": ["Anu", "Rahul", "Kiran"],
"Marks": [78, 85, 90]
}
df = pd.DataFrame(data)
print("Marks Column:")
print(df["Marks"])
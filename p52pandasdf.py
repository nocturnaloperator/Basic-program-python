import pandas as pd
data = {
"Name": ["Amit", "Riya", "Sohan"],
"Marks": [45, 75, 85]
}
df = pd.DataFrame(data)
print("Students with Marks > 60:")
print(df[df["Marks"] > 60])
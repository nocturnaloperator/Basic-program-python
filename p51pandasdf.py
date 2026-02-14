import pandas as pd
data = {
"Name": ["A", "B", "C"],
"Marks": [60, 70, 80]
}
df = pd.DataFrame(data)
df["Result"] = ["Pass", "Pass", "Pass"]
print(df)
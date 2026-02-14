import pandas as pd
data = {
"ID": [1, 2, 3],
"Salary": [20000, 25000, 30000]
}
df = pd.DataFrame(data)
print("Data Types:")
print(df.dtypes)
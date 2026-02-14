import pandas as pd
data = {
"Numbers": [10, 20, 30, 40, 50]
}
df = pd.DataFrame(data)
print("First Rows:")
print(df.head(2))
print("\nLast Rows:")
print(df.tail(1))
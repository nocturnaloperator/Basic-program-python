import pandas as pd
data = {
"Marks": [55, 65, 75, 85, 95]
}
df = pd.DataFrame(data)
print("Statistical Summary:")
print(df.describe())
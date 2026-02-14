import pandas as pd
data = [[1, "Pen"], [2, "Pencil"], [3, "Book"]]
df = pd.DataFrame(data, columns=["ID", "Item"])
print("Item List:")
print(df)
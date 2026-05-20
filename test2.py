import pandas as pd
file_path = "test2.xlsx"
df = pd.read_excel(file_path)
print(df.head())
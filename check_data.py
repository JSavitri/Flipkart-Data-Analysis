import pandas as pd

df = pd.read_csv("data/flipkart_data.csv")

print(df.head(10))
print(df.columns)
print(df.info())
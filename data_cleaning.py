import pandas as pd
import os

os.makedirs("data", exist_ok=True)

df = pd.read_csv("data/flipkart_data.csv")

print("Original rows:", len(df))
print(df.head())

# STEP 1: Keep only rows where Name is not empty
df = df[df["Name"].notna()]

# STEP 2: Convert everything safely (no aggressive filtering)
df["Name"] = df["Name"].astype(str)

df["Price"] = df["Price"].astype(str).str.replace("₹", "", regex=False).str.replace(",", "", regex=False)
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")

# STEP 3: Only remove rows where BOTH Price and Name are missing
df = df[~((df["Name"] == "nan") & (df["Price"].isna()))]

# STEP 4: Fill values AFTER cleaning
df["Price"] = df["Price"].fillna(df["Price"].median())
df["Rating"] = df["Rating"].fillna(0)

print("Cleaned rows:", len(df))

df.to_excel("data/flipkart_clean_data.xlsx", index=False)

print("Cleaning Completed ✔")
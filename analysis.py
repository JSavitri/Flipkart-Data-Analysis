import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("data/flipkart_clean_data.xlsx")

print("Dataset loaded:", len(df), "rows")

if len(df) == 0:
    print("No data available for analysis ❌")
    exit()

print("\nTop 5 Expensive Products:")
print(df.sort_values("Price", ascending=False).head(5))

print("\nAverage Price:", df["Price"].mean())

# Price distribution
plt.figure()
plt.hist(df["Price"], bins=8)
plt.title("Flipkart Price Distribution")
plt.xlabel("Price")
plt.ylabel("Count")
plt.show()

print("Analysis Completed ✔")
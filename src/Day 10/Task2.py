import pandas as pd

# Sample dataset (Price has $ symbol, Date is object)
data = {
    "Price": ["$120.50", "$99.99", "$150.00", "$75.25"],
    "Date": ["2024-01-05", "2024-01-10", "2024-02-01", "2024-02-05"]
}

df = pd.DataFrame(data)

# STEP 1 — Check initial data types
print("Data types BEFORE conversion:")
print(df.dtypes)

# STEP 2 — Remove $ symbol and convert Price to float
df["Price"] = df["Price"].str.replace("$", "", regex=False).astype(float)

# STEP 3 — Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# STEP 4 — Check data types after conversion
print("\nData types AFTER conversion:")
print(df.dtypes)

# Example mathematical operations
print("\nAverage Price:", df["Price"].mean())
print("Date range:", df["Date"].min(), "to", df["Date"].max())
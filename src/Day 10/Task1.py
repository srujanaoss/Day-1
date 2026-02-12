import pandas as pd

# 1️⃣ Load your dataset
df = pd.read_csv("customer_orders.csv")   # change file name

# Shape BEFORE cleaning
print("Shape before cleaning:", df.shape)

# 2️⃣ Report missing values
print("\nMissing values report:")
print(df.isna().sum())

# 3️⃣ Fill missing NUMERIC values with MEDIAN
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

for col in numeric_cols:
    median_value = df[col].median()
    df[col] = df[col].fillna(median_value)

# 4️⃣ Remove duplicate rows (across ALL columns)
df = df.drop_duplicates()

# Shape AFTER cleaning
print("\nShape after cleaning:", df.shape)

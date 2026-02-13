import pandas as pd

# Example dataset
data = {
    "Location": [" New York", "new york", "NEW YORK ", " chicago ", "chicago"]
}

df = pd.DataFrame(data)

# 1️⃣ Check unique values BEFORE cleaning
print("Unique locations BEFORE cleaning:")
print(df["Location"].unique())

# 2️⃣ Remove leading/trailing spaces
df["Location"] = df["Location"].str.strip()

# 3️⃣ Standardize casing (use ONE)
# Option A: lowercase (best for grouping)
df["Location"] = df["Location"].str.lower()

# Option B: title case (for display)
# df["Location"] = df["Location"].str.title()

# 4️⃣ Verify AFTER cleaning
print("\nUnique locations AFTER cleaning:")
print(df["Location"].unique())

# Final cleaned column
print("\nFinal Location column:")
print(df["Location"])

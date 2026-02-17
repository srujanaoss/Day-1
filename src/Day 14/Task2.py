import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# -----------------------------
# Step 1: Create Sample Dataset
# -----------------------------
data = {
    'Age': [22, 25, 47, 52, 46, 56, 23, 40, 60, 36],
    'Salary': [25000, 30000, 120000, 150000, 110000, 170000, 28000, 90000, 200000, 75000]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# -----------------------------
# Step 2: Standardization
# (Mean = 0, Std = 1)
# -----------------------------
scaler_standard = StandardScaler()
df_standardized = pd.DataFrame(
    scaler_standard.fit_transform(df),
    columns=df.columns
)

print("\nStandardized Data:")
print(df_standardized)

# -----------------------------
# Step 3: Normalization
# (Range 0 to 1)
# -----------------------------
scaler_minmax = MinMaxScaler()
df_normalized = pd.DataFrame(
    scaler_minmax.fit_transform(df),
    columns=df.columns
)

print("\nNormalized Data:")
print(df_normalized)

# -----------------------------
# Step 4: Histogram Comparison (Salary)
# -----------------------------

plt.figure(figsize=(12, 4))

# Original Salary
plt.subplot(1, 3, 1)
plt.hist(df['Salary'], bins=5)
plt.title("Original Salary")

# Standardized Salary
plt.subplot(1, 3, 2)
plt.hist(df_standardized['Salary'], bins=5)
plt.title("Standardized Salary")

# Normalized Salary
plt.subplot(1, 3, 3)
plt.hist(df_normalized['Salary'], bins=5)
plt.title("Normalized Salary")

plt.tight_layout()
plt.show()

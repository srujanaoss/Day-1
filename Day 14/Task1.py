import pandas as pd
from sklearn.preprocessing import LabelEncoder

# -----------------------------
# Step 1: Create Sample Dataset
# -----------------------------
data = {
    'Transmission': ['Automatic', 'Manual', 'Automatic', 'Manual', 'Automatic'],
    'Color': ['Red', 'Blue', 'Green', 'Blue', 'Red']
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# -----------------------------
# Step 2: Label Encoding (Binary)
# -----------------------------
le = LabelEncoder()
df['Transmission'] = le.fit_transform(df['Transmission'])

print("\nAfter Label Encoding (Transmission):")
print(df)

# -----------------------------
# Step 3: One-Hot Encoding (Nominal)
# -----------------------------
df = pd.get_dummies(df, columns=['Color'], drop_first=True)

print("\nAfter One-Hot Encoding (Color with drop_first=True):")
print(df)


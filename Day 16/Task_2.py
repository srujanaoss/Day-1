import pandas as pd
import numpy as np

# Create sample dataset (normally distributed heights)
np.random.seed(42)
data = pd.DataFrame({
    "Height": np.random.normal(loc=170, scale=10, size=1000)
})

# Step 1️⃣ Calculate Mean and Standard Deviation
mu = data["Height"].mean()
sigma = data["Height"].std()

print("Mean (μ):", round(mu,2))
print("Standard Deviation (σ):", round(sigma,2))

# Step 2️⃣ Create Z-score column
data["z_score"] = (data["Height"] - mu) / sigma

# Step 3️⃣ Identify Outliers (|Z| > 3)
outliers = data[np.abs(data["z_score"]) > 3]

print("\nNumber of Outliers:", len(outliers))
print(outliers.head())

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 11:30:56 2026

@author: K M SRUJANA
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

# Step 1️⃣ Create a heavily right-skewed dataset (like income)
population = np.random.exponential(scale=50000, size=10000)

# Visualize original skewed data
plt.figure()
sns.histplot(population, kde=True)
plt.title("Original Population (Right-Skewed)")
plt.show()


# Step 2️⃣ Take 1000 samples of size 30 and compute their means
sample_means = []

for i in range(1000):
    sample = np.random.choice(population, size=30)
    sample_means.append(np.mean(sample))

sample_means = pd.Series(sample_means)


# Step 3️⃣ Plot histogram of sample means
plt.figure()
sns.histplot(sample_means, kde=True)
plt.title("Distribution of Sample Means (n=30)")
plt.show()

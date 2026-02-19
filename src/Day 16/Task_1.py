import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set random seed
np.random.seed(42)

# 1️⃣ Normal Distribution (Human Heights)
heights = np.random.normal(loc=170, scale=10, size=1000)

# 2️⃣ Right-Skewed Distribution (Income)
income = np.random.exponential(scale=50000, size=1000)

# 3️⃣ Left-Skewed Distribution (Easy Exam Scores)
scores = 100 - np.random.exponential(scale=10, size=1000)

# Convert to Pandas Series
heights = pd.Series(heights)
income = pd.Series(income)
scores = pd.Series(scores)

# Function to plot and compare
def analyze_data(data, title):
    mean = data.mean()
    median = data.median()
    
    print(f"\n{title}")
    print("Mean:", round(mean,2))
    print("Median:", round(median,2))
    
    plt.figure()
    sns.histplot(data, kde=True)
    plt.axvline(mean)
    plt.axvline(median)
    plt.title(title)
    plt.show()

# Analyze all three
analyze_data(heights, "Normal Distribution (Heights)")
analyze_data(income, "Right-Skewed Distribution (Income)")
analyze_data(scores, "Left-Skewed Distribution (Scores)")

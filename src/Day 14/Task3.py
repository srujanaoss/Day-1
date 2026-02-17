import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

# -----------------------------------
# Step 1: Create Non-Linear Dataset
# -----------------------------------
# y = x^2 + noise  (clearly curved)

np.random.seed(42)
X = np.linspace(-5, 5, 100).reshape(-1, 1)
y = X**2 + np.random.normal(0, 2, size=X.shape)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# -----------------------------------
# Step 2: Linear Regression (Original)
# -----------------------------------
lin_model = LinearRegression()
lin_model.fit(X_train, y_train)

y_pred_linear = lin_model.predict(X_test)
r2_linear = r2_score(y_test, y_pred_linear)

print("R² score (Simple Linear Regression):", r2_linear)

# -----------------------------------
# Step 3: Polynomial Features (degree=2)
# -----------------------------------
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# Train Linear Regression on Polynomial Features
poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)

y_pred_poly = poly_model.predict(X_test_poly)
r2_poly = r2_score(y_test, y_pred_poly)

print("R² score (Polynomial Regression degree=2):", r2_poly)

# -----------------------------------
# Step 4: Visualization
# -----------------------------------
plt.scatter(X, y, label="Actual Data")

# Linear line
plt.plot(X_test, y_pred_linear, label="Linear Fit")

# Polynomial curve
plt.scatter(X_test, y_pred_poly, label="Polynomial Fit")

plt.legend()
plt.title("Linear vs Polynomial Regression")
plt.show()

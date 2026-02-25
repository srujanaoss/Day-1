"""
plots.py
A reusable plotting module using Matplotlib and Seaborn.

Usage:
    from plots import plot_line, plot_bar, plot_histogram, plot_scatter

Each function returns a Matplotlib figure,
so you can display or save it:
    fig = plot_line(...)
    fig.savefig("output.png")
"""

import matplotlib.pyplot as plt
import seaborn as sns

# Set a default style
sns.set(style="whitegrid")


def plot_line(x, y, title="Line Plot", xlabel="X", ylabel="Y"):
    """Creates a line plot."""
    fig, ax = plt.subplots()
    ax.plot(x, y, marker="o")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    return fig


def plot_bar(categories, values, title="Bar Plot", xlabel="Category", ylabel="Value"):
    """Creates a bar chart."""
    fig, ax = plt.subplots()
    ax.bar(categories, values, color="skyblue")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    return fig


def plot_histogram(data, bins=10, title="Histogram", xlabel="Value", ylabel="Frequency"):
    """Creates a histogram."""
    fig, ax = plt.subplots()
    ax.hist(data, bins=bins, color="lightgreen", edgecolor="black")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    return fig


def plot_scatter(x, y, title="Scatter Plot", xlabel="X", ylabel="Y"):
    """Creates a scatter plot."""
    fig, ax = plt.subplots()
    ax.scatter(x, y, color="purple")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    return fig


if __name__ == "__main__":
    # Example usage
    import numpy as np

    x = np.arange(10)
    y = np.random.randn(10)

    plot_line(x, y, title="Example Line Plot").show()
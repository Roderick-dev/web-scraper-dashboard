import pandas as pd
import matplotlib.pyplot as plt

# Load scraped data
df = pd.read_csv("website_data.csv")

# Add a column: title length
df["title_length"] = df["title"].apply(len)

# Plot histogram of title lengths
plt.figure(figsize=(10,6))
df["title_length"].plot(kind="hist", bins=10, color="skyblue", edgecolor="black")
plt.title("Distribution of Link Title Lengths")
plt.xlabel("Title Length")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("dashboard_chart.png")
plt.show()

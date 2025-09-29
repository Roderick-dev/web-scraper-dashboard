# dashboard.py
import pandas as pd
import matplotlib.pyplot as plt

# Load scraped data
df = pd.read_csv("website_data.csv")

# 1. Show counts of element types (links, headings, images)
type_counts = df["type"].value_counts()

plt.figure(figsize=(6,4))
type_counts.plot(kind="bar", rot=0, color=["skyblue", "lightgreen", "salmon"])
plt.title("Extracted Element Types")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("element_types.png")
plt.show()

# 2. Show distribution of text lengths
df["text_length"] = df["text"].astype(str).apply(len)

plt.figure(figsize=(6,4))
df["text_length"].plot(kind="hist", bins=10, color="purple", alpha=0.7)
plt.title("Distribution of Text Lengths")
plt.xlabel("Text Length (characters)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("text_length_distribution.png")
plt.show()

print("✅ Dashboard charts generated: element_types.png, text_length_distribution.png")

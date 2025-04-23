import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the enriched dataset
df = pd.read_csv("data/anime_dataset_enriched.csv")

# Top 5 most watched anime per country
top_anime_by_country = (
    df.groupby('Country')
    .apply(lambda x: x.nlargest(5, 'Estimated Watch Count'))
    .reset_index(drop=True)
)

# Plot
plt.figure(figsize=(15, 8))
sns.barplot(
    data=top_anime_by_country,
    x='Country',
    y='Estimated Watch Count',
    hue='Name'
)

plt.title("Top 5 Most Watched Anime per Country (2024)")
plt.xticks(rotation=45)
plt.ylabel("Watch Count")
plt.tight_layout()
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.savefig("output/top_anime_by_country.png")
plt.show()

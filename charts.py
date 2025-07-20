import matplotlib.pyplot as plt
from collections import Counter
import os

CHARTS_DIR = "charts"
os.makedirs(CHARTS_DIR, exist_ok=True)

def generate_charts(articles, sentiment_summary):
    # Pie Chart
    labels = list(sentiment_summary.keys())
    sizes = list(sentiment_summary.values())
    if sum(sizes) == 0:
        print("No sentiment data to plot.")
    else:
        plt.figure(figsize=(5, 5))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.title("Sentiment Distribution")
        plt.savefig(f"{CHARTS_DIR}/sentiment_pie.png")
        plt.close()

    # Timeline Chart
    dates = [a['date'] for a in articles]
    date_counts = Counter(dates)
    if date_counts:
        plt.figure(figsize=(8, 4))
        plt.plot(list(date_counts.keys()), list(date_counts.values()), marker='o')
        plt.xticks(rotation=45)
        plt.title("News Frequency Over Time")
        plt.tight_layout()
        plt.savefig(f"{CHARTS_DIR}/timeline.png")
        plt.close()
    else:
        print("No date data to plot timeline.")

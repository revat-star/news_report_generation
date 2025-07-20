from textblob import TextBlob

def analyze_sentiments(articles):
    sentiment_summary = {"positive": 0, "neutral": 0, "negative": 0}
    results = []
    for article in articles:
        text = article['title']
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        sentiment = "neutral"
        if polarity > 0.1:
            sentiment = "positive"
        elif polarity < -0.1:
            sentiment = "negative"
        sentiment_summary[sentiment] += 1
        results.append({"title": text, "sentiment": sentiment, "date": article['publishedAt']})
    return results, sentiment_summary
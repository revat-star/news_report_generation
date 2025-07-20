

#run this commands in cmd (windows button+r)
#cd news_report_generation
# python -m venv venv
# venv\Scripts\activate
#pip install flask requests beautifulsoup4 textblob matplotlib fpdf
# python -m textblob.download_corpora
# pip install feedparser
#python main.py



from news_scraper import fetch_news
from sentiment import analyze_sentiments
from charts import generate_charts
from report_generator import create_pdf_report

if __name__ == "__main__":
    start_date = "2025-07-01"
    end_date = "2025-07-20"
    category = "latest"  # supports any news category: politics, sports, business, etc.

    print("Fetching news...")
    articles = fetch_news(start_date, end_date, category)
    print(f"Fetched {len(articles)} articles.")

    print("Analyzing sentiment...")
    analyzed_articles, sentiment_summary = analyze_sentiments(articles)

    print("Generating charts...")
    generate_charts(analyzed_articles, sentiment_summary)

    print("Creating PDF report...")
    pdf_path = create_pdf_report(analyzed_articles, sentiment_summary)
    print(f"Report saved to: {pdf_path}")

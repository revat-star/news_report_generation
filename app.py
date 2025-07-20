from flask import Flask, request, send_file, jsonify
from news_scraper import fetch_news
from sentiment import analyze_sentiments
from charts import generate_charts
from report_generator import create_pdf_report
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "PDF News Report API is Running"

@app.route('/generate_report', methods=['POST'])
def generate_report():
    try:
        data = request.json
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        category = data.get('category', 'general')

        articles = fetch_news(start_date, end_date, category)
        analyzed_articles, sentiment_summary = analyze_sentiments(articles)
        generate_charts(analyzed_articles, sentiment_summary)
        pdf_path = create_pdf_report(analyzed_articles, sentiment_summary)
        return send_file(pdf_path, as_attachment=True)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

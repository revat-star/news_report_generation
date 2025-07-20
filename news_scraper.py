import requests
from bs4 import BeautifulSoup
from datetime import datetime

def fetch_news(start_date, end_date, category="telugu"):
    url = "https://www.eenadu.net/home"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    articles = []
    for item in soup.select(".lead-news-box .lead-news-title a")[:10]:
        title = item.get_text(strip=True)
        link = item['href']
        if not link.startswith("http"):
            link = "https://www.eenadu.net" + link
        articles.append({
            "title": title,
            "publishedAt": datetime.today().strftime("%Y-%m-%d"),
            "link": link
        })

    for item in soup.select(".col-12.col-sm-6.col-md-4.col-lg-3 .item-title a")[:10]:
        title = item.get_text(strip=True)
        link = item['href']
        if not link.startswith("http"):
            link = "https://www.eenadu.net" + link
        articles.append({
            "title": title,
            "publishedAt": datetime.today().strftime("%Y-%m-%d"),
            "link": link
        })

    
    return articles
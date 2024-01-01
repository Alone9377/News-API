import requests
from datetime import datetime

# Replace 'YOUR_API_KEY' with your actual NewsAPI key
NEWS_API_KEY = "1d3a0eefa97b499d8fbc4ee93eeb40b7"

# URL for fetching top headliness
NEWS_API_URL = f"https://newsapi.org/v2/everything?q="

# Get today's date in YYYY-MM-DD format
today = datetime.now().strftime('%2023-%08-%19')

# Parameters for the request
params = {
    'apiKey': NEWS_API_KEY,
    'country': 'india',
    'from': today,
    'to': today
}

response = requests.get(NEWS_API_URL, params=params)

if response.status_code == 200:
    news_data = response.json()

    if news_data['status'] == 'ok':
        articles = news_data['articles']

        for idx, article in enumerate(articles, start=1):
            title = article['title']
            source = article['source']['name']
            description = article['description']

            print(f"Article {idx}:\nSource: {source}\nTitle: {title}\nDescription: {description}\n")
    else:
        print("NewsAPI response status is not 'ok'")
else:
    print("Failed to retrieve news")

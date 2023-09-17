from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.find_all(name="span", class_='titleline')
article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
article_text = []
article_link = []

for article in articles:
    # To get hold of the title anchor tag
    a_tag = article.find('a')
    article_text.append(a_tag.text)
    a_link = a_tag.get("href")
    article_link.append(a_link)

    # To get the upvote count
    # vote = int(votes.find(name="span", class_="score").text.split()[0])

    # print(f"{a_tag.text} - {a_link}")

highest_upvote = article_upvote.index(max(article_upvote))
# print(highest_upvote)

print(article_text[highest_upvote])
print(article_link[highest_upvote])
print(article_upvote[highest_upvote])

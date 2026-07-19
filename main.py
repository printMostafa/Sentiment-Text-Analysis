import nltk
from textblob import TextBlob
# from newspaper import Article 


# url = 'https://en.wikipedia.org/wiki/Bad_News_(band)       '
# article = Article(url)
# article.download()
# article.parse()
# article.nlp()

#text = article.summary

with open('Text.txt', 'r') as file:
    text = file.read()
print(text)
blob = TextBlob(text)
sentiment = blob.sentiment.polarity
print(sentiment)
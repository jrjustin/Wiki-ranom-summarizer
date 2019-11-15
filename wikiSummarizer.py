import bs4 as bs
import urllib.request
import re
import nltk
import heapq
import os
import wikipedia

# global variables

# PRINTING - output file: output.txt
output = open("output.txt", "w")


def summary():
    # take in article
    scraped_data = urllib.request.urlopen(wikipedia.random(1))
    article = scraped_data.read()

    parsed_article = bs.BeautifulSoup(article, 'html.parser')

    paragraphs = parsed_article.find_all('p')

    article_text = ""

    for p in paragraphs:
        article_text += p.text

    # precessing
    # Removing Square Brackets and Extra Spaces
    article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
    article_text = re.sub(r'\s+', ' ', article_text)
    # Removing special characters and digits
    formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text)
    formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

    # text to sentences
    sentence_list = nltk.sent_tokenize(article_text)

    # Find Weighted Frequency of Occurrence
    stopwords = nltk.corpus.stopwords.words('english')

    # use weightedAverage(dict) & findMaxFreq(dict)
    word_frequencies = {}
    for word in nltk.word_tokenize(formatted_article_text):
        if word not in stopwords:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1

    maximum_frequncy = max(word_frequencies.values())

    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word] / maximum_frequncy)

    # Calculating Sentence Scores
    sentence_scores = {}
    for sent in sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]

    # Summary
    summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)
    summary = '\n'.join(summary_sentences)
    output.write(url + "\n" + summary + "\n\n")


summary()
output.close()
j
import pickle
import os
from bs4 import BeautifulSoup
import requests
import nltk
from nltk.corpus import stopwords
# from statsmodels.sandbox.regression.sympy_diff import df
from urls import urls

nltk_stopwords = set(stopwords.words('english'))


def save_tokenized_test(tokenized_txt, filename):
    with open(filename, 'wb') as f:
        pickle.dump(tokenized_txt, f)

def crawl(start_url):
    response = requests.get(start_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a', href=True)

    urls = [link['href'] for link in links]
    urls = [url for url in urls if not url.startswith('http')]
    urls = [start_url + url if not url.startswith('/') else start_url[:-1] + url for url in urls]

    return urls[:5]


if not os.path.exists('tokenized_text_pickle.pkl'):

    text_content = []
    # for website in urls:
    #     try:
    #         links = crawl(website)
    #         for link in links:
    #             response = requests.get(link)
    #             soup = BeautifulSoup(response.text, 'html.parser')
    #             text_content.append(soup.get_text())
    #     except requests.exceptions.RequestException as e:
    #         print(f"Error fetching content from {website}: {e}")

    for website in urls:
        links = crawl(website)
        response = requests.get(website)
        soup = BeautifulSoup(response.text, 'html.parser')
        text_content.append(soup.get_text())

    stop_word = ['the', 'is', 'and', 'hi', 'there', ':', 'am', 'i', 'click', 'here', 'a', 'go', 'it', 'that', 'for']

    nltk_stopwords.update(stop_word)

    filtered_text_content = []
    for content in text_content:
        tokens = content.lower().split()
        filtered_tokens = [token for token in tokens if token.lower() not in nltk_stopwords]
        filtered_text_content.append(" ".join(filtered_tokens))
    tokenize = []
    for content in filtered_text_content:
        tokens = content.lower().split()
        one_word_tokens = [token for token in tokens if token.lower() not in nltk_stopwords]
        two_word_tokens = [" ".join(tokens[i:i + 2]) for i in range(len(tokens) - 1)]
        two_word_tokens = [token for token in two_word_tokens if token.lower() not in nltk_stopwords]
        tokenize.append([one_word_tokens, two_word_tokens])
    print(tokenize)
    save_tokenized_test(tokenize, 'tokenized_text_pickle.pkl')

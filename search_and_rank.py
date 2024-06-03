import pickle
from flask import Flask, render_template, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx


def create_tfidf_vectors(corpus):
    tfidf = TfidfVectorizer()
    tfidf_vectors = tfidf.fit_transform(corpus)
    return tfidf, tfidf_vectors


def calculate_cosine_similarity(query_vectors, tfidf_vectors):
    return cosine_similarity(query_vectors, tfidf_vectors)


def create_graph(urls, similarities):
    G = nx.DiGraph()
    for i, link in enumerate(urls):
        G.add_node(link)
        for j, sim in enumerate(similarities[0]):
            if sim > 0 and i != j:
                G.add_edge(link, urls[j], weight=sim)
    return G


def calculate_pagerank(G):
    return nx.pagerank(G)


def search(query, urls):
    tokenized_text = load_tokenized_text('tokenized_text_pickle.pkl')
    corpus = [' '.join([' '.join(token_list) for token_list in doc_tokens]) for doc_tokens in tokenized_text]
    tfidf, tfidf_vectors = create_tfidf_vectors(corpus)
    query_vectors = tfidf.transform([query])
    similarity = calculate_cosine_similarity(query_vectors, tfidf_vectors)
    if all_zero(similarity[0]):
        return None
    G = create_graph(urls, similarity)
    pagerank = calculate_pagerank(G)
    rank_result = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)
    top_result = [x[0] for x in rank_result if x[1] >= 0.14]
    return top_result


def all_zero(I):
    for i in I:
        if i != 0:
            return False
    return True


def load_tokenized_text(filename):
    try:
        tokenized_text = pickle.load(open(filename, 'rb'))
        return tokenized_text
    except (FileNotFoundError, EOFError) as e:
        print(f"Error loading tokenized text: {e}")
        return None

import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import dataPreprocessing.data_processing as dp

def query_processing(query):
    text = dp.tokenize_text(query)
    text = dp.stemming(text)
    text = dp.remove_stopwords(text)
    text = dp.cleaning(text)
    text = dp.remove_punctuation(text)
    text = dp.tokenize_text(text)
    text = dp.remove_numbers_with_text(text)
    text = dp.lemmatization(text)
    return text

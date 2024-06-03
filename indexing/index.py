import os
import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import scipy.sparse
import re

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import DataSet.save_files as sf
import dataPreprocessing.data_processing as dp



def build_inverted_index(documents,ds_f_inverted_index_file,ds_f_vectorizer_file, ds_f_tfidf_matrix_file,ds_f_data_indexing_for_test):
    print("hi")
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    terms = vectorizer.get_feature_names_out().tolist() 
    inverted_index = {}
    for i, doc in enumerate(documents):
      doc_terms = set(doc.lower().split())
  # Split the document into terms
      for term in doc_terms:
          inverted_index[term] = set()  # Initialize a set for the term if it doesn't exist
          inverted_index[term].add(i) 
        

    inverted_index_file = ds_f_inverted_index_file
    vectorizer_file = ds_f_vectorizer_file
    tfidf_matrix_file = ds_f_tfidf_matrix_file
    sf.save_indexed_corpus(inverted_index,vectorizer,tfidf_matrix,ds_f_data_indexing_for_test)
    sf.save_file_pickle(inverted_index, inverted_index_file)
    sf.save_file_pickle(vectorizer, vectorizer_file)
    scipy.sparse.save_npz(tfidf_matrix_file, tfidf_matrix)




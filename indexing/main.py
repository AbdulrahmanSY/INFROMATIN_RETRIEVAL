import os
import sys
import pandas as pd

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import DataSet.save_files as sf
import attrbute as a
import indexing.index as ind
from DataSet.save_files import save_file_pickle, load_file_pickle
import csv



collection=load_file_pickle(a.ds_f_data_processing)
collection_2=load_file_pickle(a.ds_s_data_processing)


ind.build_inverted_index(collection['clean_doc'],a.ds_f_inverted_index_file,a.ds_f_vectorizer_file, a.ds_f_tfidf_matrix_file)
ind.build_inverted_index(collection_2['clean_doc'],a.ds_s_inverted_index_file,a.ds_s_vectorizer_file, a.ds_s_tfidf_matrix_file)




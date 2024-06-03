from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import DataSet.save_files as sf
import attrbute as a
import dataPreprocessing.query_proccessing as qp
import scipy.sparse




def Search_of_query(query,name_data_set):
    if name_data_set=='lotte':
        collection=sf.load_file_pickle(a.ds_f_data_processing)
        vectorizer=sf.load_file_pickle(a.ds_f_vectorizer_file)
        tfidf_matrix =scipy.sparse.load_npz(a.ds_f_tfidf_matrix_file)
        inverted_index=sf.load_file_pickle(a.ds_f_inverted_index_file)
        clean_query=qp.query_processing(query)
        query_vector=vectorizer.transform([clean_query])
        query_terms = set(clean_query.lower().split())

        matching_docs = []

        for term in query_terms:
         if term in inverted_index:
            matching_docs.extend(inverted_index[term])

        if not matching_docs:
         print("No documents found for the given query.")
         return []
        
        tfidf_matrix_documents = tfidf_matrix[matching_docs]
        # tfidf_vector_query = vectorizer.transform([query])
        cosine_similarities = cosine_similarity(query_vector, tfidf_matrix_documents)
        documents_list = list(matching_docs)
        print("documents_list")
        print(documents_list)

        document_ranking = np.argsort(cosine_similarities)[::-1][:10]
        document_ranking = document_ranking[0].tolist() 

        results = []
        for  doc_index in enumerate(document_ranking):
            doc_id=documents_list[doc_index]
            doc = collection['doc'].iloc[doc_id]
            results.append(doc)

        return results
    elif name_data_set=="clinic":
          collection=sf.load_file_pickle(a.ds_s_data_processing)
          vectorizer=sf.load_file_pickle(a.ds_s_vectorizer_file)
          tfidf_matrix =scipy.sparse.load_npz(a.ds_s_tfidf_matrix_file)
          inverted_index=sf.load_file_pickle(a.ds_s_inverted_index_file)
          clean_query=qp.query_processing(query)
          query_vector=vectorizer.transform([clean_query])
          query_terms = set(clean_query.lower().split())

          matching_docs = []  

          for term in query_terms:
           if term in inverted_index:
            matching_docs.extend(inverted_index[term])

          if not matching_docs:
            print("No documents found for the given query.")
            return []
        
          tfidf_matrix_documents = tfidf_matrix[matching_docs]
        # tfidf_vector_query = vectorizer.transform([query])
          cosine_similarities = cosine_similarity(query_vector, tfidf_matrix_documents)
          documents_list = list(matching_docs)
          document_ranking = np.argsort(cosine_similarities)[::-1][:10]
          document_ranking = document_ranking[0].tolist() 

          results = []
          for  doc_index in enumerate(document_ranking):
            doc_id=documents_list[doc_index]
            doc = collection['doc'].iloc[doc_id]
            results.append(doc)

          return results



query="Making sense of principal component analysis, eigenvectors & eigenvalues"
Search_of_query(query,"lotte")


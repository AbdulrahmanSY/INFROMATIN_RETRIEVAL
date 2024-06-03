from dataPreprocessing import query_proccessing as qp
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import attrbute as at
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import DataSet.save_files as sf
import scipy.sparse
import attrbute as a



# النتائج تبعنا
def relevant(queries,filename,nameDataSet):
    results = get_relevant_results(queries,nameDataSet)
    # for query_id, document_numbers in results:
    #     print(f"Query ID: {query_id}")
    #     print("Documents:")
    #     for doc_number in document_numbers:
    #         print(f"('{doc_number}')")
    results_dict = {}
    for query_id, document_numbers in results:
        results_dict[query_id] = [(doc_number) for doc_number in document_numbers]

    sf.save_file_pickle(results_dict,filename)

    return results_dict


def get_relevant_results(queries,nameDataSet):
    results = []
    for query_id, query_text in zip(queries['query_id'], queries['clean_query']):
        # clean_query=qp.query_prossing(query_text)
        document_numbers =match_query_cosine(query_text,nameDataSet,10)
        results.append((query_id, document_numbers))
    return results


def match_query_cosine(query, nameDataSet,k):
      if nameDataSet=="lotte":
        # collection=sf.load_file_pickle(a.ds_f_data_processing)
        vectorizer=sf.load_file_pickle(a.ds_f_vectorizer_file)
        tfidf_matrix =scipy.sparse.load_npz(a.ds_f_tfidf_matrix_file)
        inverted_index=sf.load_file_pickle(a.ds_f_inverted_index_file)
      elif nameDataSet=="clinic":
        # collection=sf.load_file_pickle(a.ds_f_data_processing)
        vectorizer=sf.load_file_pickle(a.ds_s_vectorizer_file)
        tfidf_matrix =scipy.sparse.load_npz(a.ds_s_tfidf_matrix_file)
        inverted_index=sf.load_file_pickle(a.ds_s_inverted_index_file)
      query_vector=vectorizer.transform([query])
      query_terms = set(query.lower().split())


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

      document_ranking = np.argsort(cosine_similarities)[::-1][:k]
      document_ranking = document_ranking[0].tolist() 

      results = []
      for  index,doc_index in enumerate(document_ranking):
            doc_id=documents_list[doc_index]
            # doc = collection['doc'].iloc[doc_id]
            results.append(doc_id)

    #     # return results
    # for rank, doc_index in enumerate(document_ranking):
    #     print("Rank", rank + 1, ": Document", documents_list[doc_index], "with cosine similarity score",
    #           cosine_similarities[doc_index])
    #     # print(data.loc[documents_list[doc_index], 'clean_doc'])
    #     results_doc.append(documents_list[doc_index])
      print(results)
      return results

      
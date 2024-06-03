from dataPreprocessing import query_proccessing as qp
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import attrbute as at
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import DataSet.save_files as sf


# النتائج تبعنا
def relevant(queries,filename):
    results = get_relevant_results(queries)
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


def get_relevant_results(queries):
    results = []
    for query_id, query_text in zip(queries['query_id'], queries['clean_query']):
        # clean_query=qp.query_prossing(query_text)
        document_numbers =match_query_cosine(query_text,10)
        results.append((query_id, document_numbers))
    return results



def match_query_cosine(query, k=10):
    inverted_index, vectorizer, data_matrix=sf.load_indexed_corpus(at.ds_f_data_indexing)
    terms = vectorizer.get_feature_names_out()
    query_terms = vectorizer.transform([query]).nonzero()[1]

    documents = set()
    for term_index in query_terms:
        term = terms[term_index]
        if term in inverted_index:
            documents.update(inverted_index[term])

    if not documents:
        print("No documents found for the given query.")
        return []

    tfidf_matrix_documents = data_matrix[list(documents)]
    tfidf_vector_query = vectorizer.transform([query])
    cosine_similarities = cosine_similarity(tfidf_vector_query, tfidf_matrix_documents)
    documents_list = list(documents)
    document_ranking = np.argsort(cosine_similarities)[::-1][:k]
    results_doc = []
    

    for rank, doc_index in enumerate(document_ranking):
        print("Rank", rank + 1, ": Document", documents_list[doc_index], "with cosine similarity score",
              cosine_similarities[doc_index])
        # print(data.loc[documents_list[doc_index], 'clean_doc'])
        results_doc.append(documents_list[doc_index])
   
    return results_doc
         
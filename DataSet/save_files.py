import json
import pickle



def save_json_file(retrieval_results,file_name):
 # حفظ المتغير retrieval_results في ملف باستخدام JSON
  # with open('retrieval_results.json', 'w', encoding='utf-8') as file:
  with open(f'{file_name}.json', 'w', encoding='utf-8') as file:
    json.dump(retrieval_results, file)


def load_json_file(file_name):
  # استرجاع المتغير من الملف
  with open(f'{file_name}.json', 'r', encoding='utf-8') as file:
    retrieved_results = json.load(file)
  return retrieved_results




def save_indexed_corpus(indexed_corpus_matrix, vectorizer, corpus_documents, filename):
    print("yes")
    with open(filename, 'wb') as file:
        pickle.dump((indexed_corpus_matrix, vectorizer, corpus_documents), file)

def load_indexed_corpus(filename):
    print("yessssssssssss")
    with open(filename, 'rb') as file:
        indexed_corpus_matrix, vectorizer, corpus_documents = pickle.load(file)
    return indexed_corpus_matrix, vectorizer, corpus_documents


def save_file_pickle(data, filename):
    print("yes")
    with open(filename, 'wb') as file:
        pickle.dump((data), file)

def load_file_pickle(filename):
    print("yessssssssssss")
    with open(filename, 'rb') as file:
        data = pickle.load(file)
    return data


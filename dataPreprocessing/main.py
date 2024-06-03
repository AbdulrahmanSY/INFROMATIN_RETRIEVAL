import os
import sys
import query_proccessing as qp
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from DataSet.read_dataSet import read_query, read_data, read_qrels, read_jsonl
from DataSet.save_files import save_file_pickle, load_file_pickle
import data_processing as dp
from path import ds_f_doc_path, ds_f_qrels_path, ds_f_queries_path, ds_s_doc_path, ds_s_qrels_path, ds_s_queries_path
import attrbute as a

def query_processing(fileQueryName,ds_f_queries_path):
    queries = read_query(ds_f_queries_path)
    queries_data_proceing = []
    for _, row in queries.iterrows():
        query_id = row['query_id']
        query = row['query']
        q = qp.query_processing(query)
        print(query_id)
        print('Query:', q)
        # queries_data_proceing.append(q)
        queries.loc[queries['query_id'] == query_id, 'clean_query'] = q 
    save_file_pickle(queries, fileQueryName)
    return queries



def data_processing(fileDataName,ds_f_doc_path):
    ds_f_doc_data = read_data(ds_f_doc_path)
    print(ds_f_doc_data.columns)
    ds_f_doc_data_clean = dp.data_prossing(ds_f_doc_data)
    save_file_pickle(ds_f_doc_data_clean,fileDataName)
    return ds_f_doc_data_clean


def process_qrels(file_path):
    qrels = read_qrels(read_jsonl(file_path))
    # queries = read_query(ds_f_queries_path)
    return qrels


ds_f_data = ds_f_doc_path
ds_f_queries = ds_f_queries_path
ds_f_quels = ds_f_qrels_path

ds_s_data = ds_s_doc_path
ds_s_queries = ds_s_queries_path
ds_s_quels = ds_s_qrels_path


data_processing(a.ds_f_data_1,ds_f_data)

print('query done')







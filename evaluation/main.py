
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import DataSet.save_files as sf
import dataPreprocessing.main as m
import attrbute as a
import path as p
import relevant as rel 
import retrieval as ret
import evaluation.MAP as eval


# # Load the TF-IDF matrix from the saved NPZ file
# loaded_tfidf_matrix = scipy.sparse.load_npz(tfidf_matrix_file)


qieries=m.query_processing(a.ds_f_query,p.ds_f_queries_path)


def get_results(name_data_set):
    if name_data_set=="lotte":
        queries=sf.load_file_pickle(a.ds_f_query)
        print(queries['query_id'])
        qrels=m.process_qrels(p.ds_f_qrels_path)
        rel.relevant(queries,a.ds_f_relevant,name_data_set)
        ret.retrieval(queries,qrels)
    elif name_data_set=="clinic":
        queries=sf.load_file_pickle(a.ds_s_query)
        print(queries['query_id'])
        qrels=m.process_qrels(p.ds_s_qrels_path)
        rel.relevant(queries,a.ds_s_relevant,name_data_set)
        ret.retrieval(queries,qrels)


get_results("lotte")
get_results("clinic")




def calculat_map(name_dataset):
    if name_dataset=="lotte":
      relevant_results=sf.load_file_pickle(a.ds_f_relevant)
      retrieval_results=sf.load_file_pickle(a.ds_f_retrieval)

      map_score = eval.mean_average_precision(retrieval_results,relevant_results)
      print("Mean Average Precision (MAP):", map_score)

    elif name_dataset=="clinic":
        relevant_results=sf.load_file_pickle(a.ds_f_relevant)
        retrieval_results=sf.load_file_pickle(a.ds_f_retrieval)
        map_score = eval.mean_average_precision(retrieval_results,relevant_results)
        print("Mean Average Precision (MAP):", map_score)



calculat_map("lotte")
calculat_map("clinic")

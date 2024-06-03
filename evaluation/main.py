
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import DataSet.save_files as sf
import dataPreprocessing.main as m
import attrbute as a
import path as p
import relevant as rel 
import retrieval as ret
import evaluation as eval




qieries=m.query_processing(a.ds_f_query,p.ds_f_queries_path)
queries=sf.load_file_pickle(a.ds_f_query)
qrels=m.process_qrels(p.ds_f_qrels_path)

rel.relevant(queries,a.ds_f_relevant)
ret.retrieval(queries,qrels)

relevant_results=sf.load_file_pickle(a.ds_f_relevant)
retrieval_results=sf.load_file_pickle(a.ds_f_retrieval)


eval.mean_average_precision(retrieval_results,relevant_results)



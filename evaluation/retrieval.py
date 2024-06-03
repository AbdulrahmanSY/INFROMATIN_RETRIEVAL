
import DataSet.save_files as sf
import attrbute as at



# التائج الصجيجة
def retrieval(queries,qrels):
    retrieval_results = {}
    for _, query in queries.iterrows():
        query_id = query['query_id']
        relevant_qrels = qrels[qrels['qid'] == query_id]
        for _, qrel in relevant_qrels.iterrows():
           retrieval_results[query_id] = qrel['answer_pids']

    sf.save_file_pickle(retrieval_results,at.ds_f_retrieval)
    return retrieval_results

# هاد مشان كل كويري لحال ولا كلن سوا  ؟  وايمت يستخدم

def calculate_recall_precision(query,relevant_docs,retrieved_docs): 

    y_true = [1 if doc_id in relevant_docs else 0 for doc_id in retrieved_docs]
    true_positives = sum(y_true)
    recall_at_10 = true_positives / len(relevant_docs) if relevant_docs else 0
    precision_at_10 = true_positives / 10
    print(f"Query: {query}, Recall@10: {recall_at_10}")
    print(f"Query : {query}, Precision@10: {precision_at_10}")    
    return recall_at_10
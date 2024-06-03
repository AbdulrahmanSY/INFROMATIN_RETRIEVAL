
def average_precision(retrieved_docs, relevant_docs):
    precision_sum = 0.0
    relevant_count = 0
    for i, doc in enumerate(retrieved_docs):
        if doc in relevant_docs:
            relevant_count += 1
            precision_sum += relevant_count / (i + 1)
    if relevant_count == 0:
        return 0.0
    return precision_sum / len(relevant_docs)


def mean_average_precision(retrieval_results, relevant_docs_per_query):
    print(retrieval_results)
    print(relevant_docs_per_query)
    total_precision = 0.0
    num_queries = len(retrieval_results)
    for query_id, retrieved_docs in retrieval_results.items():
        relevant_docs = relevant_docs_per_query.get(query_id, set())
        total_precision += average_precision(retrieved_docs, relevant_docs)
    return total_precision / num_queries







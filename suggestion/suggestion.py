import csv
from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def fetch_suggestion(query, csv_file, encoding='utf-8'):
    # Load the queries from the CSV file
    queries = []
    with open(csv_file, 'r', encoding=encoding) as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            queries.append(row[0])

    # Create a TF-IDF matrix from the queries
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(queries)

    # Calculate the cosine similarity between the input query and all other queries
    query_vector = vectorizer.transform([query])
    similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()

    # Sort the queries by similarity score
    sorted_indices = similarities.argsort()[::-1]
    similar_queries = [queries[i] for i in sorted_indices]
    for i, similar_query in enumerate(similar_queries):
        if i < 10:
            print(similar_query)
        else:
            break
    similar_queries = [queries[i] for i in sorted_indices]

    # Return the first 5 similar queries
    return [q.split('\t')[1] for q in similar_queries[:5]]

# Example usage
# input_query = "between"
# csv_file = "C:\\Users\\hp\\.ir_datasets\\lotte\\science\\dev\\questions.forum.tsv"
# fech_suggestion = fech_suggestion(input_query, csv_file)
#
# print("Similar queries:")
# print(fech_suggestion)

import csv

import pandas as pd
import jsonlines


def read_data(dataSet_path):
    collection_dataFrame = pd.read_csv(dataSet_path, sep='\t', header=None)
    collection_dataFrame.columns = ['doc_id', 'doc']

    print(collection_dataFrame.shape)

    print(collection_dataFrame.head())

    return collection_dataFrame


def read_qrels(data):
    queries_dataFrame = pd.DataFrame(data)

    # print(queries_dataFrame.shape)

    # print(queries_dataFrame.head())

    return queries_dataFrame


def read_data(file_path):
    data = []
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)

        # Skip the header row
        next(reader)

        # Iterate through the rows and append to the data list
        for row in reader:
            doc_id, doc_content = row
            data.append({'doc_id': doc_id, 'doc': doc_content})

    # Create a pandas DataFrame from the data list
    df = pd.DataFrame(data)
    return df

def read_query(path):
    queries_dataFrame = pd.read_csv(path, sep='\t', header=None)
    queries_dataFrame.columns = ['query_id', 'query']

    # print(queries_dataFrame.shape)

    # print(queries_dataFrame.head())

    return queries_dataFrame

def read_data_f(path):
    queries_dataFrame = pd.read_csv(path, sep='\t', header=None)
    queries_dataFrame.columns = ['doc_id', 'doc']
    return queries_dataFrame


def read_jsonl(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = jsonlines.Reader(file)
        for line in reader:
            data.append(line)
    return data

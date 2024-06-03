import ir_datasets
dataset = ir_datasets.load("lotte/science/dev/forum")
for query in dataset.queries_iter():
    query # namedtuple<query_id, text>
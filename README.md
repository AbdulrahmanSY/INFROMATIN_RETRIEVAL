 In this project, we have two basic processes. The first is the offlin process, which consists of the following modules: 
 data process, indeexing, and dataSet for downloading, which has functions for dealing with files. Also, the path module, 
 which contains links to the dataset, and the attrubute file, which contains constants.
 We also have an evaluation module to verify the validity of the information extracted from dataset with the original information, a qrels file, 
 where Recall, Precision, MAP, MRR, and a matching module are calculated to match the results and arrange them.
 The second process, online, consists of a matching module. In this module, the query is processed and the results are given.
 This module is used online and offline, where when the user requests A query returns results based on the UI.
 We also have one, Crawling and query suggestion, for additional requests for the project.


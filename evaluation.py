# Add your import statements here

from util import *
import math
import numpy as np

class Evaluation():

	def queryPrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of precision of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The precision value as a number between 0 and 1
		"""

		precision = -1
		retrieved_docs = query_doc_IDs_ordered[:k]
		n_relevant_docs = 0
		
		for doc in retrieved_docs:
			if doc in true_doc_IDs:
				n_relevant_docs+=1
		
		precision = n_relevant_docs/k

		return precision


	def meanPrecision(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of precision of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean precision value as a number between 0 and 1
		"""

		meanPrecision = -1
		total_Precision = 0
		count = 0
		for i in query_ids:
			true_doc_IDs = []
			flag = 0
			for dic in qrels:
				if(int(dic["query_num"]) == i):
					flag = 1
					true_doc_IDs.append(int(dic["id"]))
				elif(flag == 1):
					break     
			total_Precision = total_Precision + self.queryPrecision(doc_IDs_ordered[count] , i , true_doc_IDs, k)
			count = count+1
		meanPrecision = total_Precision/count

		return meanPrecision

	
	def queryRecall(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of recall of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The recall value as a number between 0 and 1
		"""

		recall = -1
		retrieved_docs = query_doc_IDs_ordered[:k]
		n_relevant_docs = 0
		for doc in retrieved_docs:
			if doc in  true_doc_IDs:
				n_relevant_docs += 1
		recall = n_relevant_docs/len(true_doc_IDs)

		return recall


	def meanRecall(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of recall of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean recall value as a number between 0 and 1
		"""

		meanRecall = -1
		total_Recall = 0
		count = 0
		for i in query_ids:
			true_doc_IDs = []
			flag = 0
			for dic in qrels:
				if(int(dic["query_num"]) == i):
					flag = 1
					true_doc_IDs.append(int(dic["id"]))
				elif(flag == 1):
					break
			total_Recall = total_Recall + self.queryRecall(doc_IDs_ordered[count] , i , true_doc_IDs, k)
			count = count+1
		meanRecall = total_Recall/count

		return meanRecall


	def queryFscore(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of fscore of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The fscore value as a number between 0 and 1
		"""

		fscore = -1
		precision = self.queryPrecision(query_doc_IDs_ordered , query_id , true_doc_IDs, k)
		recall = self.queryRecall(query_doc_IDs_ordered , query_id , true_doc_IDs, k)
		fscore = (2*precision*recall)/(precision + recall + 0.00001)

		return fscore


	def meanFscore(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of fscore of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value
		
		Returns
		-------
		float
			The mean fscore value as a number between 0 and 1
		"""

		meanFscore = -1
		total_Fscore = 0
		count = 0
		for i in query_ids:
			true_doc_IDs = []
			flag = 0
			for dic in qrels:
				if(int(dic["query_num"]) == i):
					flag = 1
					true_doc_IDs.append(int(dic["id"]))
				elif(flag == 1):
					break
			total_Fscore = total_Fscore + self.queryFscore(doc_IDs_ordered[count] , i , true_doc_IDs, k)
			count = count+1
		meanFscore = total_Fscore/count

		return meanFscore
	

	def queryNDCG(self, query_doc_IDs_ordered, query_id, qrels, k):
		"""
		Computation of nDCG of the Information Retrieval System
		at given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The nDCG value as a number between 0 and 1
		"""

		nDCG = -1
		DCG = 0
		iDCG = 0
		retrieved_docs = query_doc_IDs_ordered[:k]
		true_doc_IDs = dict()
		flag = 0
		
		for dic in qrels:
			if(int(dic["query_num"]) == query_id):
				flag = 1
				true_doc_IDs[int(dic["id"])] = 5 - dic['position']
			elif(flag == 1):
				break
		ideal_order = sorted(retrieved_docs, key = lambda x: true_doc_IDs[x] if x in true_doc_IDs else 0, reverse = True)
		for i in range(1,k+1):
			if retrieved_docs[i-1] in true_doc_IDs:
				DCG += true_doc_IDs[retrieved_docs[i-1]]/math.log2(i+1)
			if ideal_order[i-1] in true_doc_IDs:
				iDCG += true_doc_IDs[ideal_order[i-1]]/math.log2(i+1)
		nDCG = DCG/iDCG

		return nDCG


	def meanNDCG(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of nDCG of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean nDCG value as a number between 0 and 1
		"""

		meanNDCG = -1
		total_NDCG = 0
		count = 0
		for i in query_ids:
			total_NDCG = total_NDCG + self.queryNDCG(doc_IDs_ordered[count] , i , qrels, k)
			count = count+1
		meanNDCG = total_NDCG/count

		return meanNDCG


	def queryAveragePrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of average precision of the Information Retrieval System
		at a given value of k for a single query (the average of precision@i
		values for i such that the ith document is truly relevant)

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The average precision value as a number between 0 and 1
		"""

		avgPrecision = -1
		retrieved_docs = query_doc_IDs_ordered[:k]
		Total_Precision = 0
		count = 0
		for i in range(len(retrieved_docs)):
			doc = retrieved_docs[i]
			if doc in true_doc_IDs:
				count += 1
				Total_Precision += self.queryPrecision(query_doc_IDs_ordered, query_id, true_doc_IDs, i+1)       
		avgPrecision = Total_Precision/count

		return avgPrecision


	def meanAveragePrecision(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of MAP of the Information Retrieval System
		at given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The MAP value as a number between 0 and 1
		"""

		meanAveragePrecision = -1
		total_AveragePrecision = 0
		count = 0
		for i in query_ids:
			true_doc_IDs = []
			flag = 0
			for dic in qrels:
				if(int(dic["query_num"]) == i):
					flag = 1
					true_doc_IDs.append(int(dic["id"]))
				elif(flag == 1):
					break
			total_AveragePrecision = total_AveragePrecision + self.queryAveragePrecision(doc_IDs_ordered[count] , i , true_doc_IDs, k)
			count = count+1
		meanAveragePrecision = total_AveragePrecision/count

		return meanAveragePrecision
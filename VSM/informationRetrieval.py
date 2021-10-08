# Add your import statements here

from util import *
import math
import numpy as np


class InformationRetrieval():

	def __init__(self):
		self.docIDs = None
		self.matrix = None
		self.basis_words = None
		self.idfs = None

	def buildIndex(self, docs, docIDs):
		"""
		Builds the document index in terms of the document
		IDs and stores it in the 'index' class variable

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is
			a document and each sub-sub-list is a sentence of the document
		arg2 : list
			A list of integers denoting IDs of the documents
		Returns
		-------
		None
		"""
		index = dict()
		n_docs = len(docs)
		for i in range(n_docs):
			docID = i
			for sentences in docs[i]:
				for word in sentences:
					if word not in index:
						index[word] = list()
					index[word].append(docID)   

		basis_words = list(index.keys())
		matrix = dict()
		idfs = list()

		for i in range(n_docs):
			vector = list()
			for j in range(len(basis_words)):
				tf = index[basis_words[j]].count(i)
				if i == 0:
					idf = math.log2(n_docs/len(set(index[basis_words[j]])))
					idfs.append(idf)
				vector.append(tf*idfs[j])
			matrix[i] = vector

		self.docIDs = docIDs
		self.matrix = matrix
		self.basis_words = basis_words
		self.idfs = idfs

	def rank(self, queries):
		"""
		Rank the documents according to relevance for each query

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is a query and
			each sub-sub-list is a sentence of the query
		

		Returns
		-------
		list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		"""
       
		doc_IDs_ordered = list()
		for query in queries:
			vector = list()
			retrieved_docs = dict()
						
			for i in range(len(self.basis_words)):
				tf = 0
				for query_sentence in query:
					tf += query_sentence.count(self.basis_words[i])
				vector.append(tf*self.idfs[i])
								 
			for key in self.matrix:
				cosine = sum(np.multiply(self.matrix[key],vector))/(np.sqrt(sum(np.square(self.matrix[key]))*sum(np.square(vector))) + 0.0001)
				retrieved_docs[self.docIDs[key]] = cosine        
			doc_IDs_ordered.append(sorted(retrieved_docs,reverse=True,key = lambda x: retrieved_docs[x]))
            
		return doc_IDs_ordered

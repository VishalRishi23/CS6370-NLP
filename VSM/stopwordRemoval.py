from util import *
from nltk.corpus import stopwords  
from nltk.tokenize import word_tokenize
# Add your import statements here




class StopwordRemoval():

	def fromList(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence with stopwords removed
		"""

		stopwordRemovedText = []

		stop_words = set(stopwords.words('english'))

		for i in range(len(text)):
			temp_list = [w for w in text[i] if not w in stop_words]
			stopwordRemovedText.append(temp_list)

		return stopwordRemovedText

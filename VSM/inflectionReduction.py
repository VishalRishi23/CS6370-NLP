from util import *
from nltk.stem import WordNetLemmatizer
# Add your import statements here




class InflectionReduction:

	def reduce(self, text):
		"""
		Stemming/Lemmatization

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of
			stemmed/lemmatized tokens representing a sentence
		"""

		reducedText = []

		for i in range(len(text)):
			temp_lemma = [WordNetLemmatizer().lemmatize(w) for w in text[i]]
			reducedText.append(temp_lemma)
		
		return reducedText



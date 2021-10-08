from util import *
from nltk.tokenize import TreebankWordTokenizer
# Add your import statements here




class Tokenization():

	def naive(self, text):
		"""
		Tokenization using a Naive Approach

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

		tokenizedText = []

		for j in range(len(text)):
			text(j).replace("\""," ")
			text(j).replace(", "," ")
			text(j).replace("(", " ").replace(")", " ").replace("{"," ").replace("}"," ").replace("["," ").replace("]"," ")
			text(j).replace("; "," ").replace(": "," ")
			text(j).replace("- "," ")
			naive_tok = text.split()
			tokenizedText.append(naive_tok)

		return tokenizedText



	def pennTreeBank(self, text):
		"""
		Tokenization using the Penn Tree Bank Tokenizer

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

		tokenizedText = []

		for i in range(len(text)):
			temp_token = TreebankWordTokenizer().tokenize(text[i])
			tokenizedText.append(temp_token)

		return tokenizedText

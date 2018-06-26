import csv
import pandas as pd
import numpy as np
from Vset import Vset

def readcsv(filename):
	df = pd.read_csv(filename, header=None, dtype= str)
	b = len(df.loc[0,0])
	n = len(df.columns)
	L = len(df.index)
	k = n - L
	return b, df, n, k, L

class BCJR:		
	def __init__(self, filename):
		print("I am BCJR!")
		self.b, self.H, self.n, self.k, self.L = readcsv(filename)
		self.V = []
		self.E = []

	def build(self):
		print("Building...")
		self.V = []
		self.E = []

		for i in range(self.n + 1):
			self.V.append(Vset(self.L))

		self.V[0].add_vertex(self.L)
		#for i in range(self.n + 1):

		
	def get_len(self):
		return self.n

	def get_dim(self):
		return self.k

	def get_bit(self):
		return self.b
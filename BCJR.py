import csv
import pandas as pd
import numpy as np
from Vset import Vset
from Eset import Eset

def readcsv(filename):
	df = pd.read_csv(filename, header=None, dtype= str)
	b = len(df.loc[0,0])
	n = len(df.columns)
	L = len(df.index)
	k = n - L
	df = pd.read_csv(filename, header=None)
	return df, b, n, k, L

class BCJR:		
	def __init__(self, filename):
		print("I am BCJR!")
		self.H, self.b, self.n, self.k, self.L = readcsv(filename)
		self.V = []
		self.E = []

	def build(self):
		print("Building...")
		self.V = []
		self.E = []

		for i in range(self.n + 1):
			self.V.append(Vset(self.L))

		self.V[0].set_vertex([0, 0])
		for i in range(self.n):
			self.E.append(Eset(self.L))

		for i in range(self.n):
			self.build_edge_layer(i)
			self.build_vertex_layer(i)

	def build_edge_layer(self, layer):
		print("Building edge",layer)
		print("Vertex number in layer", layer,":", self.V[layer].get_vertice_number())
		for vindex in range(self.V[layer].get_vertice_number()):
			if self.V[layer].vertice[vindex] == 0:
				continue
			for symbol in range (2**self.b):
				self.E[layer].add_edge(self.V[layer].vertice[vindex], symbol, self.H[layer].values)
				self.E[layer].print_Eset()
				print("Number of edge:", self.E[layer].get_edgeNum())

	def build_vertex_layer(self, layer):
		print("Building vertex", layer)
		for edge in self.E[layer].edgelist:
			self.V[layer + 1].set_vertex(edge.end.val)
		
	def get_len(self):
		return self.n

	def get_dim(self):
		return self.k

	def get_bit(self):
		return self.b
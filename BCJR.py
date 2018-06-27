import csv
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from Vset import Vset
from Eset import Eset
from Vertex import Vertex

def readcsv(filename):
	df = pd.read_csv(filename, header=None, dtype= str)
	b = len(df.loc[0,0])
	n = len(df.columns)
	L = len(df.index)
	k = n - L
	df = pd.read_csv(filename, header=None)
	return df, b, n, k, L

def val_to_index(val):
	index = 0
	multiple = 1
	for i in reversed(range(len(val))):
		index = index + multiple * val[i]
		multiple *=2
	return index

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

		self.V[0].set_vertex(val_to_index([0, 0]), [0, 0])
		for i in range(self.n):
			self.E.append(Eset(self.L))

		for i in range(self.n):
			self.build_edge_layer(i)
			self.build_vertex_layer(i)

	def build_edge_layer(self, layer):
		print("### Building edge",layer)
		for vindex in range(self.V[layer].get_vertice_number()):
			if self.V[layer].vertice[vindex] == 0:
				continue
			for symbol in range (2**self.b):
				self.E[layer].add_edge(self.V[layer].vertice[vindex], symbol, self.H[layer].values)

		print("Number of edge:", self.E[layer].get_edgeNum())
		self.E[layer].print_Eset()

	def build_vertex_layer(self, layer):
		print("### Building vertex", layer)
		for edge in self.E[layer].edgelist:
			self.V[layer + 1].set_vertex(val_to_index(edge.end.val), edge.end.val)

		self.V[layer+1].print_Vset()
		
	def get_len(self):
		return self.n

	def get_dim(self):
		return self.k

	def get_bit(self):
		return self.b

	def plot_section(self, i, j):
		pos = {}
		edge_list = []
		# Draw vertex
		for layer in range(i,j+1):
			vLayer = self.V[layer]
			for v in range(vLayer.get_vertice_number()):
				if(type(vLayer.vertice[v]) == Vertex):
					index = val_to_index(vLayer.vertice[v].val)
					vName = str(layer) + str(index)
					pos[vName] = (layer, index)

		# Draw edge
		for layer in range(i,j):
			eLayer = self.E[layer]
			for e in eLayer.edgelist:
				start_index = val_to_index(e.start.val)
				end_index = val_to_index(e.end.val)
				edge_list.append((str(layer) + str(start_index), str(layer+1) + str(end_index)))

		print("pos dictionary:", pos)
		print("Edge list:", edge_list)
		#pos={'0':(0,0),'1':(1,1),'2':(1,2),'3':(1,0)} 
		G = nx.Graph()
		#edge_list = [('0','2'),('0','1'),('0','3')]
		G.add_edges_from(edge_list)
		#pos = nx.spring_layout(G) # positions for all nodes
		#G.add_edge(1,2)
		#nx.draw(G)
		nx.draw_networkx_nodes(G,pos,node_size=700,)
		nx.draw_networkx_edges(G,pos, width=6)
		plt.show()


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

		# Build V subset
		for i in range(self.n + 1):
			self.V.append(Vset(self.L))

		# Initialize the vertex in first layer as 0
		self.V[0].set_vertex([0 for i in range(self.L)])
		for i in range(self.n): # Build E subset
			self.E.append(Eset(self.L))

		for i in range(self.n):
			self.build_edge_layer(i)
			self.build_vertex_layer(i)

		# Only keep vertice 0 at the last layer
		self.V[-1].keep_vertex([0])


		for i in reversed(range(self.n)):
			self.E[i].remove_edge(self.V[i+1])
			self.V[i].remove_vertex(self.E[i])

		#self.E[-1].print_Eset()


	def build_edge_layer(self, layer):
		print("### Building edge",layer)
		for vindex in range(self.V[layer].get_vertice_number()):
			if self.V[layer].vertice[vindex] == 0:
				continue
			#print("H values:", self.H[layer].values)
			for symbol in range (2**self.b):
				self.E[layer].add_edge(self.V[layer].vertice[vindex], symbol, self.H[layer].values)

		#print("Number of edge:", self.E[layer].get_edgeNum())
		#self.E[layer].print_Eset()

	def build_vertex_layer(self, layer):
		print("### Building vertex", layer)
		for edge in self.E[layer].edgelist:
			self.V[layer + 1].set_vertex(edge.end.val)

		#self.V[layer+1].print_Vset()
		
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
					index = vLayer.vertice[v].val_to_index()
					vName = str(layer) + str(index)
					pos[vName] = (layer, index)

		# Draw edge
		for layer in range(i,j):
			eLayer = self.E[layer]
			for e in eLayer.edgelist:
				start_index = e.start.val_to_index()
				end_index = e.end.val_to_index()
				edge_list.append((str(layer) + str(start_index), str(layer+1) + str(end_index)))

		print("pos dictionary:", pos)
		print("Edge list:", edge_list)
		G = nx.Graph()
		G.add_edges_from(edge_list)
		#pos = nx.spring_layout(G) # positions for all nodes
		#G.add_edge(1,2)
		#nx.draw(G)
		nx.draw_networkx_nodes(G,pos,node_size=200)
		nx.draw_networkx_edges(G,pos, width=3)
		plt.show()


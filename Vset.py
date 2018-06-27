import numpy as np
from Vertex import Vertex

class Vset:
	def __init__(self, L):
		self.L = L
		self.vertice = [0 for i in range(2**L)]

	def add_vertex(self, val):
		newV = Vertex(self.L)
		self.vertice.append(newV)

	def set_vertex(self, val):
		tmpV = Vertex(self.L, val)
		index = tmpV.val_to_index()
		self.vertice[index] = Vertex(self.L, val)

	def keep_vertex(self, index_list):
		for i in range(len(self.vertice)):
			if i not in index_list:
				self.vertice[i] = 0

	def remove_vertex(self, eset):
		vertex_val_list = []
		for e in eset.edgelist:
			vertex_val_list.append(e.start.val_to_index())
		#print(vertex_val_list)
		self.keep_vertex(vertex_val_list)

	def get_vertice_number(self):
		return len(self.vertice)

	def print_Vset(self):
		for i in range(len(self.vertice)):
			if(type(self.vertice[i]) == Vertex):
				print(self.vertice[i].val)
			else:
				print("No vertex.")

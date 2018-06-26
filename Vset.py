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
		index = self.val_to_index(val)
		self.vertice[index] = Vertex(self.L, val)

	def val_to_index(self, val):
		index = 0
		multiple = 1
		for i in reversed(range(len(val))):
			index = index + multiple * val[i]
			multiple *=2
		return index

	def get_vertice_number(self):
		return len(self.vertice)

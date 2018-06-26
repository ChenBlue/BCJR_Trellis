import numpy as np
from Vertex import Vertex

class Vset:
	def __init__(self, L):
		self.L = L
		self.vertice = []

	def add_vertex(self, val):
		newV = Vertex(self.L)
		self.vertice.append(newV)

	def get_vertice_number(self):
		return len(self.vertice)

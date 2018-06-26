import numpy as np

class Vertex:
	def __init__(self, L):
		self.L = L
		self.val = np.zeros(self.L)
		print("In Vertex value:", self.val)

V = Vertex(3)
import numpy as np

class Vertex:
	#def __init__(self, L):
	#	self.L = L
	#	self.val = np.zeros(self.L)
		#print("In Vertex value:", self.val)

	def __init__(self, L, val):
		self.L = L
		self.val = val

	def add(self, addValues):
		self.val = (self.val + addValues) % 2


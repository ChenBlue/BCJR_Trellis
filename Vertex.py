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
		#print("val:", self.L, self.val)
		self.val = (self.val + addValues) % 2

	def val_to_index(self):
		index = 0
		multiple = 1
		for i in reversed(range(len(self.val))):
			index = index + multiple * self.val[i]
			multiple *=2
		return index



import numpy as np
from operator import add

class Vertex:
	#def __init__(self, L):
	#	self.L = L
	#	self.val = np.zeros(self.L)
		#print("In Vertex value:", self.val)

	def __init__(self, L, b, val):
		self.L = L
		self.b = b
		self.val = val

	def add(self, addValues):
		#print("val:", self.L, self.val)
		#sum = list(map(add, self.val, addValues))
		#self.val = np.mod(np.asarray(sum), 2).tolist()
		#self.val = (self.val + addValues) % (2**self.b)
		#tmpVal = addValues
		#print(type(addValues[0]), type(self.val[0]))
		self.val = np.bitwise_xor(self.val, addValues)

	#def 

	def val_to_index(self):
		index = 0
		multiple = 1
		for i in reversed(range(len(self.val))):
			index = index + multiple * self.val[i]
			multiple *= (2**self.b)
		return index



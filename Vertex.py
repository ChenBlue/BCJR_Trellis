import numpy as np
from operator import add

class Vertex:
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

	def multiply(self, array, scalar):
		result = np.zeros(len(array), dtype=int)
		for i in range(len(array)):
			result[i] = self.element_mul(array[i], scalar)

		#print("Result of multiplication:", result)
		return result

	def element_mul(self, a, b):
		binA = self.dec2bin(a)
		binB = self.dec2bin(b)

		x = self.bin_mul(a, binB)
		prim_poly = self.prim_poly(self.b)
		prim_poly_dec = self.bin2dec(prim_poly)
		prim_deg = len(prim_poly)
		#print(x, a, b, prim_poly, prim_poly_dec, prim_deg)

		deg = len(bin(x)[2:])
		while deg > self.b:
			Q = prim_poly_dec * (2**(deg - prim_deg))
			x = x ^ Q
			deg = len(bin(x)[2:])

		#print("Result of multiplication:", x)
		return x

	def bin_mul(self, decA, binB):
		result = 0
		for i in range(len(binB)):
			if binB[i] == 1:
				 result = result ^ (decA << (len(binB)-i-1))

		#print("Result of bin_mul:", result)
		return result

	def dec2bin(self, dec):
		binstr = bin(dec)[2:]
		bin_length = len(binstr)
		binnum = np.zeros(bin_length, dtype=int)
		for i in range(bin_length):
			binnum[i] = int(binstr[i])

		#print("Decimal:", dec, "Binary number:", binnum)
		return binnum

	def val_to_index(self):
		index = 0
		multiple = 1
		for i in reversed(range(len(self.val))):
			index = index + multiple * self.val[i]
			multiple *= (2**self.b)
		return index

	def bin2dec(self, bin):
		dec = 0
		mul = 1
		for i in reversed(range(len(bin))):
			dec = dec + mul * bin[i]
			mul *= 2
		return dec 

	def prim_poly(self, b):
		if b == 1:
			return np.array([0, 1])
		elif b == 2:
			return np.array([1, 1, 1])
		elif b == 3:
			return np.array([1, 0, 1, 1])
		elif b == 4:
			return np.array([1, 0, 0, 1, 1])
		elif b == 5:
			return np.array([1, 0, 0, 1, 0, 1])
		elif b == 6:
			return np.array([1, 0, 0, 0, 0, 1, 1])
		elif b == 7:
			return np.array([1, 0, 0, 0, 1, 0, 0, 1])
		elif b == 8:
			return np.array([1, 0, 0, 0, 1, 1, 1, 0, 1])
		elif b == 9:
			return np.array([1, 0, 0, 0, 0, 1, 0, 0, 0, 1])
		elif b == 10:
			return np.array([1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1])
		elif b == 11:
			return np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1])
		elif b == 12:
			return np.array([1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1])
		elif b == 13:
			return np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1])
		elif b == 14:
			return np.array([1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1])
		elif b == 15:
			return np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  1, 1])
		elif b == 16:
			return np.array([1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1])
		elif b == 17:
			return np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1])
		elif b == 18:
			return np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1])
		elif b == 19:
			return np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1])
		elif b == 20:
			return np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1])




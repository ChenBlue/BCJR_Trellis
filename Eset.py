from Edge import Edge

class Eset:
	def __init__(self, L):
		self.L = L
		self.edge = []

	def add_edge(self, symbol):
		newE = Edge(self.L, symbol)
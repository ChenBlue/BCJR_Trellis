from Vertex import Vertex

class Edge:
	def __init__(self, L, startV, symbol, endV):
		self.L = L
		self.start = startV
		self.symbol = symbol
		self.end = endV

	def print_edge(self):
		print(self.start.val, self.symbol, self.end.val)

#e = Edge(2,0)
#print(e.start.val)
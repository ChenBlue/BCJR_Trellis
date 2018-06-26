from Vertex import Vertex

class Edge:
	def __init__(self, L, symbol):
		print("I am edge", 2**L)
		self.start = Vertex(L)
		self.end = Vertex(L)
		self.symbol = symbol
		print("Edge symbol:", self.symbol)

#e = Edge(2,0)
#print(e.start.val)
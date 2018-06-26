from Edge import Edge
from Vertex import Vertex

class Eset:
	def __init__(self, L):
		self.L = L
		self.edgelist = []
		self.edgeNum = 0

	def add_edge(self, startV, symbol, addValues):
		tmpV = Vertex(self.L, startV.val)
		tmpV.add(addValues * symbol)
		newE = Edge(self.L, startV, symbol, tmpV)
		self.edgelist.append(newE)
		self.edgeNum = self.edgeNum + 1

	def get_edgeNum(self):
		return self.edgeNum

	def print_Eset(self):
		for e in self.edgelist:
			e.print_edge()
		
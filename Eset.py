from Edge import Edge
from Vertex import Vertex
from Vset import Vset

class Eset:
	def __init__(self, L, b):
		self.L = L
		self.b = b
		self.edgelist = []
		#self.edgeNum = 0

	def add_edge(self, startV, symbol, addValues):
		tmpV = Vertex(self.L, self.b, startV.val)
		tmpV.add(addValues * symbol)
		newE = Edge(self.L, startV, symbol, tmpV)
		self.edgelist.append(newE)

	def remove_edge(self, vset):
		vertex_val_list = []
		for v in vset.vertice:
			if(type(v) == Vertex):
				vertex_val_list.append(v.val_to_index())

		print(vertex_val_list)
		del_index_list = []
		for e in reversed(range(len(self.edgelist))):
			if self.edgelist[e].end.val_to_index() not in vertex_val_list:
				del self.edgelist[e]
				
	def get_edgeNum(self):
		return len(self.edgelist)

	def print_Eset(self):
		for e in self.edgelist:
			e.print_edge()
		
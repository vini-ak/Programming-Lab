''' O problema do código está na lista de adjacência para cada vértice.'''

class Vertice:
	''' Vertice de um grafo. '''
	def __init__(self, dado, visitado = False):
		self._vizinhos = []
		self._dado = dado
		self._visitado = visitado

	def getDado(self):
		return self._dado

	def setDado(self, novoDado):
		self._dado = novoDado

	def getVisitado(self):
		return self._visitado

	def setVisitado(self):
		self._visitado = True

	def getVizinhos(self):
		return self._vizinhos

	def addVizinho(self, vertice):
		''' Adicionando o nó para a lista de vizinhos. '''
		self.getVizinhos().append(vertice)


class Grafo:
	def __init__(self):
		self._vertices = []

	def getVertices(self):
		return self._vertices

	def addVertice(self, vertice):
		self.getVertices().append(vertice)


def dfs_recursiva(g, u, destino, passos = 1):
	u.setVisitado()
	for v in u.getVizinhos():
		print(v.getDado())
		if v is destino:
			return True
		if not v.getVisitado():
			if dfs_recursiva(grafo,v, destino, passos+1):
				return 'deu certo!'

numero_cidades, o, d = map(int, input().split())
grafo = Grafo()

for j in range(1, numero_cidades):
	cidade_a, cidade_b = map(int, input().split())
	
	if no_a not in grafo.getVertices():
		if cidade_a == o:
			origem = no_a
		if cidade_a == d:
			destino = no_a
		grafo.addVertice(no_a)

	no_b = Vertice(cidade_b)
	if no_b not in grafo.getVertices():
		if cidade_b == o:
			origem = no_b
		if cidade_b == d:
			destino = no_b
		grafo.addVertice(no_b)


	no_a.addVizinho(no_b)
	no_b.addVizinho(no_a)

for no in grafo.getVertices():
	print(no.getVizinhos())
print(dfs_recursiva(grafo, origem, destino))
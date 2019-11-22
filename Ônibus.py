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


def dfs_recursiva(grafo, origem, destino, passos = 0, minimo_passos = float('inf')):
	if origem is destino:	# Caso base: se o vértice que está sendo varrido é o final, será retornada a quantidade de passos até este vértice
		return passos

	origem.setVisitado()	# Marcando o nó para evitar que entre numa recursão infinita.
	passos += 1
	for vizinho in origem.getVizinhos():
		if not vizinho.getVisitado():
			s = dfs_recursiva(grafo, vizinho, destino, passos)	# Define o total de passos de um caminho
			if s < minimo_passos:	# Se este caminho é o menor
				minimo_passos = s

	return minimo_passos
			

numero_cidades, origem, destino = map(int, input().split())
grafo = Grafo()

for n in range(1, numero_cidades + 1):
	vertice = Vertice(n)
	grafo.addVertice(vertice)

for i in range(numero_cidades - 1):
	cidade_a, cidade_b = map(int, input().split())
	vertice_a = grafo.getVertices()[cidade_a - 1]	# Pegando o vértice da lista de vértices do grafo.
	vertice_b = grafo.getVertices()[cidade_b - 1]	# Pegando o vértice da lista de vértices do grafo.

	vertice_a.addVizinho(vertice_b)	# Colocando o vertice_b na lista de adjacencia de vertice_a
	vertice_b.addVizinho(vertice_a)	# Colocando o vertice_a na lista de adjacencia de vertice_b

	# Definindo o vértice de origem e de destino do grafo:
	if cidade_a == origem:
		vertice_origem = vertice_a
	elif cidade_a == destino:
		vertice_destino = vertice_a

	if cidade_b == origem:
		vertice_origem = vertice_b
	elif cidade_b == destino:
		vertice_destino = vertice_b

print(dfs_recursiva(grafo, vertice_origem, vertice_destino))
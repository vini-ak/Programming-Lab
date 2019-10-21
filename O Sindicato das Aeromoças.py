class Vertice:
	''' Criando uma classe que defina o vértice:
	métodos e atributos. '''
	def __init__(self, numero):
		self._numero = numero
		self._peso = float('inf')
		self._lista_adjacencia = []
		self._verificado = False

	def getNumero(cls):
		''' Retorna o número (identificação) de um vértice. '''
		return cls._numero

	def getPeso(cls):
		''' Retorna o peso de um vértice.'''
		return cls._peso

	def changePeso(cls, novoPeso):
		''' Altera o peso de um vértice.'''
		cls._peso = novoPeso

	def getListaAdjacencia(cls):
		''' Retorna a lista de adjacência de um vértice.'''
		return cls._lista_adjacencia

	def addListaAdjacencia(cls, vertice):
		''' Adiciona um vértice à lista de adjacência.'''
		cls._lista_adjacencia.append(vertice)


class Grafo:
	def __init__(self, vertices, inicio = None):
		self._vertices = vertices
		self._arestas = {}
		self.inicio = inicio

	def getVerticeByNumber(cls, numero):
		''' Retorna uma classe vértice. '''
		return cls._vertices[numero]
	
	def getVertices(cls):
		''' Retorna a lista de vértices de um grafo.'''
		return cls._vertices

	def getArestas(cls):
		''' Retorna todas as arestas de um grafo.'''
		return cls._arestas

	def addAresta(cls, a, b, distancia):
		''' Adiciona uma aresta ao grafo. '''
		if cls.getAresta(a, b) == None:
			# Definindo a aresta para a lista de arestas de cada vértice.

			# Verificando se os vértices já está incluso no 
			# dicionário de arestas.
			if a not in cls.getArestas().keys():
				cls.getArestas()[a] = {}
				cls.getArestas()[a][b] = distancia
			elif b not in cls.getArestas()[a].keys():
				cls.getArestas()[a][b] = distancia

			if b not in cls.getArestas().keys():
				cls.getArestas()[b] = {}
				cls.getArestas()[b][a] = distancia

			elif a not in cls.getArestas()[b].keys():
				cls.getArestas()[b][a] = distancia

			# Adicionando a na lista de adjacência de b
			a.addListaAdjacencia(b)
			# e b na lista de adjacẽncia de a.
			b.addListaAdjacencia(a)
		else:
			# Será verificada qual aresta é menor,
			# pois não faz sentido uma aeromoça tomar
			# o maior caminho entre duas cidades.
			aresta = cls.getAresta(a, b)

			if distancia < aresta:
				cls.getArestas()[a][b] = distancia
				cls.getArestas()[b][a] = distancia

	def getAresta(cls, a, b):
		''' Retorna o comprimento de uma aresta. '''
		try:
			return cls._arestas[a][b]
		except:
			return None


def dijkstra(grafo, inicio):
	# Definindo os pesos:
	for p in list(grafo.getVertices().values()):
		p.changePeso(float("inf"))

	# Definindo o peso inicial como 0.
	start = grafo.getVerticeByNumber(inicio)
	start.changePeso(0)

	vertices = list(grafo.getVertices().values())
	pesos = [0] * len(vertices)
	maior_peso = 0

	while vertices:
		lista_adjacencia = start.getListaAdjacencia()
		vertices.remove(start)

		for vertice in lista_adjacencia:
			peso_atual = vertice.getPeso()
			peso_temp = start.getPeso() + grafo.getAresta(start, vertice)

			if peso_atual == float("inf") or peso_temp < peso_atual:
				vertice.changePeso(peso_temp)
				pesos[vertice.getNumero()] = peso_temp

		if vertices:
			start = vertices[0]

	for h in pesos:
		if h > maior_peso:
			maior_peso = h
			
	return maior_peso


# ========================================================


# Informando o número de cidades e linhas aéreas.
cidades, linhas_aereas = [int(x) for x in input().split()]

vertices = {}

for cidade in range(cidades):
	vertice = Vertice(cidade)
	vertices[cidade] = vertice

# Criando um grafo a partir da lista de vértices
grafo = Grafo(vertices)

for i in range(linhas_aereas):
	cidade_a, cidade_b, distancia = [int(x) for x in input().split()]
	grafo.addAresta(grafo.getVerticeByNumber(cidade_a), grafo.getVerticeByNumber(cidade_b), distancia)

# Procurando o caminho máximo para uma aeromoça...
maximo = float("inf")
for j in range(cidades):
	a = dijkstra(grafo, j)
	if a < maximo:
		maximo = a

print(maximo)

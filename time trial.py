class Grafo:
	def __init__(self, vertices, inicio = 0, fim = 0):
		self._vertices = vertices
		self._arestas = {}
		self._inicio = inicio
		self._fim = fim

	# ======================= MÉTODOS PARA OS VÉRTICES =============================
	def setInicio(cls, inicio):
		cls._inicio = inicio
		cls.set_peso(inicio, 0)


	def getFim(cls):
		return cls._fim


	def setFim(cls, fim):
		cls._fim = fim


	def get_lista_adjacencia(cls, pesquisa):
		return cls._vertices[pesquisa]['lista_adjacencia']


	def get_peso(cls, pesquisa):
		return cls._vertices[pesquisa]['peso']


	def set_peso(cls, pesquisa, peso):
		cls._vertices[pesquisa]['peso'] = peso


# ============================ MÉTODOS PARA AS ARESTAS ====================================


	def setAresta(cls, a, b, distancia):
		cls._arestas[(a,b)] = distancia
		cls._arestas[(b,a)] = distancia


	def getDistancia(cls, a, b):
		return cls._arestas[(a, b)]


# ======================================= DIJKSTRA ========================================


	def dijkstra(cls, pesquisa, menor_caminho = 0):

		lista_adjacencia = cls.get_lista_adjacencia(pesquisa)

		# Peso do vértice que está sendo verificado
		predecessor = cls.get_peso(pesquisa)

		if cls.getFim() in lista_adjacencia:
			# O peso de um vértice é dado pela soma do peso do seu antecessor
			# com a distância entre estes vértices.
			
			distancia = cls.getDistancia(pesquisa, cls.getFim())

			peso = predecessor + distancia

			if peso < menor_caminho or menor_caminho == 0:
				menor_caminho = peso
				cls.set_peso(cls.getFim(), peso)
				return menor_caminho

		else:

			for vertice in lista_adjacencia:
				# Definindo o peso...
				distancia = cls.getDistancia(pesquisa, vertice)
				peso = predecessor + distancia
				cls.set_peso(vertice, peso)

				menor_caminho = cls.dijkstra(vertice, menor_caminho)

		return menor_caminho



# =========================================================================================


# Adicionando os vértices ao grafo...

vertices = {} # dicionário que contém os vértices e seus pesos e listas de adjacencia

ilhas, cabos = map(int, input().split())

for ilha in range(1, ilhas+1):
	vertices[ilha] = {} # Cria um dicionário para o vértice
	vertices[ilha]['peso'] = None	# Estabelece o peso inicial do vértice como sendo None
	vertices[ilha]['lista_adjacencia'] = [] # Estabelece uma lista de adjacência para o vértice


# =========================================================================================


# Criando a instância da classe...

grafo = Grafo(vertices)


# =========================================================================================


# Adicionando as arestas ao grafo...

for cabo in range(cabos):
	a, b, distancia = map(int, input().split())

	# Um vértice entra na lista de adjacência do outro.
	grafo.get_lista_adjacencia(a).append(b)
	grafo.get_lista_adjacencia(b).append(a)

	# Adicionando uma aresta
	grafo.setAresta(a,b,distancia)


# destino -> corresponde ao fim do grafo.
destino = int(input())
grafo.setFim(destino)


# =========================================================================================


# Fazendo a varredura em cada vértice, com exceção do destino...
menor_caminho = 0
maior_caminho = 0

for vertice in vertices.keys():
	if vertice != destino:
		grafo.setInicio(vertice)
		dijkstra = grafo.dijkstra(vertice, 0)
		print(vertice,dijkstra)

		if menor_caminho == 0 or dijkstra < menor_caminho and dijkstra != 0:
			menor_caminho = dijkstra

		if dijkstra > maior_caminho:
			maior_caminho = dijkstra

print(maior_caminho - menor_caminho)
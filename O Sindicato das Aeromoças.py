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


	def getVertices(cls):
		return cls._vertices


	def get_lista_adjacencia(cls, pesquisa):
		return cls._vertices[pesquisa]['lista_adjacencia']


	def get_peso(cls, pesquisa):
		return cls._vertices[pesquisa]['peso']


	def set_peso(cls, pesquisa, peso):
		cls._vertices[pesquisa]['peso'] = peso


	def zera_pesos(cls):
		vertices = cls.getVertices()
		for v in range(len(vertices)):
			cls.set_peso(v, None)


# ============================ MÉTODOS PARA AS ARESTAS ====================================


	def setAresta(cls, a, b, distancia):
		cls._arestas[(a,b)] = distancia
		cls._arestas[(b,a)] = distancia


	def getDistancia(cls, a, b):
		return cls._arestas[(a, b)]


	def setDistancia(cls, a, b, distancia):
		cls._arestas[(a,b)] = distancia
		cls._arestas[(b,a)] = distancia


# ======================================= DIJKSTRA ========================================


	def dijkstra(cls, pesquisa, menor_caminho = 0, pilha = []):

		lista_adjacencia = cls.get_lista_adjacencia(pesquisa)

		# Peso do vértice que está sendo verificado
		predecessor = cls.get_peso(pesquisa)

		# Adicionando o vértice aos verificados...
		pilha.append(pesquisa)

		for vertice in lista_adjacencia:
			if vertice not in pilha:
				# O peso de um vértice é o peso do vértice anterior
				# somado à distância entre estes dois vértices.			
				distancia = cls.getDistancia(pesquisa, vertice)
				peso = predecessor + distancia

				# Se o peso encontrado for menor do que o peso já
				# estabelecido ou se este nó ainda não tiver um peso
				# atribuído, o novo peso será atribuído.
				if cls.get_peso(vertice) == None or peso < cls.get_peso(vertice):
					cls.set_peso(vertice, peso)

				# Se o vértice final foi encontrado, vamos comparar 
				# os caminhos a fim de encontrar o menor possível.
				if vertice == cls.getFim():
					if peso < menor_caminho or menor_caminho == 0:
						menor_caminho = peso

				else:
					menor_caminho = cls.dijkstra(vertice, menor_caminho)


			# Se a lista de adjacência de um vértice foi completamente varrida,
			# ele será removido da pilha e a busca será continuada
			if vertice == lista_adjacencia[-1]:
				pilha.pop()

		return menor_caminho



# =========================================================================================


# Adicionando os vértices ao grafo...

vertices = {} # dicionário que contém os vértices e seus pesos e listas de adjacencia

cidades, cabos = map(int, input().split())

for cidade in range(cidades):
	vertices[cidade] = {} # Cria um dicionário para o vértice
	vertices[cidade]['peso'] = None	# Estabelece o peso inicial do vértice como sendo None
	vertices[cidade]['lista_adjacencia'] = [] # Estabelece uma lista de adjacência para o vértice


# =========================================================================================


# Criando a instância da classe...

grafo = Grafo(vertices)


# =========================================================================================


# Adicionando as arestas ao grafo...

for cabo in range(cabos):
	a, b, distancia = map(int, input().split())

	lista_adjacencia = grafo.get_lista_adjacencia(a)

	if b not in lista_adjacencia:
		# Um vértice entra na lista de adjacência do outro.
		grafo.get_lista_adjacencia(a).append(b)
		grafo.get_lista_adjacencia(b).append(a)

		# Adicionando uma aresta
		grafo.setAresta(a,b,distancia)

	elif grafo.getDistancia(a,b) > distancia:
		grafo.setDistancia(a, b, distancia)


# =========================================================================================


# Fazendo a varredura em cada vértice, com exceção do destino...
caminho_maximo = 0


# O final do grafo é alterado a cada iteração
for destino in vertices.keys():
	# destino -> corresponde ao fim do grafo.
	grafo.setFim(destino)

	# Maior distância entre as aeromoças...
	maior_distancia = 0

	for vertice in vertices.keys():
		if vertice != destino:
			grafo.setInicio(vertice)
			dijkstra = grafo.dijkstra(vertice, 0)

			if dijkstra > maior_distancia:
				maior_distancia = dijkstra

			# Zera
			grafo.zera_pesos()

	# O caminho máximo é a maior distância mínima
	# que uma aeromoça pode percorrer

	if caminho_maximo == 0 or caminho_maximo > maior_distancia:
		caminho_maximo = maior_distancia

print(caminho_maximo)
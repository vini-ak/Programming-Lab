''' 


'''

class Grafo:
	def __init__(self, vertices, fim = None):
		self._vertices = vertices # um dicionário com vértices e pesos.
		self._arestas = {}	# Dicionário contendo arestas e distâncias.
		self._inicio = None	# Definindo o inicio da pesquisa.
		self.fim = fim	# Definindo a cidade de destino.

	def addAresta(cls, a, b, distancia):
		''' Aresta e distância entre os vértices. '''
		cls._arestas[(a, b)] = distancia
		cls._arestas[(b, a)] = distancia

	def getVertices(cls):
		''' Retorna os vértices. '''
		return cls._vertices

	def predecessor(cls, predecessor = None):
		''' O peso do predecessor. '''
		return predecessor

	def getArestas(cls):
		''' Retorna as arestas.'''
		return cls._arestas

	def get_lista_adjacencia_vertice(cls, vertice):
		''' Retorna a lista de adjacência de um vértice.'''
		return cls.getVertices()[vertice]['lista_adjacencia']

	def get_peso_vertice(cls, vertice):
		''' Retorna o peso de um determinado vértice.'''
		return cls.getVertices()[vertice]['peso']

	def set_peso_vertice(cls, vertice, novo_peso):
		''' Alterando o peso de um vértice. '''
		if cls.get_peso_vertice(vertice) == None:
			cls.getVertices()[vertice]['peso'] = novo_peso
		elif cls.get_peso_vertice(vertice) > novo_peso:
			cls.getVertices()[vertice]['peso'] = novo_peso
		else:
			cls.getVertices()[vertice]['peso'] += novo_peso

	def setInicio(cls, vertice):
		''' Define o começo da pesquisa. '''
		cls._inicio = vertice
		cls.getVertices()[vertice]['peso'] = 0

	def dijkstra(cls, v, menor_caminho = 0, path = []):

		''' Procurando o menor caminho entre duas cidades. '''
		pesquisa = v
		path.append(pesquisa)

		# Procurando a lista de adjacencia da cidade de partida
		lista_adjacencia = cls.get_lista_adjacencia_vertice(pesquisa)

		for vertice in lista_adjacencia:
			# Se o vértice ainda não estiver no caminho
			if vertice not in path:
				# Pegando o peso do predecessor...
				predecessor = cls.get_peso_vertice(pesquisa)
				# Definindo a distancia no peso...
				distancia = cls.getArestas()[(pesquisa, vertice)]

				# O peso do vértice é dado pelo peso do seu predecessor somado com a distância entre eles.
				peso = predecessor + distancia

				# Se ainda não houver um peso associado ao vértice ou
				# se o peso encontrado acima for menor do que o peso já
				# definido, o peso deste vértice será alterado.
				if cls.get_peso_vertice(vertice) == None:
					cls.set_peso_vertice(vertice, peso)

				elif peso < cls.get_peso_vertice(vertice):
					cls.set_peso_vertice(vertice, peso)

				if vertice == cls.fim:
					if (cls.get_peso_vertice(pesquisa) < menor_caminho) or menor_caminho == 0:
						menor_caminho = cls.get_peso_vertice(vertice)
						return menor_caminho

				else:
					caminho = cls.dijkstra(vertice, menor_caminho)

		return menor_caminho

	def __str__(cls):
		''' Printa a lista de vértices e arestas. '''
		return str(cls.getVertices()) + '\n' + str(cls.getArestas())


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
	grafo.getVertices()[a]['lista_adjacencia'].append(b)
	grafo.getVertices()[b]['lista_adjacencia'].append(a)
	grafo.addAresta(a,b,distancia)


# destino -> corresponde ao fim do grafo.
destino = int(input())
grafo.fim = destino


# =========================================================================================


# Fazendo a varredura em cada vértice, com exceção do destino...
menor_caminho = 0
maior_caminho = 0

for vertice in vertices.keys():
	if vertice != destino:
		grafo.setInicio(vertice)
		dijkstra = grafo.dijkstra(vertice)

		if dijkstra < menor_caminho or menor_caminho == 0:
			menor_caminho = dijkstra

		if dijkstra > maior_caminho:
			maior_caminho = dijkstra

		print(vertice, dijkstra)

print(maior_caminho - menor_caminho)
''' 

1 - Criar um grafo não dirigido.

											COISAS QUE FALTARAM FAZER


2 - Adicionar cada aresta às arestas do grafo.
3 - Chamar o método Dijkstra do Grafo para poder fazer a varredura tanto do menor caminho, quanto do maior caminho
4 - Retornar o maior e o menor caminho possível.

'''

class Grafo:
	def __init__(self, vertices, inicio, fim):
		self._vertices = vertices # um dicionário com vértices e pesos.
		self._arestas = {}	# Dicionário contendo arestas e distâncias.
		self.inicio = inicio	# Definindo o inicio da pesquisa.
		self.fim = fim	# Definindo a cidade de destino.

	def addAresta(cls, a, b, distancia):
		''' Aresta e distância entre os vértices. '''
		cls._arestas[(a,b)] = distancia

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
		return cls.getVertices()[vertice]['lista_adjacencia']

	def get_peso_vertice(cls, vertice):
		return cls.getVertices()[vertice]['peso']

	def set_peso_vertice(cls, vertice, novo_peso):
		''' Alterando o peso de um vértice. '''
		if cls.get_peso_vertice(vertice) == None:
			cls.getVertices()[vertice]['peso'] = novo_peso
		elif cls.get_peso_vertice(vertice) > novo_peso:
			cls.getVertices()[vertice]['peso'] = novo_peso
		else:
			cls.getVertices()[vertice]['peso'] += novo_peso

	def dijkstra(cls, pesquisa, menor_caminho=0, maior_ caminho = 0):
		''' Procurando o menor caminho entre duas cidades. '''

		# Procurando a lista de adjacencia da cidade de partida
		lista_adjacencia = cls.get_lista_adjacencia_vertice(pesquisa)

		print(pesquisa)

		for vertice in lista_adjacencia:
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
				if (cls.get_peso_vertice(pesquisa) > maior_caminho) or maior_caminho == 0:
					maior_caminho = cls.get_peso_vertice(vertice)
					
				return menor_caminho, maior_caminho


			else:
				caminho = cls.dijkstra(vertice, menor_caminho, maior_caminho)

		return maior_caminho - menor_caminho

	def __str__(cls):
		''' Printa a lista de vértices e arestas. '''
		return str(cls.getVertices()) + '\n' + str(cls.getArestas())

''' ------------------------------------------------------------------- '''

ilhas, cabos = map(int, input().split())

grafo = Grafo()

for cabo in range(cabos):
	path = map(int, input().split())

destino = int(input())
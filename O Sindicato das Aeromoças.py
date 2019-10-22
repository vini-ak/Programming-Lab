def converteInt(string):
	lista = []
	n = ''
	for i in string:
		if i != " ":
			n += i
		else:
			lista += [int(n)]
			n = ''
	if n != '':
		lista += [int(n)]

	return lista

def dikjstra(arestas, pesos, v, inicio):
	maior = float("-inf")
	while v:
		lista_adjacencia = arestas[inicio]
		v.remove(inicio)
		for tupla in lista_adjacencia:
			peso_atual = pesos[tupla[0]]
			peso_temp = pesos[inicio] + tupla[1]
			if peso_temp < peso_atual:
				pesos[tupla[0]] = peso_temp
		if v:
			inicio = v[0]

	for i in range(len(pesos)):
		# Recuperando a lista de vértices.
		v += [i]
		# Separando a maior distância entre cidades partindo de inicio.
		if pesos[i] > maior:
			maior = pesos[i]
	return maior


# ===========================================================================

entrada1 = converteInt(input())	# passando o número de cidades e linhas aéreas
cidades = entrada1[0]	# numero de cidades
linhas_aereas = entrada1[1]	# numero de linhas aéreas
arestas = []
vertices = []

for v in range(cidades):
	arestas.append([])
	vertices += [v]

for i in range(linhas_aereas):
	entrada2 = converteInt(input())
	cidade_a = entrada2[0]
	cidade_b = entrada2[1]
	distancia = entrada2[2]

	arestas[cidade_a] += [(cidade_b, distancia)]
	arestas[cidade_b] += [(cidade_a, distancia)]

maximo = float("inf")

for j in range(cidades):
	pesos = [float('inf')] * cidades
	pesos[j] = 0
	a = dikjstra(arestas, pesos, vertices, j)
	if a < maximo:
		maximo = a

print(maximo)

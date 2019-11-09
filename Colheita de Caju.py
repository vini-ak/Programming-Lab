# Caju

l, c, m, n = map(int, input().split())
# l é o número de linhas do campo de cajueiros.
# c é o número de colunas do campo de cajueiros.
# m é o número de linhas a serem colhidas.
# n é o número de colunas a serem colhidas.

# Definindo a MATRIZ da fazenda de cajueiros
fazendaCajueiros = [[0]] * l

# Tabela de ÁREAS:
areas = []

for p in range(l):
	linha = list(map(int, input().split()))	# Passando os valores da linha
	fazendaCajueiros[p] = linha	# Adicionando a linha à matriz
	areas += [[0] * c]

for i in range(l):
	for j in range(c):
		areas[i][j] = fazendaCajueiros[i][j] + (areas[i-1][j] + areas[i][j-1] - areas[i-1][j-1])

# Determinando a maior colheita possível:
maior_colheita = 0

for u in range(m-1, l):
	for v in range(n-1, c):
		linha_anterior = u-m	# linha anterior à "janela" de colheita
		coluna_anterior = v-n	# coluna anterior à "janela" de colheita
		if linha_anterior >= 0 and coluna_anterior >= 0:
			area = (areas[u][v] - areas[linha_anterior][v] - areas[u][coluna_anterior] + areas[linha_anterior][coluna_anterior])
			if area > maior_colheita:
				maior_colheita = area

print(maior_colheita)
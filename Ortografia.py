''' 
ORTOGRAFIA
1 - SUBSTITUIR
2 - REMOVER
3 - ADICIONAR
'''
def minimo(n1, n2, n3):
	if n1 <= n2 and n1 <= n3:
		return n1
	elif n2 < n1 and n2 <= n3:
		return n2
	else:
		return n3

def distanciaLevenshtein(a,b):
	# Criando uma tabela a * b
	tabela = []
	for i in range(len(a)):
		tabela += [[0] * len(b)]

		# Moficando os valores da primeira coluna
		tabela[i][0] = i

	# Modificando os valores da primeira linha
	for c in range(len(b)):
		tabela[0][c] = c

	custo = 0

	for x in range(1, len(a)):
		for y in range(1, len(b)):
			if a[x] == b[y]: 
				custo = 0
			else:
				custo = 2 # Custo para substituição

			tabela[x][y] = minimo(tabela[x-1][y] + 1, tabela[x][y-1] + 1, tabela[x-1][y-1] + custo)

	return tabela[len(a)-1][len(b)-1]





n, m = map(int, input().split())

certas = []
for p in range(n):
	palavra = " "+input()
	certas += [palavra]

verificadas = []
for q in range(m):
	palavra = " "+input()
	verificadas += [palavra]

res = []
print('\nDistâncias de edição\n\n')
for pv in verificadas:
	res_ver = []
	for pc in certas:
		dist_edicao = distanciaLevenshtein(pv,pc)
		if dist_edicao <= 2:
			res_ver += [pc]

	res += [res_ver]

for linha in res:
	print(linha)

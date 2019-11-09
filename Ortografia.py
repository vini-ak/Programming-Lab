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

def distanciaMinima(a,b):
	# Criando uma tabela a * b
	tabela = []
	for i in range(len(a)):
		tabela += [[0] * len(b)]

		# Moficando os valores da primeira coluna
		tabela[i][0] = i

	# Modificando os valores da primeira linha
	for c in range(len(b)):
		tabela[0][c] = c

	for x in range(1, len(a)):
		for y in range(1, len(b)):
			if a[x] == b[y]:
				tabela[x][y] = tabela[x-1][y-1]
			else:
				tabela[x][y] = (minimo(tabela[x][y-1], tabela[x-1][y-1], tabela[x-1][y])+1) 

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

for pv in verificadas:
	res_ver = ""
	for pc in certas:
		dist_edicao = distanciaMinima(pv,pc)
		if dist_edicao <= 2:
			res_ver += pc[1:] + " "

	print(res_ver[0:-1])
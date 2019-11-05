''' PROBLEMA DA MOCHILA.'''

def maximo(a,b):
	if a>=b:
		valor_maximo = a
	else:
		valor_maximo = b
	return valor_maximo

n, c = map(int, input().split())
# n é o número de objetos
# c é a capacidade da mochila

objetos = []	# lista de listas (peso, valor)

for k in range(n):
	peso, valor = map(int, input().split())
	objetos += [[peso, valor]]

matriz = []
for l in range(n+1):
	linha = [0] * (c+1)
	matriz += [linha]

# i -> linha
for i in range(1,n+1):
	# j -> coluna
	for j in range(1,c+1):
		# Se o peso do objeto for menor ou igual a j
		if objetos[i-1][0] <= j:
			num = objetos[i-1][1] + matriz[i-1][j-objetos[i-1][0]] # valor do objeto + o objeto com peso que complete o peso da mochila 
			esq = matriz[i-1][j]
			matriz[i][j] = maximo(num, esq)
		# Se for maior, o valor acima é carregado.
		else:
			matriz[i][j] = matriz[i-1][j]

print(matriz[n][c])
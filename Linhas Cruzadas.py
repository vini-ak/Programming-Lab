vertices = int(input()) # numero de vértices
lista = [int(x) for x in input().split()] # Adicionando os vértices

# Número de cruzamentos: 
cruzamentos = 0

# Verificação crescente da lista
for i in range(vertices - 1):
	for j in range(i+1, vertices):
		if lista[i] > lista[j]:
			cruzamentos += 1

print(cruzamentos)
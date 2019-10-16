''' O número de pedaços será medido através da quantidade de
desnivelamento entre os retângulos de papel.'''

while True:
	numero_pedacos = int(input())
	pedacos = list(map(int, input().split()))

	# Por garantia, já temos dois pedaços
	# pois quando cortamos, dividimos em duas partes
	maximo_pedacos = 2

	for i in range(1, numero_pedacos - 1):
		anterior = pedacos[i-1]
		pedaco = pedacos[i] 
		proximo = pedacos[i+1]

		if pedaco < anterior and pedaco < proximo:
			# Foi encontrado um buraco
			maximo_pedacos += 1
	
	print(maximo_pedacos)
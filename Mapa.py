'''
A questão pede que nós pintemos um mapa de modo que
duas áreas vizinhas não possam ser pintadas pela 
mesma cor.

O código deve retornar o número de cores que foram usadas
para pintar o mapa.

Devemos nos preocupar com a otimização do problema.

=========================================================

                    REGRAS DA ENTRADA


1 - Será inputada o número de estados;

2 - Será inputada uma série de termos binários separados 
por espaço, simbolizando o grafo e suas fronteiras.

3 - Deve começar sempre com o vértice de maior grau (mais fronteiras)

EXEMPLOS:

8
0 1 1 1 1 1 0 0
1 0 1 0 0 0 0 0
1 1 0 1 0 0 0 1
1 0 1 0 1 0 0 1
1 0 0 1 0 1 0 1
1 0 0 0 1 0 1 1
0 0 0 0 0 1 0 1
0 0 1 1 1 1 1 0


8
0 1 1 1 1 1 0 0
1 0 1 0 0 0 1 1
1 1 0 1 0 0 1 0
1 0 1 0 1 0 1 0
1 0 0 1 0 1 1 0
1 0 0 0 1 0 0 0
0 1 1 1 1 0 0 1
0 1 0 0 0 0 1 0


5
0 1 1 1 1
1 0 1 1 1
1 1 0 1 1
1 1 1 0 1
1 1 1 1 0


6
0 1 0 1 1 0
1 0 1 0 0 1
0 1 0 0 0 1
1 0 0 0 0 0
1 0 0 0 0 1
0 1 1 0 1 0


8
0 1 1 1 1 1 0 0
1 0 1 0 0 0 1 1
1 1 0 1 0 0 0 1
1 0 1 0 1 0 0 1
1 0 0 1 0 1 0 1
1 0 0 0 1 0 0 0
0 1 0 0 0 0 0 1
0 1 1 1 1 0 1 0


'''
def troca_cor(pos, cores_disponiveis):
  # Para ser branco, o estado ou não possui fronteiras, ou só existem duas opções de cores disponíveis.
  if cores_disponiveis == {'white', 'blue', 'red', 'green'} or cores_disponiveis == {'white', 'green'}:
    pos = 'white'
  # A primeira prioridade para a pintura é a cor vermelha. Se ela estiver disponível, deve ser usada.
  elif 'red' in cores_disponiveis:
    pos = 'red'
  # Se caso o vermelho não estiver disponível, o azul é a cor imediata.
  elif 'blue' in cores_disponiveis:
    pos = 'blue'
  # Verde só é usada em último caso.
  else:
    pos = 'green'
  
  return pos


def matriz():
  ''' Criando a função para que o código saia do escopo global.'''

  matriz = [] # Matriz que representa o estado e suas fronteiras
  cores = {'white', 'red', 'blue', 'green'} # Esquema de cores disponíveis para pintura
  cores_usadas = set() # As cores que foram usadas para fazer a pintura

  numero_de_estados = int(input('Número de áreas: ')) # quantos estados este país tem?

  for i in range(numero_de_estados):
    # Inputando a área e suas fronteiras:
    estado_e_fronteiras = input().split(' ')
    # Adicionando essas informações à matriz
    matriz.append(estado_e_fronteiras)
    # Definindo a cor dos estados. Por padrão, ela será 'white'
    matriz[i][i] = 'white'
    

    contador = 0 # O contador que vai percorrer somente os estados com cores definidas.
    cores_encontradas = set() # Conjunto das cores preenchidas pelos vizinhos

    # Loop para verificar as cores existentes
    while contador < i:
      if matriz[i][contador] == '1':
        cores_encontradas.add(matriz[contador][contador])
      contador += 1

    # Atribuindo uma nova cor ao estado...
    dif = cores - cores_encontradas # Conjunto das cores disponíveis
    matriz[i][i] = troca_cor(matriz[i][i], dif)
    if matriz[i][i] not in cores_usadas:
      cores_usadas.add(matriz[i][i])


  return len(cores_usadas)

print("\nTotal de cores: ",matriz())

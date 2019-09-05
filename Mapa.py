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
  Exemplo: '0 1 1 1 1 1 0 0'
3 - Deve começar sempre com o vértice de maior grau

'''
def troca_cor(pos, cores_disponiveis):
  if cores_disponiveis == {'white', 'blue', 'red', 'green'} or cores_disponiveis == {'white', 'green'}:
    pos = 'white'
  elif 'red' in cores_disponiveis:
    pos = 'red'
  elif 'blue' in cores_disponiveis:
    pos = 'blue'
  else:
    pos = 'green'
  
  return pos

def matriz():
  ''' Criando a função para que o código saia do escopo global.'''

  matriz = []
  cores = {'white', 'red', 'blue', 'green'}
  cores_usadas = set()

  numero_de_estados = int(input('Número de áreas: ')) # quantos estados este país tem?

  for i in range(numero_de_estados):
    # Inputando a área e suas fronteiras:
    estado_e_fronteiras = input().split(' ')
    # Adicionando essas informações à matriz
    matriz.append(estado_e_fronteiras)
    # Definindo a cor dos estados. Por padrão, ela será 'white'
    matriz[i][i] = 'white'
    

    # Loop para verificar as cores existentes
    contador = 0
    cores_encontradas = set()

    while contador < i:
      if matriz[i][contador] == '1':
        cores_encontradas.add(matriz[contador][contador])
      contador += 1

    # Atribuindo uma nova cor ao estado...
    dif = cores - cores_encontradas # Conjunto das cores disponíveis
    matriz[i][i] = troca_cor(matriz[i][i], dif)
    if matriz[i][i] not in cores_usadas:
      cores_usadas.add(matriz[i][i])
      if len(cores_usadas) == 4:
        return 4
  
  print()

  for line in matriz:
    print(line)
  
  print()

  return len(cores_usadas)

print(matriz())

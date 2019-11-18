class Node:
	def __init__(self, dados, anterior = None, proximo = None):
		self.__nome = dados[0]
		self.__plano = dados[1]
		self.__grau = int(dados[2])
		self.__anterior = anterior
		self.__proximo = proximo

	def getNome(cls):
		return cls.__nome

	def setNome(cls, novoNome):
		cls.__nome = novoNome

	def getPlano(cls):
		return cls.__plano

	def setPlano(cls, plano):
		cls.__plano = plano 

	def prioridadePlano(cls):
		if cls.getPlano() == 'premium':
			return 6
		elif cls.getPlano() == 'diamante':
			return 5
		elif cls.getPlano() == 'ouro':
			return 4
		elif cls.getPlano() == 'prata':
			return 3
		elif cls.getPlano() == 'bronze':
			return 2
		elif cls.getPlano() == 'resto':
			return 1

	def getGrau(cls):
		return cls.__grau

	def setGrau(cls, novoGrau):
		cls.__grau = novoGrau

	def getAnterior(cls):
		return cls.__anterior

	def setAnterior(cls, novoanterior):
		cls.__anterior = novoanterior

	def getProximo(cls):
		return cls.__proximo

	def setProximo(cls, novoproximo):
		cls.__proximo = novoproximo


class Fila:
	def __init__(self, inicio = None, fim = None):
		self._inicio = inicio
		self._fim = fim 

	def getInicio(cls):
		return cls._inicio

	def getFim(cls):
		return cls._fim

	def setInicio(cls, novoInicio):
		cls._inicio = novoInicio

	def setFim(cls, novoFim):
		cls._fim = novoFim

	def isVazia(cls):
		return cls.getInicio() == None

	def inserir(cls, dados):
		paciente = Node(dados)
		if cls.isVazia():
			cls.setInicio(paciente)
			cls.setFim(paciente)
		else:
			no = cls.getInicio()
			found = False
			while no is not None and found == False:
				if paciente.prioridadePlano() > no.prioridadePlano():
					paciente.setAnterior(no.getAnterior())
					paciente.setProximo(no)
					no.setAnterior(paciente)
					found = True

					if no is cls.getInicio():
						cls.setInicio(paciente)
					if no is cls.getFim():
						cls.setFim(paciente)

				elif paciente.prioridadePlano() == no.prioridadePlano():
					if paciente.getGrau() > no.getGrau():
						print('eu sou maior')
						paciente.setAnterior(no.getAnterior())
						paciente.setProximo(no)
						no.setAnterior(paciente)
						found = True

						if no is cls.getInicio():
							cls.setInicio(paciente)
						if no is cls.getFim():
							cls.setFim(paciente)

					elif paciente.getGrau() == no.getGrau():
						print("compara os nome")
						if paciente.getNome() < no.getNome():
							paciente.setAnterior(no.getAnterior())
							paciente.setProximo(no)
							no.setAnterior(paciente)
							found = True

							if no is cls.getInicio():
								cls.setInicio(paciente)
							if no is cls.getFim():
								cls.setFim(paciente)

				no = no.getProximo()
				if no is not None:
					print(no.getNome())

			if not found:
				cls.getFim().setProximo(paciente)
				paciente.setAnterior(cls.getFim)
				cls.setFim(paciente)


	def varrer(cls):
		no = cls.getInicio()
		while no is not None:
			print(no.getNome())
			no = no.getProximo()


	def __str__(cls):
		''' Define o que será exibido quando a lista receber um print'''
		imprimeLista = ''
		i = cls._inicio
		while i is not None:
			imprimeLista += str(i.getNome()) + " -> "
			i = i.getProximo()
			if i is None:
				imprimeLista += 'Acabou esse carai'
				
		if imprimeLista == "":
			imprimeLista = "Lista vazia kkkkkkk bichinha"
		return imprimeLista




# entrada:

numeroPacientes = int(input())
fila = Fila()

for p in range(numeroPacientes):
	dados = input().split()
	fila.inserir(dados)
	print(fila)

fila.varrer()
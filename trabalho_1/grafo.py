class Nodo:
		vizinhos = []
		id = ''
		rotulo = ''
		ehRaiz = False

		def __init__(self, id_, rotulo):
			Nodo.id = id_
			Nodo.rotulo = rotulo

		def vizinhos():
			return vizinhos
		
		def adicionarVizinhos(self, vertice_vizinho, peso):
			vizinhos.append([vertice_vizinho,peso])

		def ehRaiz():
			return ehRaiz

		def rotulo():
			return rotulo

		def adicionarRotulo(self, rotulo_):
			rotulo = rotulo_


class Grafo:
	qtd_vertices = 0
	qtd_arestas = 0
	vertices = []

	
	
	def adicionarVertice(self, id_, rotulo):
		self.vertices.append(Nodo(id_, rotulo))
		print(self.vertices[0].id, self.vertices[0].rotulo)

	# def printartudo(self):
	# 	for i in range(0, len(Grafo.vertices)):
	# 		Grafo.vertices[i].printacarai()
	# def __init__(self):

	# def qtdVertices():
		
	# def qtdArestas():

	# def grau(v):

	# def rotulo(v):

	# def vizinhos(v):

	# def haAresta(u, v):

	# def peso(u, v):

	# def ler(arquivo):

	

a = open('facebook_santiago.net', 'r')
nomes = []
grafo = Grafo()
# print(len(grafo.vertices))

for i in a:
	linha = i.split()
	lista = []
	if (linha[0] == '*vertices'):
		# print(linha[1])
		for j in range(int(linha[1])):
			info1, info2 = a.readline().split(' ', 1)
			grafo.adicionarVertice(info1, info2)
		#endfor
	# else:
	# 	#cria ligações


# class grafo:
# 	qtd_vertices = 0
# 	qtd_arestas = 0

# 	vertices = []

# 	def qtdVertices():

# 	def qtdArestas():

# 	def grau(v):

# 	def rotulo(v):

# 	def vizinhos(v):

# 	def haAresta(u, v):

# 	def peso(u, v):

# 	def ler(arquivo):

# 	class nodo:
# 		vizinhos = []
# 		rotulo = ''
# 		ehRaiz = False

# 		def vizinhos():
# 			return vizinhos

# 		def ehRaiz():
# 			return ehRaiz

# 		def rotulo():
# 			return rotulo

a = open('facebook_santiago.net', 'r')
nomes = []
for i in range(100):
	vertice, rotulo = a.readline().split(' ', 1)
	print(vertice)
	# print(a.readline().split(' ', 1))

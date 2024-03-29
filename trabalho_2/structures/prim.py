import copy
import sys
def prim_(grafo):
	r = 0
	A = dict([(i, None) for i,v in enumerate(grafo.vertices_)])
	K = dict([(i, sys.maxsize) for i,v in enumerate(grafo.vertices_)])
	K[r] = 0
	Q = [[i for i in range(len(grafo.vertices_))], K]

	soma = 0
	arestas = []

	while Q[0]:
		# i = 0
		# for v in K.values():
		# 	print(i, ':', v)
		# 	i = i + 1
		Q[0].sort(key = lambda u : K[u], reverse = False)
		u = Q[0].pop(0)
		# print(Q[0])

		for v, peso in grafo.vizinhos(u):
			if Q[0].count(v) and (peso < K[v]):
				soma = soma + peso
				arestas.append([grafo.rotulo(u), grafo.rotulo(v)])
				A[v] = u
				K[v] = peso
	
	return [A, soma, arestas]
import copy
import sys
def prim_(grafo):
	r = 10
	A = dict([(i, None) for i,v in enumerate(grafo.vertices_)])
	K = dict([(i, sys.maxsize) for i,v in enumerate(grafo.vertices_)])
	K[r] = 0
	Q = [[i for i in range(len(grafo.vertices_))], K]
	# print(Q[0])
	while Q[0]:
		Q[0].sort(key = lambda u : K[u], reverse = False)
		u = Q[0].pop(0)
		# print('u da vez = ', u)

		for v, peso in grafo.vizinhos(u):
			# print(v, peso)
			if Q[0].count(v) and (peso < K[v]):
				A[v] = u
				K[v] = peso
			# if v == 396 or v == 627:
			# 	print (grafo.vertices_[u])
			# 	print (v, '\n')
	# print(A.values())
	return
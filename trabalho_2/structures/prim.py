import copy
import sys
def prim(grafo):
	r = 0
	A = dict([(i, None) for i,v in enumerate(grafo.vertices_)])
	K = dict([(i, sys.maxsize) for i,v in enumerate(grafo.vertices_)])
	K[r] = 0
	Q = [A.keys(), K]
	while not Q[0]:
		Q[0].sort(key = lambda u : K[u], reverse = False)
		u = Q[0].pop(0)

		for v in grafo.vizinhanca(u):
			if Q[0].count(v) and (grafo.peso(u, v) < K[v]):
				A[v] = u
				K[v] = grafo.peso(u, v)
	return A
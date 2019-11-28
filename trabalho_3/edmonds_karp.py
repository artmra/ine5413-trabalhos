import sys
from grafo import Grafo

def ed_k(Grafo, origem, destino):
	n = Grafo.qtd_vertices()
	F = dict([((u, v), 0) for u in Grafo.vertices_ for v in Grafo.vertices_])

	# a capacidade residual de u para v é dada por C(u, v) - F(u, v)

	while True:
		caminho = bfs(Grafo, F, origem, destino)
		if not caminho:
			break

		u, v = caminho[0], caminho[1]
		menor = Grafo.peso(u, v) - F[(u, v)]

		for i in range(len(caminho) - 2):
			u, v = caminho[i + 1], caminho[i + 2]
			menor = min(menor, Grafo.peso(u, v) - F[(u, v)])

		for i in range(len(caminho) - 1):
			u, v = caminho[i], caminho[i + 1]
			F[(u, v)] = F[(u, v)] + menor
			F[(v, u)] = F[(v, u)] - menor

	return sum([F[(origem, i)] for i in range(1, n + 1)])

def bfs(Grafos, F, origem, destino):
	P = dict([(i, None) for i in range(len(Grafo.vertices_))])
	P[source] = source
	queue = [source]

	while len(queue) > 0:
		u = queue.pop(0)
		for v in Grafo.vizinhos(u):
			if Grafo.peso(u, v) - F[(u, v)] > 0 and P[v] is None:
				P[v] = u
				queue.append(v)
				if v == destino:
					caminho = []
					while True:
						caminho.insert(0, v)
						if v == origem:
							break
						v = P[v]
					return caminho
	return None
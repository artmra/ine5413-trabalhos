from structures.grafo import Grafo

# deve-se passar como parametro a origem e destino decrementados em uma unidade
def ed_k(Grafo, origem, destino):
	n = Grafo.qtd_vertices()
	F = dict([((u, v), 0) for u in range(n) for v in range(n)])

	# a capacidade residual de u para v é dada por C(u, v) - F(u, v)

	while True:
		caminho = bfs(Grafo, F, origem, destino)
		# obtem um caminho minimo da origem ao destino
		if not caminho:
			# se nao encontrar, sai
			break

		# inicia o processo de busca pela menor capacidade residual para todo arco do caminho
		u, v = caminho[0], caminho[1]
		menor = Grafo.peso(u, v) - F[(u, v)]

		for i in range(len(caminho) - 2):
			u, v = caminho[i + 1], caminho[i + 2]
			menor = min(menor, Grafo.peso(u, v) - F[(u, v)])

		# atualiza os fluxos atuais de cada aresta do caminho
		for i in range(len(caminho) - 1):
			u, v = caminho[i], caminho[i + 1]
			F[(u, v)] = F[(u, v)] + menor
			F[(v, u)] = F[(v, u)] - menor

	# retorna a soma dos fluxos
	sum_ = sum([F[(origem, i)] for i in range(n)])
	return sum_

def bfs(Grafo, F, origem, destino):
	# cria uma estrutura para armazenar o vértice que visitou um vertice u qualquer
	P = dict([(i, None) for i in range(Grafo.qtd_vertices())])
	P[origem] = origem
	queue = [origem]

	# enquanto a fila nao estiver vazia
	while len(queue) > 0:
		# retira o primeiro elemento da fila
		u = queue.pop(0)

		# para todo vizinho desse vértice
		for v in Grafo.vizinhos(u):
			# se ele ainda não foi visitado e a capacidade residual for maior que 0
			if Grafo.peso(u, v[0]) - F[(u, v[0])] > 0 and P[v[0]] is None:
				# marca por quem o vertice v foi visitado
				P[v[0]] = u
				# adiciona a fila, para propagar as visitas
				queue.append(v[0])
				# se v for o vértice destino, contrói o caminho de u até v e o retorna
				if v[0] == destino:
					v_ = v[0]
					caminho = []
					while True:
						caminho.insert(0, v_)
						if v_ == origem:
							break
						v_ = P[v_]
					return caminho
	return None
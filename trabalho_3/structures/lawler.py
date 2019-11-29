from copy import deepcopy
import sys

def lawler(Grafo):
	n = Grafo.qtd_vertices()
	# cria um array com o indice de todos os vertices do grafo
	vertices = [i for i in range(n)]
	
	# cria uma lista de todos os subconjuntos dos vertices do grafo, já inserindo o conjunto vazio
	subconjuntos = [[]]
	# preenche a lista com todos os subconjuntos diferentes possiveis
	criar_subconjunto(subconjuntos, [], vertices, n)
	# adiciona o conjunto de vertices em si como ultimo elemento
	subconjuntos.append(vertices)

	# ordena todas as listas, afim de facilitar a busca por elementos mais tarde
	for i in subconjuntos:
		i.sort(reverse=True)

	# cria e inicializa uma lista que conterá o número de cores necessárias para cada subconjunto
	X = [sys.maxsize for i in range(len(subconjuntos))]
	# define que o número de cores necessárias para colorir o conjunto vazio é 0
	X[0] = 0


	# para cada subconjunto de vertices
	for s in range(len(subconjuntos)):
		
		# cria o conjunto de todos os subconjuntos independentes dos vertices desse subgrafoo
		subconjuntos_independentes = []
		criar_conjunto_independente(Grafo, subconjuntos_independentes, [], subconjuntos[s])
		
		# para cada subconjunto indepedente criado
		for si in subconjuntos_independentes:
			# armazena em i a diferença entre o subconjunto e um de seus subconjuntos
			i = deepcopy(subconjuntos[s])
			for j in range(len(si)):
				i.remove(si[j])
			# ordena o resultado
			i.sort(reverse=True)
			
			# procura o indice desse subconjunto na lista de subconjuntos
			index = subconjuntos.index(i)
			
			# se o numero de cores desse subconjunto for menor que o numero de cores do subconjunto em si, atualiza o
			# numero de cores necessárias para se colorir esse subgrafo
			if X[index] + 1 < X[s]:
				X[s] = X[index] + 1

	# como o numero de cores necessárias para se colorir o grafo original; Esse numero está disponível no último indice do array
	# qualquer coisa só olhar na linha 14
	return X[len(X) - 1]


# cria todos os subconjuntos possíveis, evitando repetições do tipo [1, 2, 3] e [3, 2, 1]
def criar_subconjunto(tds_subconjuntos, subconjunto_atual, vertices, n_vertices):
	# verificação adicionada para impedir que o próprio conjunto de vértices seja criado
	if len(subconjunto_atual) + 1 == n_vertices:
		return

	# array de vertices visitados
	visited = [False for i in range(len(vertices))]

	# para todo vertice no array de vértices passado na entrada
	for v in range(len(vertices)):
		# cria um novo conjunto de vértices vazio
		vertices_ = []
		# marca que o vértice no indice v foi visitado
		visited[v] = True
		# preenche o novo array de vertices com todos os vertices não visitados em iterações anteriores
		for i in range(len(vertices)):
			if visited[i] == False:
				vertices_.append(vertices[i])
		# cria uma cópia do subconjunto atual passado como parametro
		subconjunto_atual_ = deepcopy(subconjunto_atual)
		# adiciona o vertice do indice v nesse novo subconjunto
		subconjunto_atual_.append(vertices[v])
		# adiciona esse novo subconjunto ao conjunto de todos os subconjuntos criados ate entao
		tds_subconjuntos.append(subconjunto_atual_)
		# propaga a criacao de novos subconjuntos usando o subconjunto criado na iteracao atual como base,
		# e os vertices que ainda nao haviam sido visitados
		criar_subconjunto(tds_subconjuntos, subconjunto_atual_, vertices_, n_vertices)

def criar_conjunto_independente(Grafo, tds_subconjuntos, subconjunto_atual, vertices):
	# array de vertices visitados
	visited = [False for i in range(len(vertices))]

	# para todo vertice no array de vértices passado na entrada
	for v in range(len(vertices)):
		# cria um novo conjunto de vértices vazio
		vertices_ = []
		# marca que o vértice no indice v foi visitado
		visited[v] = True
		# preenche o novo array de vertices com todos os vertices não visitados em iterações anteriores
		for i in range(len(vertices)):
			if visited[i] == False:
				vertices_.append(vertices[i])
		# cria uma cópia do subconjunto atual passado como parametro
		subconjunto_atual_ = deepcopy(subconjunto_atual)
		# adiciona o vertice do indice v nesse novo subconjunto caso nao exista nenhuma aresta entre eles e os vertices que
		# ja se encontram no conjunto
		adicionar = True
		for u in subconjunto_atual:
			if Grafo.ha_aresta(vertices[i], u):
				adicionar = False
				break
		if adicionar:
			# caso o requisito seja atendido, adiciona o vertice
			subconjunto_atual_.append(vertices[v])

		# propaga a criacao de novos subconjuntos indepentes usando o subconjunto criado na iteracao atual como base,
		# e os vertices que ainda nao haviam sido visitados
		tds_subconjuntos.append(subconjunto_atual_)
		criar_conjunto_independente(Grafo, tds_subconjuntos, subconjunto_atual_, vertices_)
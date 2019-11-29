from structures.grafo import Grafo
from structures.lawler import lawler
from copy import deepcopy

grafo = Grafo('teste2.gr')

n_colors = lawler(grafo)

print("1º numéro mínimo de cores necessárias: ", n_colors, '\n')

cores = [(i + 1) for i in range(n_colors)]

cor_vertice_ = [0 for i in range(grafo.qtd_vertices())]

# colorindo grafo
print('2º colorindo o grafo: \n')
for v in range(grafo.qtd_vertices()):
	# copia lista de cores
	cores_disponiveis = deepcopy(cores)
	print('vertice ',v+1)
	print('cores dos meus vizinhos ->')
	# marca como 0 todas as cores indisponíveis
	for u in grafo.vizinhos(v):
		print('cor de ', u[0] + 1, ':', cor_vertice_[u[0]])
		if not(cor_vertice_[u[0]] == 0):
			cores_disponiveis[cor_vertice_[u[0]] - 1] = 0
	
	# procura a primeira cor disponível e marca o vertice com ela
	for i in range(len(cores_disponiveis)):
		if not(cores_disponiveis[i] == 0):
			cor_vertice_[v] = cores_disponiveis[i]
			print('minha cor é: ', cor_vertice_[v])
			break
	
	# se nao achar, cria uma nova cor
	if cor_vertice_[v] == 0:
		cores.append(len(cores) + 1)
		cor_vertice_[v] = cores[len(cores) - 1]

	print('')

print('3º resultado final:')
for v in range(grafo.qtd_vertices()):
	print('vértice', (v + 1), ', cor: ', cor_vertice_[v])
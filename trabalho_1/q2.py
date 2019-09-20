from structures.grafo import Grafo
from structures.breadth_first_search import bfs
import sys

grafo = Grafo('fln_pequena.net')
print("Digite o vertice para iniciar a busca:")
# s = int(input())

D, A = bfs(grafo, 1)
# cria um dicionário para cada armazenar um lista de vértices em cada nível
levels_and_elements = dict([(d, []) for d in D])

# adiciona cada vértice em seu respectivel nível
for i in range(len(A)):
    if not D[i] is sys.maxsize:
        levels_and_elements[D[i]].append(i)

# imprime os níveis e os elementos em cada um deles
for l in levels_and_elements.keys():
    print(l, ":", str(levels_and_elements[l]).strip('[]'))
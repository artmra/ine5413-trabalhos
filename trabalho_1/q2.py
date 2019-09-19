from structures.grafo import Grafo
from structures.breadth_first_search import bfs

grafo = Grafo('fln_pequena.net')
print("Digite o vertice para iniciar a busca:")
# s = int(input())
bfs(grafo, 1)

from structures.grafo import Grafo
from structures.edmonds_karp import ed_k

grafo = Grafo('teste1.gr')

print(ed_k(grafo, 0, 5))
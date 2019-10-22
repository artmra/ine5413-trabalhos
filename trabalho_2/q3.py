from structures.grafo import Grafo
from structures.prim import prim_

grafo = Grafo('facebook_santiago.net')

print("Quantidade de vertices : ",grafo.qtd_vertices())
print("Quantidade de arestas", grafo.qtd_arestas())
prim_(grafo)		
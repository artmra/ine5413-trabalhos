from structures.grafo import Grafo
from structures.ordenacao_topologica import ordenacao_topologica

grafo = Grafo('grafo.net')
ordenacao_topologica(grafo)

string = ""
for u in range (len(grafo.vertices_)):
	string += " -> " + grafo.rotulo(u)
print((string.replace("\n", "")).replace(" -> ", "", 1))

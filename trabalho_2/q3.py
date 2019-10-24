from structures.grafo import Grafo
from structures.prim import prim_

grafo = Grafo('fln_pequena.net')
print('O programa irá imprimir os indices dos vértices da arvore \n\n')
A, soma, arestas = prim_(grafo)
print (soma)
primeira_aresta = arestas.pop(0)
aresta_1 = primeira_aresta[0]
aresta_1 += '    -    '
aresta_1 += primeira_aresta[1]
print(aresta_1.replace('\n', ''))

for u,v in arestas:
	aresta_n = ','
	aresta_n += u
	aresta_n += '    -    '
	aresta_n += v
	print(aresta_n.replace('\n', ''),)
print('\n')
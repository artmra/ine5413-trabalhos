from structures.grafo import Grafo
from structures.prim import prim_

grafo = Grafo('facebook_santiago.net')
print('O programa irá imprimir os indices dos vértices da arvore \n\n')
A, soma, arestas = prim_(grafo)
print (soma)
primeira_aresta = arestas.pop(0)
print(primeira_aresta[0],'-',primeira_aresta[1], end = '')
for u,v in arestas:
    print(',', end = '')
    print(u,'-',v, end = '')
print('\n')
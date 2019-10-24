from structures.grafo import Grafo
from structures.componentes_fortemente_conexos import cfc

grafo1 = Grafo('facebook_santiago_dirigido.net')
# link do grafo usado: https://www.ime.usp.br/~pf/algoritmos_para_grafos/aulas/strong-comps.html
print('O programa irá imprimir o rótulo dos vértices de cada cfc \n\n')
cfc(grafo1)
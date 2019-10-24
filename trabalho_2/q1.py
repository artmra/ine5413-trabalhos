from structures.grafo import Grafo
from structures.componentes_fortemente_conexos import cfc

grafo1 = Grafo('GrafoCFC.net')
# link do grafo usado: https://www.ime.usp.br/~pf/algoritmos_para_grafos/aulas/strong-comps.html
print('O programa irá imprimir o rótulo dos vértices de cada cfc')
cfc(grafo1)
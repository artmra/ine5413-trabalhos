from structures.grafo import Grafo
from structures.hopcroft_karp import hopcroft_karp

grafo = Grafo('gr128_10.gr')

print(hopcroft_karp(grafo))
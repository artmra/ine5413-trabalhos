from structures.grafo import Grafo
from structures.dfs import dfs
from structures.bfs import bfs
import sys
def hopcroft_karp(grafo):
    D = dict([(i+1, sys.maxsize) for i, v in enumerate(grafo.vertices_)])
    D[None] = sys.maxsize

    # Mate = dict([(i+1, None) for i, v in enumerate(grafo.vertices_)])
    Mate = []
    for _ in grafo.vertices_:
        Mate.append(None)
    # tamanho de emparelhamento
    m = 0
    while bfs(grafo, Mate, D):
        for x in grafo.X:
            if (Mate[x] is None):
                if dfs(grafo, Mate, x, D):
                    m += 1
    return (m, Mate)
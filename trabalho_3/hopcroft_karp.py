from grafo import Grafo
import sys
def hopcroft_karp(grafo):
    D = []
    Mate = []

    # Configurando os vertices
    for _ in grafo.vertices_:
        D.append(sys.maxsize)
        Mate.append(None)
    # tamanho de emparelhamento
    m = 0
    while bfs(grafo, Mate, D):
        for x in grafo.X:
            if (Mate[x] == None):
                if dfs(grafo, Mate, x, D):
                    m += 1
    return (m, Mate)
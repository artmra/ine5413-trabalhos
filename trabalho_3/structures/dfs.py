import sys
from structures.grafo import Grafo
def dfs(grafo, Mate, x, D):
    if (x != None):
        for y in grafo.vizinhos(x):
            if (D[Mate[y[0]]] == D[x] + 1):
                if (dfs(grafo, Mate, Mate[y[0]], D)):
                    Mate[y[0]] = x
                    Mate[x] = y
                    return True
        D[x] = sys.maxsize
        return False
    return True
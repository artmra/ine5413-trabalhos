import sys
from grafo import Grafo
def dfs(grafo, Mate, x, D):
    if (x != None):
        for y in grafo.vizinhos(x):
            if (D[Mate[y]] == D[x] + 1):
                if (dfs(grafo, Mate, Mate[y], D)):
                    Mate[y] = x
                    Mate[x] = y
                    return True
        D[x] = sys.maxsize
        return False
    return True
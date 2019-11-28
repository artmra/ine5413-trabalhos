from grafo import Grafo
import sys
def bfs(grafo, Mate, D):
    Q = []
    for x in grafo.X:
        if (Mate[x] == None):
            D[x] = 0
            Q.append(x)
        else:
            D[x] = sys.maxsize
    D[None] = sys.maxsize
    while(not(len(Q))):
        x = Q.pop()
        if (D[x] < D[None]):
            for y in grafo.vizinhos(x):
                if (D[Mate[y]] == sys.maxsize):
                    D[Mate[y]] = D[x] + 1
                    Q.append(Mate[y])
    return (D[None] != sys.maxsize)
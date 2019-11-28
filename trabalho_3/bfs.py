from grafo import Grafo
import sys
def bfs(grafo, Mate, D):
    Q = []
    # print(grafo.X)
    for x in grafo.X:
        if (Mate[x] is None):
            D[x] = 0
            Q.append(x)
        else:
            D[x] = sys.maxsize
    D[None] = sys.maxsize
    while len(Q) > 0:
        x = Q.pop(0)
        if (D[x] < D[None]):
            for y in grafo.vizinhos(x):
                # print(Mate[y[0]])
                # print()
                # print(Mate[y[0]])
                if (D[Mate[y[0]]] == sys.maxsize):
                    D[Mate[y[0]]] = D[x] + 1
                    Q.append(Mate[y[0]])
    return (D[None] != sys.maxsize)
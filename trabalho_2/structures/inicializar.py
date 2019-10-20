def inicilizar(grafo, s):
    D = dict([(i, "infinite") for i in range(len(grafo.vertices_))])
    A = dict([(i, None) for i in range(len(grafo.vertices_))])
    D[s] = 0
    return [D, A]
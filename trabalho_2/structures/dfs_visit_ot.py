def dfs_visit_ot (grafo, v, C, T, F, tempo, lista):
    C[v] = True
    tempo += 1
    T[v] = tempo
    for u in grafo.vizinhos(v):
        if (not C[u[0]]):
            dfs_visit_ot(grafo, u, C, T, F, tempo, lista)
    tempo += 1
    F[v] = tempo
    lista.insert(0, v)
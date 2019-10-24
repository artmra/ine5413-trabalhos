def dfs_visit(grafo, v, C, T, A, F, tempo, cfc, adaptado):
    C[v] = True
    tempo = tempo + 1
    T[v] = tempo
    if adaptado and cfc.count(grafo.vertices_[v][0]) < 1:
        cfc.append(grafo.vertices_[v][0])

    for u, peso in grafo.vizinhos_saintes(v):
        if (not C[u]):
            if adaptado and cfc.count(grafo.vertices_[u][0]) < 1:
                cfc.append(grafo.vertices_[u][0])
                 # print(v, '->', u)
            A[u] = v
            tempo, cfc = dfs_visit(grafo, u, C, T, A, F, tempo, cfc, adaptado)

    tempo = tempo + 1
    F[v] = tempo
    return [tempo, cfc]
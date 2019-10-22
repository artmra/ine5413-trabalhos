def dfs_visit(grafo, v, C, T, A, F, tempo, adaptado):
    C[v] = True
    tempo = tempo + 1
    T[v] = tempo
    if adaptado:
        print(v, ';', end = '')

    for u in grafo.vizinhos_saintes(v):
        if (not C[u[0]]):
            if adaptado:
                print(u[0], ';', end = '')
            A[u[0]] = v
            tempo = dfs_visit(grafo, u[0], C, T, A, F, tempo, adaptado)

    tempo = tempo + 1
    F[v] = tempo
    return tempo
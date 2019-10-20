def dfs_visit(grafo, v, C, T, A, F, tempo):
	C[v] = True
	tempo = tempo + 1
	T[v] = tempo
	
    for u in grafo.vizinhos_saintes(v):
        if (not C[u[0]]):
            A[u[0]] = v
            tempo = dfs_visit(grafo, u[0], C, T, A, F, tempo)
    
    tempo = tempo + 1
    F[v] = tempo
    return tempo
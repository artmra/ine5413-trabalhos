def relaxamento(grafo, u, v, D, A):
    neighbor_index = -1
    for i in range(len(grafo.vertices_[u])):
        if i[0] == v:
            neighbor_index = i
    if D[v] > D[u] + :
def W(G):
    D = list()
    [D.append([float('inf') for j in G.matrix]) for i in G.matrix]

    for i, row in enumerate(D):
        for j, _ in enumerate(row):
            if i == j:
                D[i][j] = 0
            
            elif G.matrix[i][j] != float('inf'):
                D[i][j] = G.matrix[i][j]

    return D

def floyd_warshall(G):
    D = list()
    D.append(W(G))

    for k, _ in enumerate(G.V):
        d = W(G)
        D.append(d)

        for u, __ in enumerate(G.V):
            for v, ___ in enumerate(G.V):
                D[k+1][u][v] = min(D[k][u][v], D[k][u][k] + D[k][k][v])

    return D[-1]

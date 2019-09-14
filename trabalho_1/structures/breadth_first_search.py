from grafo import Grafo
def bfs(grafo, origem):
    C = []
    D = []
    A = []
    for _ in grafo.vertices_:
        C.append(False)
        D.append(-1)
        A.append(None)
    C[origem - 1] = True
    D[origem - 1] = 0

    vertices_a_visitar = []
    vertices_a_visitar.append(origem - 1)

    while len(vertices_a_visitar) != 0:
        u = vertices_a_visitar.pop(0)
        print(grafo.vertices_[u][0])
        for v in grafo.vizinhos(u):
            if C[v[0]] == False:
                print(grafo.vertices_[v[0]][0])
                C[v[0]] = True
                D[v[0]] = D[u] + 1
                A[v[0]] = u
                vertices_a_visitar.append(v[0])
    
    return [D, A]
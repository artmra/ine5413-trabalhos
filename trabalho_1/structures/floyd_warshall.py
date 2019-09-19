import sys

def floyd_warshall(grafo):
    vertices = grafo.qtd_vertices()
    row, col = vertices, vertices

    D = [[0 for x in range(row)] for y in range(col)]

    # inicializando matrix com zero
    for i in range (vertices):
        for j in range (vertices):
            if i == j:
                D[i][j] = 0
            elif (grafo.ha_aresta(i,j)):
                D[i][j] = grafo.peso(i,j)
            else:
                D[i][j] = sys.maxsize
    
    for k in range (vertices):
        for i in range (vertices):
            for j in range (vertices):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    for i in range(row):
        print(i,":", end=" ")
        for j in range(col):
            print(D[i][j], end =" ")
        print("\n")
    

from grafo import Grafo
import sys

# Ncolunas * nLinhaAtual + nColunaAtual
# i*col + j
def floyd_warshall(grafo):
    D = []

    # print(grafo.peso(0, 134))
    # inicializando matrix com zero
    col = grafo.qtd_vertices()
    for i in range (col):
        for j in range (col):
            if i == j:
                D.append(0)
            elif (grafo.ha_aresta(i,j)):
                D.append(grafo.peso(i,j))
            else:
                # D.append(1000)
                D.append(sys.maxsize)

    for k in range (col):
        for i in range (col):
            for j in range (col):
                if (D[i*col + j] > D[i*col + k] + D[k*col + j]):
                    D[i*col + j] = D[i*col + k] + D[k*col + j]
                    # print("qualquer coisinha")
    print(D)

grafo = Grafo('facebook_santiago.net')
floyd_warshall(grafo)
    

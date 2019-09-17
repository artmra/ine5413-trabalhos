import math
from grafo import Grafo

def dijkstra (grafo, origem):
    D = []
    A = []
    C = []

    # configurando todos os vertices
    for _ in grafo.vertices_:
        D.append(math.inf)
        A.append(None)
        C.append(False)
    #configurando o vertice de origem
    D[origem] = 0

    # se todos os vertices foram visitados sai do laço
    while not all(C):
        dicio = dict([(i, D[i]) for i in range(len(grafo.vertices_)) if C[i] == False])
        u = getKeysByValue(dicio, min(dicio.values()))
        C[u] = True
        
        # parte do Cv = false
        for v in grafo.vizinhos(u):
            if C[v[0]] == False:
                if D[v[0]] > D[u] + v[1]:
                    print("sai de ", u, " e cheguei em ", v[0], "com peso ", (D[u] + v[1]))
                    D[v[0]] = D[u] + v[1]
                    A[v[0]] = u
            # endfor
    return [D, A]

def getKeysByValue(dictOfElements, valueToFind):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] == valueToFind:
            listOfKeys.append(item[0])
    return  listOfKeys[0]

grafo = Grafo('facebook_santiago.net')
dijkstra(grafo, 0)

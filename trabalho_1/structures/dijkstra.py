import math
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
                    # print("sai de ", u, " e cheguei em ", v[0], "com peso ", (D[u] + v[1]))
                    D[v[0]] = D[u] + v[1]
                    A[v[0]] = u
            # endfor
    # print("1:",D[2],A[2])
    vertices = grafo.qtd_vertices()
    row = vertices
    for i in range (row):
        # print(A[i])
        # print(A[A[1]])
    #     print(i,":", end=" ")
        # print(A[i])
        # A[A[i]] != 2 and
        j = i
        while (A[j] != None and A[j] != 2):
            print(A[A[j]], end =" ")
            j += 1
    #     print("\n")

    # print(origem)
    # print(D,A)
    return [D, A]

def getKeysByValue(dictOfElements, valueToFind):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] == valueToFind:
            listOfKeys.append(item[0])
    return  listOfKeys[0]

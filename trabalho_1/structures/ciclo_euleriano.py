def algoritmo_hierholzer(grafo):
    #
    # Dicionário que relaciona uma aresta do grafo ao valor False,
    #  uma vez que nenhuma foi visitada ainda.
    #
    C = dict([(e, False) for e in grafo.arestas()])
    #
    # Como os vértices estão ordenados por indice, escolhe-se
    # o primeiro de todos os vértices que ainda não foi visitado.
    #
    v = 0

    r, ciclo = buscar_subciclo_euleriano(grafo, v, C)

    if r == False:
        return [False, None]
    else:
        for i in C.values():
            if i == False:
                return [False, None]
        return [True, ciclo]


def buscar_subciclo_euleriano(grafo, v, C):
    #
    # Inicia o ciclo no vértice v.
    #
    ciclo = [v]
    t = v

    #
    # Enquanto não retorna ao vértice inicial as visitas
    # continuam sendo realizadas.
    #
    while True:
        todas_arestas_visitadas = True
        for u in grafo.vizinhos(v):
            if (v, u[0]) in C.keys():
                if C[(v, u[0])] == False:
                    todas_arestas_visitadas = False
                    C[(v, u[0])] = True
                    # print ("saiu de", v, "para", u[0])
                    v = u[0]
                    break
            elif (u[0], v) in C.keys():
                if C[(u[0], v)] == False:
                    todas_arestas_visitadas = False
                    C[(u[0], v)] = True
                    # print ("saiu de", v, "para", u[0])
                    v = u[0]
                    break
        if todas_arestas_visitadas == True:
            return [False, None]
        ciclo.append(v)
        if v == t:
            break
    
    #
    # Re-executa o algoritmo de buscar_subciclo_euleriano() para
    # toda aresta que ainda não foi percorrida.
    #
    if not all(C.values()):
        #
        # Coloca o indice de todos os elementos não visitados no
        # array x_, e depois pega o primeiro elemento para ser o x.
        #
        x_ = []
        for i in C.keys():
            if C[i] == False:
                if not i[0] in x_:
                    x_.append(i[0])
                elif not i[1] in x_:
                    x_.append(i[1])
        x = x_[0]

        #
        # Chama o algoritmo para encontrar outros subciclos que podem
        # pertencer ao ciclo que está tentando se encontrar partindo de v.
        #
        r_, ciclo_ = buscar_subciclo_euleriano(grafo, x, C)

        if r_ == False:
            return [False, None]
        
        #
        # Tenta inserir o ciclo encontrado no ciclo já existente.
        #
        conseguiu_inserir = False
        if x in ciclo:
            ciclo = [*ciclo[:ciclo.index(x) - 1], *ciclo_, *ciclo[ciclo.index(x) + 1:]]
            conseguiu_inserir = True
        if conseguiu_inserir == False:
            return [False, None]
    return [True, ciclo]

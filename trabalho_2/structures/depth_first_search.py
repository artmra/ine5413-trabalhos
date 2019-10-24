import sys
from .depth_first_search_visit import dfs_visit
def dfs(grafo):
    V = grafo.vertices_
    C = dict([(i, False) for i,v in enumerate(grafo.vertices_)])
    T = dict([(i, sys.maxsize) for i,v in enumerate(grafo.vertices_)])
    F = dict([(i, sys.maxsize) for i,v in enumerate(grafo.vertices_)])
    A = dict([(i, None) for i,v in enumerate(grafo.vertices_)])
    tempo = 0

    for v in range(len(V)):
        if (not C[v]):
            tempo, no_used = dfs_visit(grafo, v, C, T, A, F, tempo, [], False)
    
    return [C, T, A, F]

def dfs_adaptado(grafo, v_ordered_by_f):
    C = dict([(i, False) for i,v in enumerate(grafo.vertices_)])
    T = dict([(i, sys.maxsize) for i,v in enumerate(grafo.vertices_)])
    F = dict([(i, sys.maxsize) for i,v in enumerate(grafo.vertices_)])
    A = dict([(i, None) for i,v in enumerate(grafo.vertices_)])
    tempo = 0

    for v in v_ordered_by_f:
        if (not C[v]):
            tempo, cfc = dfs_visit(grafo, v, C, T, A, F, tempo, [], True)
            string = cfc.pop(0)
            for  v in cfc:
                string += ','
                string += v
            print((string.replace('\n', '')))
    
    return [C, T, A, F]
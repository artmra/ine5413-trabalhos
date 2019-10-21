import sys
from .depth_first_search_visit import dfs_visit
def dfs(grafo):
    V = grafo.vertices_
    # configurando todos os vértices
    C = dict([(i, False) for i,v in enumerate(grafo.vertices_)])
    T = dict([(i, sys.maxsize) for i,v in enumerate(grafo.vertices_)])
    F = dict([(i, sys.maxsize) for i,v in enumerate(grafo.vertices_)])
    A = dict([(i, None) for i,v in enumerate(grafo.vertices_)])
    tempo = 0
    # configurando o tempo de início
    for u in range(len(V)):
    	if (not C[u]):
    		# DFS-Visit é executado
    		tempo = dfs_visit(grafo, u, C, T, A, F, tempo)
    return [C, T, A, F]

def dfs_adaptado(grafo, v_ordered_by_f):
    V = grafo.vertices_
    # configurando todos os vértices
    C = dict([(i, False) for i,v in enumerate(grafo.vertices_)])
    T = dict([(i, sys.maxsize) for i,v in enumerate(grafo.vertices_)])
    F = dict([(i, sys.maxsize) for i,v in enumerate(grafo.vertices_)])
    A = dict([(i, None) for i,v in enumerate(grafo.vertices_)])
    tempo = 0
    # configurando o tempo de início
    for v in v_ordered_by_f:
        if (not C[v]):
            # DFS-Visit é executado
            tempo = dfs_visit(grafo, u, C, T, A, F, tempo)
    return [C, T, A, F]
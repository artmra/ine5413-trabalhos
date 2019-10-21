import math
from .dfs_visit_ot import dfs_visit_ot
def ordenacao_topologica (grafo):
    C = []
    T = []
    F = []
    # Configurando todos os vertices
    for _ in grafo.vertices_:
        C.append(False)
        T.append(math.inf)
        F.append(math.inf)
    # Configurando tempo de inicio
    tempo = 0
    #Criando lista com os vertices ordenados topologicamente
    lista = []
    for u in range (len(grafo.vertices_)):
        if (C[u] == False):
            dfs_visit_ot(grafo, u, C, T, F, tempo, lista)
    return lista
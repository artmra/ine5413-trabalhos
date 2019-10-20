import sys
def dfs-visit(grafo, v, C, T, A, F, tempo):
	C[v] = True
	tempo = tempo + 1
	T[v] = tempo
	for u in 
def dfs(grafo):
    V = grafo.vertices_
    # configurando todos os vértices
    C = []
    T = []
    F = []
    A = []
    for _ in V:
    	c.append(False)
    	T.append(sys.maxsize)
    	F.append(sys.maxsize)
    	A.append(None)
    tempo = 0
    # configurando o tempo de início
    for u in range(len(V)):
    	if C[u] == False:
    		# DFS-Visit é executado
    		dfs_visit(grafo, u, T, A, F, tempo)
    return (C, T, A, F)
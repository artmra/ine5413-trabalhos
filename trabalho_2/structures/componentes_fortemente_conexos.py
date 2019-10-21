import copy
from .depth_first_search import dfs, dfs_adaptado
def cfc(grafo):
	C, T, A, F = dfs(grafo)

	grafo_t = copy.deepcopy(grafo)
	grafo_t.trasnpor_grafo()

	Ct, Tt, At, Ft = dfs_adaptado(grafo)

	return At
import copy
from .depth_first_search import dfs, dfs_adaptado
def cfc(grafo):
	C, T, A, F = dfs(grafo)

	grafo_t = copy.deepcopy(grafo)
	grafo_t.transpor_grafo()

	v_ordered_by_f = [i for i in range(len(grafo.vertices_))]
	v_ordered_by_f.sort(key = lambda u : F[u], reverse = True)

	Ct, Tt, At, Ft = dfs_adaptado(grafo_t, v_ordered_by_f)

	return At
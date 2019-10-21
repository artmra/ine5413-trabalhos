import copy
from .depth_first_search import dfs, dfs_adaptado
def cfc(grafo):
	C, T, A, F = dfs(grafo)

	grafo_t = copy.deepcopy(grafo)
	grafo_t.transpor_grafo()

	v_ordered_by_f = [i for i in range(len(grafo.vertices_))]
	# print('antes  do order: \n', v_ordered_by_f)
	v_ordered_by_f.sort(key = lambda u : F[u], reverse = True)
	# print('depois do order: \n', v_ordered_by_f)

	Ct, Tt, At, Ft = dfs_adaptado(grafo, v_ordered_by_f)

	# print (At.values())
	return At
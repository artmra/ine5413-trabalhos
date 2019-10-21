from structures.grafo import Grafo
from structures.componentes_fortemente_conexos import cfc

grafo = Grafo('facebook_santiago.net')

print("Quantidade de vertices : ",grafo.qtd_vertices())
print("Quantidade de arestas", grafo.qtd_arestas())
cfc(grafo)
# print("Digite o vertice para descobrir o seu grau:")
# u = int(input())
# print("Grau do vertice ",u,": ", grafo.grau(u))
# print("Digite o vertice para descobrir os seus vizinhos:")
# u = int(input())
# #Tentar alterar isso
# print("Vizinhos: ",grafo.vizinhos(u))
# print("Digite os dois vertices para saber se ha uma aresta:")
# u = int(input())
# v = int(input())
# print(grafo.ha_aresta(u,v))
# print("Digite dois vertices para saber o peso de sua ligacao")
# u = int(input())
# v = int(input())
# print("Peso entre ",u, " e ",v, " é :",grafo.peso(u,v))

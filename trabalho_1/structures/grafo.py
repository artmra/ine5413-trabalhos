import sys

class Grafo:
    
    def __init__(self, arquivo):
        self.vertices_ = []
        self.n_arestas_ = 0
        a = open(arquivo, 'r')
        for i in a:
            linha = i.split()
            if (linha[0] == '*vertices'):
                for j in range(int(linha[1])):
                    _ , rotulo = a.readline().split(' ', 1)
                    # 
                    # Adiciona um vértice(lista de 2 elementos, sendo o primeiro o rótulo e o segundo os vizinhos) ao grafo
                    #
                    self.vertices_.append([rotulo, []])
            if (linha[0] == '*edges'):
                for k in a:
                    v, u, peso = k.split()
                    #
                    # Adiciona u à lista de vizinhos de v,  além do peso da aresta que os liga
                    #
                    self.vertices_[int(v) - 1][1].append([int(u)-1, float(peso)])
                    #
                    # Adiciona v à lista de vizinhos de u, além do peso da aresta que os liga
                    #
                    self.vertices_[int(u) - 1][1].append([int(v)-1, float(peso)])
                    #
                    # Incrementa o número de arestas
                    #
                    self.n_arestas_ = self.n_arestas_ + 1
    
    #
    # Retorna todos os vértices presentes no grafo.
    #
    def qtd_vertices(self):
    	return len(self.vertices_)
    #
    # Retorna a quantidade total de arestas do grafo.
    #
    def qtd_arestas(self):
    	return self.n_arestas_
    #
    # Retorna o grau de um grafo de indice v.
    # ****O ÍNDICE DIZ RESPEITO À UMA LISTA QUE COMEÇOU A SER ORDENADA DO 0****
    #
    def grau(self, v):
    	return len(self.vertices_[v][1])
    #
    # Retorna o rótulo de um vértice no indice v do grafo.
    # ****O ÍNDICE DIZ RESPEITO À UMA LISTA QUE COMEÇOU A SER ORDENADA DO 0****
    #
    def rotulo(self, v):
    	return self.vertices_[v][0]
    #
    # Retorna todos os vizinhos de um vértice no indice v do grafo.
    # ****O ÍNDICE DIZ RESPEITO À UMA LISTA QUE COMEÇOU A SER ORDENADA DO 0****
    #
    def vizinhos(self, v):
    	return self.vertices_[v][1]
    
    #
    # Se existir uma aresta {grafo.vertices_[u], grafo.vertices_[v]} no grafo 
    # retorna True, senão False.
    # ****O ÍNDICE DIZ RESPEITO À UMA LISTA QUE COMEÇOU A SER ORDENADA DO 0****
    #
    def ha_aresta(self, u, v):
        for i in self.vertices_[u]:
            if (v) == i[0]:
                return True
        return False
    
    #
    # Se existir uma aresta {grafo.vertices_[u], grafo.vertices_[v]} no grafo
    # retorna o peso da mesma, senão retorna o maior valor inteiro possível. 
    # ****O ÍNDICE DIZ RESPEITO À UMA LISTA QUE COMEÇOU A SER ORDENADA DO 0****
    #
    def peso(self, u, v):
        for i in self.vertices_[u]:
            if (v) == i[0]:
                return i[1]
        return sys.maxsize

    def arestas(self):
        arestas = []
        for i in range(len(self.vertices_)):
            for v in self.vertices_[i][1]:
                if (i < v[0]):
                    if not ((i, v[0]) in arestas):
                    # if (arestas.count((i, v[0])) == 0):
                        arestas.append((i, v[0]))
                else:
                    if not ((v[0], i) in arestas):
                    # if (arestas.count((v[0], i)) == 0):
                        arestas.append((v[0], i))
        # for i in arestas:
        #     print(i)
        return arestas
# grafo = Grafo('facebook_santiago.net')
# print(grafo.arestas())
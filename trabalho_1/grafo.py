import sys

class Grafo:
    
    def __init__(self, arquivo):
        self.vertices_ = []
        self.rotulos_ = []
        self.n_arestas_ = 0
        a = open(arquivo, 'r')
        for i in a:
            linha = i.split()
            if (linha[0] == '*vertices'):
                for j in range(int(linha[1])):
                    _ , rotulo = a.readline().split(' ', 1)
                    self.vertices_.append([])
                    self.rotulos_.append(rotulo.rstrip())
            if (linha[0] == '*edges'):
                for k in a:
                    v, u, peso = k.split()
                    self.vertices_[int(v) - 1].append([int(u)-1, float(peso)])
                    self.vertices_[int(u) - 1].append([int(v)-1, float(peso)])
                    self.n_arestas_ = self.n_arestas_ + 1
    
    def qtd_vertices(self):
    	return len(self.vertices_)
    
    def qtd_arestas(self):
    	return self.n_arestas_
    
    def grau(self, v):
    	return len(self.vertices_[v - 1])
    
    def rotulo(self, v):
    	return self.rotulos_[v - 1]
    
    def vizinhos(self, v):
    	return self.vertices_[v - 1]
    
    def ha_aresta(self, u, v):
        for i in self.vertices_[u]:
            if (v - 1) == i[0]:
                return True
        return False
    
    def peso(self, u, v):
        for i in self.vertices_[u]:
            if (v - 1) == i[0]:
                return i[1]
        return sys.maxsize


grafo = Grafo('facebook_santiago.net')


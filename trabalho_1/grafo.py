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
                    indice, rotulo = a.readline().split(' ', 1)
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
    	return len(self.vertices_[v])
    
    def rotulo(self, v):
    	return self.rotulos_[v]
    
    def vizinhos(self, v):
    	return self.vertices_[v]
    
    def ha_aresta(self, u, v):
        return True if u.ah_aresta(v) > (-1) else False
    
    def peso(self, u, v):
        return u.ah_aresta(v) if u.ah_aresta(v) > (-1) else sys.maxsize


grafo = Grafo('facebook_santiago.net')


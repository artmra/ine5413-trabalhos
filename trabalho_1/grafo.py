import sys
class Vertice:

    def __init__(self, numero, rotulo):
        self.numero_ = numero
        self.rotulo_ = rotulo
        self.vizinhos_ = []

    def grau(self):
        return len(self.vizinhos_)
    
    def rotulo(self):
        return self.rotulo_

    def vizinhos(self):
        return self.vizinhos_
    
    def ha_aresta(self, v):
        for i in self.vizinhos_:
            if i[0] == v:
                return i[1]
        return -1

    def adicionar_vizinho(self, v, peso):
        self.vizinhos_.append([v, peso])

class Grafo:
    
    def __init__(self, arquivo):
        self.vertices_ = []
        self.n_arestas_ = 0
        self.ler(arquivo)
    
    def qtd_vertices(self):
    	return len(self.vertices_)
    
    def qtd_arestas(self):
    	return self.n_arestas
    
    def grau(self, v):
    	return v.grau()
    
    def rotulo(self, v):
    	return v.rotulo()
    
    def vizinhos(self, v):
    	return v.vizinhos()
    
    def ha_aresta(self, u, v):
        return True if u.ah_aresta(v) > (-1) else False
    
    def peso(self, u, v):
        return u.ah_aresta(v) if u.ah_aresta(v) > (-1) else sys.maxsize
    
    def ler(self, arquivo):
        a = open(arquivo, 'r')
        for i in a:
            print (10000)
            linha = i.split()
            if (linha[0] == '*vertices'):
                for j in range(int(linha[1])):
                    info1, info2 = a.readline().split(' ', 1)
                    self.vertices_.append(Vertice(int(info1), info2.rstrip()))
            if (linha[0] == '*edges'):
                for k in a:
                    v, u, peso = k.split()
                    self.vertices_[int(v) - 1].adicionar_vizinho(u, float(peso))
                    self.vertices_[int(u) - 1].adicionar_vizinho(v, float(peso))
                    self.n_arestas_ = self.n_arestas_ + 1
        # print(self.vertices)

grafo = Grafo('facebook_santiago.net')


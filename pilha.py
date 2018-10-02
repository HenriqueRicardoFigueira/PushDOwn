class Pilha:
    def __init__(self,estadoInicial, palavraInicial):
        self.pilha = []
        self.pilha.append("Z")
        self.estadoInicial = estadoInicial
        self.estado = estadoInicial
        self.palavra = palavraInicial
    
    def empilha(self, letra):
        self.pilha.append(letra)

    def desempilha(self):
        if self.vazia() == False :
            self.pilha.pop()

    def vazia(self):
        if len(self.pilha) == 0:
            return True
        else:
            return False

    def olhaTopo(self):
        if(self.vazia() != True):
            return self.pilha[len(self.pilha)-1]
        else: return []

    def retorna_estado(self):
        return str(self.estado)
        
    def mudar_estado(self, novoEstado):
        self.estado = novoEstado

    def retorna_letra(self):
        if (len(self.palavra)>0):
            return self.palavra[0]
        else: return []
    
    def consome_palavra(self):
        if len(self.palavra) > 0:
            self.palavra = self.palavra[1:]
            return True
        else:
            return False

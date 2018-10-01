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
        return self.pilha[len(self.pilha)-1]

    def printPilha(self):
        if(len(self.pilha ) != 0):
            for item in self.pilha:
                print(item)
    
    def retorna_pilha(self):
        return ''.join(self.pilha)

    def retorna_estado(self):
        return str(self.estado)
        
    def mudar_estado(self, novoEstado):
        self.consome_palavra()
        self.estado = novoEstado

    def retorna_tamanho(self):
        return len(self.pilha)
    
    def consome_palavra(self):
        if len(self.palavra) != 0:
            self.palavra = self.palavra[1:]
            return True
        else:
            return False

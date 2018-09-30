class Pilha:
    def __init__(self,estadoInicial):
        self.pilha = []
        self.pilha.append("Z")
        self.estadoInicial = estadoInicial
        self.estado = estadoInicial
    
    def empilha(self, palavra):
        self.pilha.append(palavra)

    def desempilha(self):
        if self.vazia() == False:
            self.pilha.pop()

    def vazia(self):
        tam = len(self.pilha)-1
        if self.pilha[tam] == "Z" or tam == 0:
            return True
        else:
            return False

    def olhaTopo(self):
        return self.pilha[len(self.pilha)]

    def printPilha(self):
        tam = len(self.pilha)-1
        while(tam >= 0):
            print(str(self.pilha[tam]))
            tam-=1
        print("FIM DA PILHA")
    
    def retorna_pilha(self):
        return ''.join(self.pilha)

    def retorna_estado(self):
        return str(self.estado)
        
    def mudar_estado(self, novoEstado):
        self.estado = novoEstado


    def retorna_tamanho(self):
        return len(self.pilha)

    def verifica_estadoInicial(self, fita):
		if str(self.retorna_estado()) == self.estadoInicial:
			return  True
		else:
			return False

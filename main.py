#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, random
from automatoPilha import automatoPilha

class Main:

    #tudo no fim acho que vira aut_pilha
    def __main__(self):

        #cria a aut_pilha e a Pilha Inicial
        aut_pilha = automatoPilha(sys.argv)

        for i in range(0,100):

            novasPilhas = []

            if(len(aut_pilha.pilhas) == 0):
                print(-1)
                exit(1)

            pilhas = aut_pilha.pilhas
            for pilha in pilhas:
                
                if( ( ((pilha.retorna_estado() in aut_pilha.estadoFinal ) or aut_pilha.estadoFinal == ['']) 
                    and 
                    ((len(pilha.palavra) == 0) and (pilha.vazia())) )
                    #fim priemira exp
                    or 
                    #segunda exp
                    (len(pilha.palavra)== 0 and (pilha.retorna_estado() in aut_pilha.estadoFinal)) ):

                    print('0\n')
                    print("DESC INST. _________________________")
                    print("Pilha: "+str(pilha.pilha))
                    print("Palavra: "+str(pilha.palavra))
                    print("Estado: "+str(pilha.retorna_estado()))
                    exit(1)

                ret = aut_pilha.transicao(pilha)

                if (len(ret) > 0):
                    novasPilhas+=ret
                
                elif(len(ret) == 0 and len(aut_pilha.pilhas) ==1):
                    print('-1\n')
                    print("DESC INST. _________________________")
                    print("Pilha: "+str(pilha.pilha))
                    print("Palavra: "+str(pilha.palavra))
                    print("Estado: "+str(pilha.retorna_estado()))
                    exit(1)
                    
                aut_pilha.remove_pilha(pilha)
                
            if(len(novasPilhas)>0):
                for newPilha in novasPilhas:
                    aut_pilha.adiciona_pilha(newPilha)

        
        #mostra descrição instantânea
        print("COMPUTAÇÃO INTERROMPIDA")
        print("PILHAS:_____________________________")
        for pilha in aut_pilha.pilhas:
            print("Pilha: "+str(pilha.pilha))
            print("Palavra: "+str(pilha.palavra))
            print("Estado: "+str(pilha.retorna_estado()))
            print('---------------')
        print("FIM_____________________________")
            

Main().__main__()

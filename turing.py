#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, random
from maquina import Maquina

class Turing:

    #tudo no fim acho que vira maquina
    def __main__(self):

        #cria a Maquina e a Fita Inicial
        maquina = Maquina(sys.argv)

        for i in range(0,100):

            novasPilhas = []
            print('execução: '+str(i+1)+"_________________")
            print(len(maquina.pilhas))
            for maq in maquina.pilhas:
                print(maq.retorna_estado())
                print(maq.palavra)
                print(maq.pilha)
            print("FIM VELHAS FITAS")

            if(len(maquina.pilhas) == 0):
                print("Palavra Rejeitada")
                exit(1)

            #for x in range(0,len(maquina.pilhas)):
            for pilha in maquina.pilhas:
                #pilha = maquina.pilhas[x-1]
                ret = maquina.transicao(pilha)
            
                if((pilha.retorna_estado() in maquina.estadoFinal )and (len(pilha.palavra) == 0) and (pilha.vazia())):
                    print(0)
                    print("ACEITEIIIIIIIIIIII")
                    exit(1)

                if type(ret) is list and (len(ret) > 0):
                    novasPilhas+=ret
                

            if(len(novasPilhas)>0):
                for newPilha in novasPilhas:
                    maquina.adiciona_pilha(newPilha)
                    

            print("NOVAS FITAS")
            for pilha in maquina.pilhas:
                print(pilha.retorna_estado())
                print(maquina.estadoFinal)
                print(pilha.vazia())
                print(pilha.palavra)
                print(pilha.pilha)
                if(((pilha.retorna_estado() in maquina.estadoFinal ) or maquina.estadoFinal == ['']) and (len(pilha.palavra) == 0) and (pilha.vazia())):
                    print(0)
                    print("ACEITEIIIIIIIIIIII")
                    exit(1)
                print(pilha.retorna_estado())
                print(pilha.palavra)
                print(pilha.pilha)
            print('Fim execução: '+str(i+1)+"_________________")
            

Turing().__main__()

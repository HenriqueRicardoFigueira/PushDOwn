#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, random
from maquina import Maquina

class Turing:

    #tudo no fim acho que vira maquina
    def __main__(self):

        #cria a Maquina e a Fita Inicial
        maquina = Maquina(sys.argv)
        while(True):
            #aqui de debbug tb

            novasPilhas = []

            #print(len(maquina.pilhas))
            for pilha in maquina.pilhas:
                ret = maquina.transicao(pilha)

                print("entrei")
                print(pilha.pilha)
                print(pilha.palavra)
                print("topo: "+str(pilha.olhaTopo()))
                print(pilha.retorna_estado())
                print(maquina.transicoes[pilha.retorna_estado()])
            
                if(pilha.vazia() and len(pilha.palavra) == 0) or (pilha.retorna_estado() in maquina.estadoFinal and len(pilha.palavra) == 0):
                    print(0)
                    exit(1)

                if type(ret) is list:
                    novasPilhas+=ret

            if(novasPilhas != None):
                for newPilha in novasPilhas:
                    maquina.adiciona_pilha(newPilha)

Turing().__main__()

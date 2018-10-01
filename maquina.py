#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, copy, random
from pilha import Pilha

class Maquina:
	def __init__(self, dados):
		#Abre o Arquivo
		arq = open(dados[1],'r')

		self.palavraInicial = list(dados[2])

		self.linhasArq = arq.read().splitlines()

		#variaveis
		self.alfaEntrada = self.linhasArq[0].split(" ")
		self.alfaPilha = self.linhasArq[1].split(" ")
		self.branco = self.linhasArq[2]
		self.estados = self.linhasArq[4].split(" ")
		self.estadoInicial = self.linhasArq[5]
		self.estadoFinal = self.linhasArq[6].split(" ")

		#self.tamanhoFita = int(self.linhasArq[6])
		self.transicoes = {}
		self.pilhas = []

		#inicializa maquina
		self.carrega_maquinaArquivo()
		#self.cria_fitaInicial(self.linhasArq[4].strip())
		self.pilha = Pilha(self.estadoInicial, self.palavraInicial)
		self.pilhas.append(self.pilha)

	def carrega_maquinaArquivo(self):
		#COMEÇA QUEBRA DE ARQUIVO (modificar essa parte pra começar a indexar por hash e não por posição ""COMFIRMAR"")
		self.transicoes = self.grava_transicoesEstadosDestino(self.grava_transicoesEstadosOrigem())

	def grava_transicoesEstadosOrigem(self):
		transicoesArq = []
		transicoesOrigem = {}

		for k in self.linhasArq[7:]:
			transicoesArq.append(k)

		for s in self.estados:
			aux2 = []
			for t in transicoesArq:
				aux = t.split(" ")
				if s == aux[0]:
					aux2.append(aux[1:])
			transicoesOrigem[s]=[aux2]
	
		return transicoesOrigem

	def grava_transicoesEstadosDestino(self, transicoesOrigem):
		transicoesDestino= {}
		for estado in self.estados:
			transiDest = {}
			
			for transicao in transicoesOrigem[estado][0]:
				if transicao[0] in transiDest:
					estadoDest = (transicao[1],transicao[2],list(transicao[3]))
					transiDest[transicao[0]].append(estadoDest)
				else:
					estadoDest = (transicao[1],transicao[2],list(transicao[3]))
					transiDest[transicao[0]]= [estadoDest]

			transicoesDestino[estado] = transiDest

		return transicoesDestino

	def retorna_transicoesPossiveis(self, iniState):
		if(iniState not in self.transicoes):
			return None
		return self.transicoes[iniState]
	
	def adiciona_pilha(self,pilha):
		self.pilhas.append(pilha)

	def remove_pilha(self,pilha):
		self.pilhas.remove(pilha)
	
	def clonar_unicaPilha(self,pilha):
		return copy.deepcopy(pilha)
	
	def clonar_todasPilhas(self):
		return copy.deepcopy(self.pilhas)

	def transicao(self, pilha): #colocar essa função dentro da maquina também
		stateTransitions = self.transicoes[pilha.retorna_estado()]
		try:
			letra = self.pilha.palavra[0]
		except:
			letra = self.branco

		if letra in stateTransitions:
			transi = stateTransitions[letra]

			if len(transi) == 0:
				if(len(self.pilhas)>1):
					print("\nNão há Estados Possíveis Para Pilha "+str(self.pilhas.index(pilha))+'.')
					return 1

				else:
					print("\nPalavra Rejeitada")
					exit(1)

			elif len(transi) == 1:
				for tr in transi[0][0]:
					topo = pilha.olhaTopo()

					if(tr == topo):
						pilha.desempilha()

					elif(tr != self.branco):
						print("Palavra Rejeitada")						
						return exit(1)

				for tr in reversed(transi[0][2]):
					if(tr != self.branco):
						pilha.empilha(tr)

				pilha.mudar_estado(transi[0][1])
				
				return None 

			elif len(transi) > 1:
				novasPilhas = []
				topo = pilha.olhaTopo()

				for tran in transi:
					for tr in tran:
						pilha2 = self.clonar_unicaPilha(pilha)
						
						if(tr[0] == topo):
							pilha2.desempilha()
						
						elif(tr[0] != self.branco):
							print("Palavra Rejeitada")
							return exit(1)

						if(tr[2] != self.branco):	
							pilha2.empilha(tr[2])

						pilha2.mudar_estado(tr[1])
						novasPilhas.append(pilha2)

				self.remove_pilha(pilha)
				return novasPilhas

			else:
				return None
			'''
		else:
			if(len(self.pilhas)>1):
				print("\nNão há Estados Possíveis Para fita "+str(self.pilhas.index(pilha))+'.')
				return 1

			else:
				print("\nPalavra Rejeitada.")
				exit(1)'''

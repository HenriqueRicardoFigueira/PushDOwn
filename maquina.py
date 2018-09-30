#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, copy, random
from fita import Fita
from pilha import Pilha

class Maquina:
	def __init__(self, dados):
		'''#Conteudo da Fita
		self.contentTape = []
		for x in range(2,(len(dados))):
			aux = dados[x]
			self.contentTape.append(aux)'''

		#Abre o Arquivo
		arq = open(dados[0],'r')

		self.linhasArq = arq.read().splitlines()

		#variaveis
		self.alfaEntrada = self.linhasArq[0].split(" ")
		self.alfaPilha = self.linhasArq[1].split(" ")
		self.branco = self.linhasArq[2]
		self.estados = self.linhasArq[4].split(" ")
		self.estadoInicial = self.linhasArq[5].split("")
		self.estadoFinal = self.linhasArq[6].split(" ")
		#self.tamanhoFita = int(self.linhasArq[6])
		self.transicoes = {}
		self.pilhas = []

		#inicializa maquina
		self.carrega_maquinaArquivo()
		#self.cria_fitaInicial(self.linhasArq[4].strip())
		self.pilha = Pilha(self.estadoInicial)


	"""
		def cria_fitaInicial(self, estadoInicial):
		self.adiciona_fita(Fita(self.contentTape, self.alfaEntrada, self.alfaFita, self.branco, estadoInicial))
	
	"""
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
				if transicao[1] in transiDest:
					estadoDest = (transicao[0],transicao[2],transicao[3])
					transiDest[transicao[1]].append(estadoDest)
				else:
					estadoDest = (transicao[0],transicao[2],transicao[3])
					transiDest[transicao[1]]= [estadoDest]

			transicoesDestino[estado] = transiDest

		return transicoesDestino

	def verifica_estadoFinal(self, pilha):
		if pilha.retorna_estado() in self.estadoFinal:
			print "\nResultado: Palavra Aceita."
			return True
		else:
			return False

	def retorna_transicoesPossiveis(self, iniState):
		if(iniState not in self.transicoes):
			return None
		return self.transicoes[iniState]

	"""def print_fitas(self):
		print("\nQuantidade de Fitas: " + str(len(self.fitas))+"\n")
		for fita in self.fitas:
			print("    Fita: "+str(self.fitas.index(fita)))
			sys.stdout.write("    Posição da Cabeça  : ")
			sys.stdout.write(' '*fita.posicao_cabeca)
			print('|')
			print("    Conteudo Atual Fita: "+fita.retorna_fita())
			print("    Estado Atual       : "+str(fita.retorna_estado()))
			print("    Estados Possíves   : "+str(self.retorna_transicoesPossiveis(fita.retorna_estado())))
			sys.stdout.write("    ")
			print("_"* 146)
		print("_"* 150)
	"""
	
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
		topo = self.pilha.olhaTopo
		if topo in stateTransitions:
			transi = stateTransitions[topo]
			if len(transi) == 0:
				if(len(self.pilhas)>1):
					print("\nNão há Estados Possíveis Para Pilha "+str(self.pilhas.index(pilha))+'.')
					return 1

				else:
					print("\nPalavra Rejeitada")
					exit(1)

			elif len(transi) == 1:
				pilha.empilha(transi[0][1])
				pilha.mudar_estado(transi[0][0])

				return None 

			elif len(transi) > 1:
				novasPilhas = []
				for i in transi:
					pilha2 = self.clonar_unicaPilha(pilha)
					pilha2.empilha(i[1])
					#pilha2.move_cabeca(i[2])
					pilha.mudar_estado(i[0])
					novasPilhas.append(pilha2)
					#cria a copia de uam fita, movimenta para as possiveis transações e anexa a fita a uma nova lista removendo a si mesma da lista anterior
					# a lista anterior recebe as novas fitas menos a original

				self.remove_pilha(pilha)
				return novasPilhas

			else:
				return None
		else:
			if(len(self.pilhas)>1):
				print("\nNão há Estados Possíveis Para fita "+str(self.pilhas.index(pilha))+'.')
				return 1

			else:
				print("\nPalavra Rejeitada.")
				exit(1)

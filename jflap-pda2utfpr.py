# Linha 1: alfabeto de entrada
# Linha 2: alfabeto da pilha
# Linha 3: simbolo que representa epsilon (padrão: E)
# Linha 4: simbolo inicial da pilha (padrao: Z)
# Lista 5: conjunto de estados
# Linha 6: estado inicial
# Linha 7: conjunto de estados de aceitacao
# Linhas 8 em diante: transicoes, uma por linha, no formato estado atual, simbolo atual da palavra, simbolo do topo da pilha, novo estado, novos simbolos a serem empilhados (topo a esquerda, base a direita)

from xml.etree import ElementTree as ET
import csv
import sys

class Transition(object):
	def __init__(self):
		self.currentState = None
		self.currentWordSymbol = None
		self.currentStackTopSymbol = None
		self.newState = None
		self.newStackTopSymbol = None

	def __lt__(self, other):
		if self.currentState != other.currentState:
			return self.currentState < other.currentState
		if self.currentWordSymbol != other.currentWordSymbol:
			return self.currentWordSymbol < other.currentWordSymbol
		if self.currentStackTopSymbol != other.currentStackTopSymbol:
			return self.currentStackTopSymbol < other.currentStackTopSymbol
		if self.newState != other.newState:
			return self.newState < other.newState 
		if self.newStackTopSymbol != other.newStackTopSymbol:
			return self.newStackTopSymbol < other.newStackTopSymbol

class Jflap2Utfpr(object):
	def __init__(self):
		self.state_id_to_name = {}
		self.inputAlphabet = set()
		self.stackAlphabet = set()
		self.states = set()
		self.initialStates = set()
		self.acceptingStates = set()
		self.transitions = []
		self.blankSymbol = "E"
		self.stackInitialSymbol = "Z"

	def convert(self, inputFile, outputFile, blankSymbol = "E", inputAlphabet = None, stackAlphabet = None, states = None):
		self.blankSymbol = blankSymbol
		if inputAlphabet is not None:
			self.inputAlphabet = inputAlphabet
		if stackAlphabet is not None:
			self.stackAlphabet = stackAlphabet
		if states is not None:
			self.states = states

		xmldoc = ET.parse(inputFile)
		root = xmldoc.getroot()
		tm = root.find('automaton')

		for s in tm.findall('state'):
			state_id = s.attrib['id']
			state_name = s.attrib['name']
			self.state_id_to_name[state_id] = state_name
			self.states.add(state_name)
			if s.find('initial') is not None:
				self.initialStates.add(state_name)
			if s.find('final') is not None:
				self.acceptingStates.add(state_name)

		# Discover stack alphabet
		if stackAlphabet is None:
			self.stackAlphabet.add(self.stackInitialSymbol)
			for t in tm.findall('transition'):
				popSymbol = t.find('pop').text
				if popSymbol is not None and len(popSymbol.strip()) > 0:
					self.stackAlphabet.add(popSymbol)
				pushSymbol = t.find('push').text
				if pushSymbol is not None and len(pushSymbol.strip()) > 0:
					self.stackAlphabet.add(pushSymbol)
	
		# Discover input alphabet:
		if inputAlphabet is None:
			for t in tm.findall('transition'):
				if t.find('read').text is not None:
					self.inputAlphabet.add(t.find('read').text)

		# Use a symbol to represent epsilon that is not used by the input or stack alphabets
		fullAlphabet = set()
		fullAlphabet.union(self.inputAlphabet)
		fullAlphabet.union(self.stackAlphabet)
		for s in fullAlphabet:
			if s == blankSymbol:
				oldBlankSymbol = blankSymbol
				for c in ascii_uppercase:
					if c not in fullAlphabet:
						blankSymbol = c
						break
				print("Simbolo escolhida para representar branco (" + oldBlankSymbol + ") foi utilizado para outros fins no automato. Simbolo para branco foi substituido por " + blankSymbol + ".")
		self.blankSymbol = blankSymbol
		
		for t in tm.findall('transition'):
			transition = Transition()
			self.transitions.append(transition)
			transition.currentState = self.state_id_to_name[t.find('from').text]
			if t.find('read').text is not None:
				transition.currentWordSymbol = t.find('read').text
			else:
				transition.currentWordSymbol = self.blankSymbol
			if t.find('pop').text is not None:
				transition.currentStackTopSymbol = t.find('pop').text
			else:
				transition.currentStackTopSymbol = self.blankSymbol
			transition.newState = self.state_id_to_name[t.find('to').text]
			if t.find('push').text is not None:
				symbols = t.find('push').text
				transition.newStackTopSymbol = symbols
			else:
				transition.newStackTopSymbol = self.blankSymbol

		self.transitions.sort()
		
		with open(outputFile, 'w') as csvfile:
			writer = csv.writer(csvfile, delimiter = ' ', escapechar = None, quotechar = None, quoting = csv.QUOTE_NONE, skipinitialspace = True)
			writer.writerow(set2list(self.inputAlphabet))
			writer.writerow(set2list(self.stackAlphabet))
			writer.writerow(self.blankSymbol)
			writer.writerow(self.stackInitialSymbol)
			writer.writerow(set2list(self.states))
			writer.writerow(set2list(self.initialStates))
			writer.writerow(set2list(self.acceptingStates))
			for t in self.transitions:
				writer.writerow([t.currentState, t.currentWordSymbol, t.currentStackTopSymbol, t.newState, t.newStackTopSymbol])


def set2list(dataset):
	sortedList = list(dataset)
	sortedList.sort()
	return sortedList
	

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("Parametros insuficientes. Informe o nome de arquivo de entrada e o nome do arquivo de saida")
		sys.exit(1)
	converter = Jflap2Utfpr()
	converter.convert(sys.argv[1], sys.argv[2], "E")


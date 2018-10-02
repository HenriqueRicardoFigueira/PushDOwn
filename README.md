# PushDOwn

## Get Start
Clone ou faça o Download do projeto em .zip (via terminal/manual) para sua maquina.
- Clone:
  - Execute o camando no Terminal e acessa a pasta do projeto:
    ```
    git clone https://github.com/HenriqueRicardoFigueira/PushDOwn.git
    cd PushDOwn-master/
    ```
- Download:
  - Execute no Terminal de comando:
    ```
    wget https://github.com/HenriqueRicardoFigueira/PushDOwn/archive/master.zip
    ```
  - Descompacte e abra a pasta do projeto:
    ```
    unzip PushDOwn-master.zip
    cd PushDOwn-master/

### Documentação
  -MAIN

    -funcionamento:
        *Instância a classe máquina, cria lista de pilhas, verifica aceitação tanto por pilha vazia, como por estado final, caso ocorra não determinismo adiciona nova pilha criada 	na lista de pilhas.
    
  
  -AUTOMATOPILHA
    
    -Atributos:
        PalavraInicial
	alfaEntrada
	alfaPilha
	vazio
	estados
	estadoInicial
	estadoFinal
	trasicoes
	pilhas
    
    -Funcionamento:
        Quebra o arquivo em linhas e carrega os dados nos atributos, controla a criação de lista de transições, manutenção da lista de pilhas(não determinismo).
    
    -Métodos:
        
        - def carrega_maquinaArquivo():
            *carrega todas as transições para uma lista.

        - def grava_transicoesEstadosOrigem():
            *carrega as transiçoes dos estados de origem para uma lista.

        - def grava_transicoesEstadosDestino():
            *carrega as transições dos estados de destino.

        - def retorna_transicoesPossiveis():
            *dado um estado, retorna as transições que são possiveis para ele.

        - def print_fitas():
            *imprime as fitas.

        - def adiciona_pilha():
            *adiciona uma pilha a listas de pilhas.

        - def remove_pilha():
            *remove uma pilha da lista de pilhas.

        - def clonar_unicaPilha():
            *copia uma pilha da lista de pilhas.

        - def clonar_todasPilhas():
            *copia a lista de pilhas.
        
        - def transicao():
            *retorna as trasições possiveis de um estado, verifica o topo da pilha, a letra, se houver transição possivel vai para ela, empilha ou desempilha , consome palavra e muda o estado.

            #Não determinismo
                *cria a copia de uma pilha, movimenta para as possiveis transações e anexa a pilha a uma nova lista removendo a si mesma da lista anterior a recebe as novas pilhas menos a original.
  
	
    -PILHA
    
    -Atributos:
        pilha
        palavra
        estadoInicial
	estado 

    -Métodos:
        - def empilha():
             *empilha um caracter na pilha.

        - def desempilha():
              *desempilha um caracter da pilha.

        - def vazia():
              *verifica se a pilha está vazia.
      
        - def OlhaTopo():
              *olha o topo da pilha.
      
        - def printPilha():
              *imprime a pilha.
      
        - def retorna_pilha():
              *retorna a pilha

        - def retorna_estado():
              *retorna estado atual
      
        - def muda_estado():
              *muda o estado e consome a palavra.

        - def retorna_tamanho(): 
              *retorna tamanho da pilha.

        - def consome_palavra():
              *consome um caracter da palavra.


### Passos para Execução:
- Execute o seguinte comando no terminal:
  ```
  python main.py examples/(NOME DO ARQUIVO DA MAQUINA) "PALAVRA"
  ```
## Observações
Se você ja está perdido a ponto de ter chegado até aqui, vá em frente e se afunde de uma vez! :trollface:
## Autor
[Gabriel Negrão Silva](https://github.com/itsgnegrao). :alien:

[Henrique Ricardo Figueira](https://github.com/HenriqueRicardoFigueira). :alien:


#lê arquivo:
mt_input = open("input_file.txt", 'r')
linha = mt_input.readline()

class aresta:
    def __init__(self, estado_fim, direcao, leitura, escrita):
        self.estado_fim = estado_fim
        self.direcao = direcao
        self.leitura = leitura
        self.escrita = escrita   
        
    def printar(self):
        print(self.direcao) 
    

class estado:
    def __init__(self, nome):
        self.nome=nome 

    arestas = list()

    def adicionar_aresta(self,aresta):
        self.arestas.append(aresta)

class mt_fita_semi_infinita:

    posicao_cab = 0
    fita = []
    estados = list()
    linhas=list()

    while linha:        
        linha = mt_input.readline()
        linhas.append(linha)
    mt_input.close()

    #<current state> <current symbol> <new symbol> <direction> <new state>
    for linha in linhas:
       if linha:
            char_estado_atual = linha[0]
            char_simbolo_leitura = linha[2]
            char_simbolo_escrita = linha[4]
            char_direcao = linha[6] 
            char_proximo_estado = linha[8]

            aresta_da_interacao = aresta(char_proximo_estado,char_direcao,char_simbolo_leitura, char_simbolo_escrita)
            
            
    
    for e in estados:
        print(e.nome)

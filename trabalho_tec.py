
#lê arquivo:
mt_input = open("input_file.txt", 'r')
linha = mt_input.readline()

class aresta:
    def __init__(self, estado_fim, direcao, leitura, escrita):
        self.estado_fim = estado_fim
        self.direcao = direcao
        self.leitura = leitura
        self.escrita = escrita   
    
class estado:
    def __init__(self, nome):
        self.nome=nome 
        self.arestas=[]

    
    def adicionar_aresta(self,aresta):
        self.arestas.append(aresta)
    
    def get_nome(self):
        return self.nome
    def get_arestas():
        return arestas

class grafo:

    def __init__(self):
        self.estados = list()
        self.estado_inicial=estado("0")
        self.estados.append(self.estado_inicial)
        self.linhas=list()

    def incluir_conteudo(self):
        linha = mt_input.readline()
        self.linhas.append(linha)
        while linha:        
            linha = mt_input.readline()
            self.linhas.append(linha)
        mt_input.close()    

    def check_se_estado_existe_e_inclui_aresta(self,char_estado,aresta_c,estados_c):
        for e in estados_c:
                if(e.nome==char_estado):
                    e.adicionar_aresta(aresta_c)
                    return True
        estado_c = estado(char_estado)
        estado_c.arestas.append(aresta_c)
        estados_c.append(estado_c)
        return False
    #<current state> <current symbol> <new symbol> <direction> <new state>
    def fazer_grafo(self):
        for linha in self.linhas:
            if linha:
                char_estado_atual = linha[0]
                char_simbolo_leitura = linha[2]
                char_simbolo_escrita = linha[4]
                char_direcao = linha[6] 
                char_proximo_estado = linha[8]

                aresta_da_interacao = aresta(char_proximo_estado,char_direcao,char_simbolo_leitura, char_simbolo_escrita)
                #tenho q achar o estado e tacar a aresta no doido
                self.check_se_estado_existe_e_inclui_aresta(char_estado_atual,aresta_da_interacao, self.estados)

    def printar_grafo(self):
        for e in self.estados:
            print(e.nome)
            print("::")
            for a in e.arestas:
                print(a.estado_fim)
            print("-----------------------------")

class mt_semi_infinita:
    def __init__(self):
        self.posicao_cab = 0
        self.fita = []
        self.grafo_semi_inifinita = grafo()
    
    def get_grafo(self):
        return self.grafo_semi_inifinita


if linha==";S\n":
    mt = mt_semi_infinita()
    g=mt.get_grafo()
    g.incluir_conteudo()
    g.fazer_grafo()
    g.printar_grafo()


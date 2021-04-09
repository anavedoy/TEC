
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
    
    def fazer_grafo_1(self):
        for linha in self.linhas:
            if linha and len(linha)>2:     
                print(linha)           
                char_estado_atual = linha[0]
                char_simbolo_leitura = linha[2]
                char_simbolo_escrita = linha[4]
                char_direcao = linha[6] 
                char_proximo_estado = linha[8]            

                aresta_da_interacao = aresta(char_proximo_estado,char_direcao,char_simbolo_leitura, char_simbolo_escrita)
                self.check_se_estado_existe_e_inclui_aresta(char_estado_atual,aresta_da_interacao, self.estados)
    
    def fazer_grafo_2(self):
        for linha in self.linhas:
            if linha:
                #print(linha)
                #print("--------------")

                if len(linha)==10  or linha[8]=="h":
                    char_estado_atual = linha[0]
                    char_simbolo_leitura = linha[2]
                    char_simbolo_escrita = linha[4]
                    char_direcao = linha[6] 
                    char_proximo_estado = linha[8]
                else:
                    if (len(linha)==11 and linha[1]==" "):
                        char_estado_atual = linha[0]
                        char_simbolo_leitura = linha[2]
                        char_simbolo_escrita = linha[4]
                        char_direcao = linha[6] 
                        char_proximo_estado = linha[8:11]
                    else:
                        char_estado_atual = linha[0:2]
                        char_simbolo_leitura = linha[3]
                        char_simbolo_escrita = linha[5]
                        char_direcao = linha[7]
                        char_proximo_estado = linha[9:11]

                aresta_da_interacao = aresta(char_proximo_estado,char_direcao,char_simbolo_leitura, char_simbolo_escrita)
                self.check_se_estado_existe_e_inclui_aresta(char_estado_atual,aresta_da_interacao, self.estados)
   
    def printar_grafo(self):
        for e in self.estados:
            print(e.nome)
            print("::")
            for a in e.arestas:
                print(a.direcao)
                print(a.leitura)
                print(a.escrita)
                print(a.estado_fim)
                print("------------")
            print("---------------------------------------")
    
    def transf_semi_p_inf(self):  
        # no inicio coloco que a fita vai ter um marcador com o simbolo £
        # entao vai existir dois estados auxiliares para por £ na esquerda da palavra de input
        # i * * l j
        # j _ £ r 0
        estado_aux_i = estado("i") 
        aresta_aux_i1 = aresta("j", "l", "0", "0")
        aresta_aux_i2 = aresta("j", "l", "1", "1")
        estado_aux_i.arestas.append(aresta_aux_i1)
        estado_aux_i.arestas.append(aresta_aux_i2)

        estado_aux_j = estado("j")
        aresta_aux_j = aresta("0", "r", "_", "£")
        estado_aux_j.arestas.append(aresta_aux_j)
     
        estados_semi_p_infi = list()
        
        estados_semi_p_infi.append(estado_aux_i)
        estados_semi_p_infi.append(estado_aux_j)

        for e in self.estados:
            estados_semi_p_infi.append(e)

        estados_auxiliares = list()

        # fazer uma copia de cada estado, 
        # seja um estado H e sua copia HH: 
        #   onde se H ler £ vai para copia, onde a instruçao le £ e escreve £, e cabecote vai pra direita
        #   entao se vai para o estado HH com o cabecote ja fora de £ 

        alfabeto = ["a","b","c","d","e","f","g","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        aux=0
        for e in estados_semi_p_infi:
            if(e.nome != "i") and (e.nome != "j"):
                string = alfabeto[aux]
                estado_aux=estado(string)
                for a in e.arestas:
                    estado_aux.arestas.append(a)
                e.arestas.append(aresta(string, "r", "£", "£" ))
                estados_auxiliares.append(estado_aux)
                aux=aux+1
        
        for e in estados_auxiliares:
            estados_semi_p_infi.append(e)

        return estados_semi_p_infi

    def transf_inf_p_semi(self):
        estados_inf_p_semi = list()      

        for e in self.estados:
            for a in e.arestas:
                frase = e.nome + " " + a.leitura + " " + a.escrita + " " + a.direcao + " " + a.estado_fim
               

        estado_aux_i = estado("i")
        aresta_aux_i1 = aresta("i", "r", "0", "0")
        aresta_aux_i2 = aresta("i", "r", "1", "1")
        aresta_aux_i3 = aresta("j", "r", "_", "_")
        estado_aux_i.arestas.append(aresta_aux_i1)
        estado_aux_i.arestas.append(aresta_aux_i2)
        estado_aux_i.arestas.append(aresta_aux_i3)
        estados_inf_p_semi.append(estado_aux_i)
        
        estado_aux_j = estado("j")
        aresta_aux_j1 = aresta("k", "l", "_", "£")
        estado_aux_j.arestas.append(aresta_aux_j1)
        estados_inf_p_semi.append(estado_aux_j)

        estado_aux_k = estado("k")
        aresta_aux_k1 = aresta("l", "l", "_", "_")
        estado_aux_k.arestas.append(aresta_aux_k1)
        estados_inf_p_semi.append(estado_aux_k)
        
        #aresta(estdao_fim, direcao, leitura, escrita)
        estado_aux_l = estado("l")
        aresta_aux_l1 = aresta("m", "r", "1", "_")
        aresta_aux_l2 = aresta("o", "r", "0", "_")
        aresta_aux_l3 = aresta("0", "r", "_", "¢")
        estado_aux_l.arestas.append(aresta_aux_l1)
        estado_aux_l.arestas.append(aresta_aux_l2)
        estado_aux_l.arestas.append(aresta_aux_l3)
        estados_inf_p_semi.append(estado_aux_l)

        estado_aux_m = estado("m")
        aresta_aux_m1 = aresta("n", "l", "_", "1")
        estado_aux_m.arestas.append(aresta_aux_m1)
        estados_inf_p_semi.append(estado_aux_m)

        estado_aux_n = estado("n")
        aresta_aux_n1 = aresta("l", "l", "_", "_")
        estado_aux_n.arestas.append(aresta_aux_n1)
        estados_inf_p_semi.append(estado_aux_n)


        estado_aux_o = estado("o")
        aresta_aux_o1 = aresta("p", "l", "_", "0")
        estado_aux_o.arestas.append(aresta_aux_o1)
        estados_inf_p_semi.append(estado_aux_o)

        estado_aux_p = estado("p")
        aresta_aux_p1 = aresta("l", "l", "_", "_")
        estado_aux_p.arestas.append(aresta_aux_p1)
        estados_inf_p_semi.append(estado_aux_p)

        for e in self.estados:
            estados_inf_p_semi.append(e)
        
        for e in estados_inf_p_semi:
            e.arestas.append(aresta(e.nome, "r", "¢", "¢"))  
            e.arestas.append(aresta(e.nome, "r", "£", "£"))      

        return estados_inf_p_semi
    
    #<current state> <current symbol> <new symbol> <direction> <new state>
    def exportar_grafo(self, lista_estados):
        mt_output = open("output_file.txt", "w")
        for e in lista_estados:
            for a in e.arestas:
                if a.estado_fim=="h":
                    a.estado_fim="halt-accept"
                frase = e.nome + " " + a.leitura + " " + a.escrita + " " + a.direcao + " "
                mt_output.write(frase+ a.estado_fim + "\n")
        
        mt_output.close()


if linha==";S\n":
    g=grafo()
    g.incluir_conteudo()
    g.fazer_grafo_1()
    lista_estados_auxiliar = g.transf_semi_p_inf()
    g.exportar_grafo(lista_estados_auxiliar)

if linha==";I\n":
    g=grafo()
    g.incluir_conteudo()
    g.fazer_grafo_2() 
    lista_estados_auxiliar = g.transf_inf_p_semi()
    g.exportar_grafo(lista_estados_auxiliar)



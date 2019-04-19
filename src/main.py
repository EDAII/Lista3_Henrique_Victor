from tkinter import *
from tkinter import filedialog
from funcoes import *

bg_color = "white"
button_color = "cyan"
option_button_font = ("Arial", "15", "bold")
confirmation_button_font = ("Arial", "10", "bold")
error_msg_font = ("Arial", "10", "bold")
text_font = ("Arial", "20", "bold")

def verif_ano(ano):
    if ano.isalpha() == True:
        return "Ano deve ser um numero de 1930 a 2019"
    
    ano = int(ano)

    if ano < 1930:
        return "O ano deve ser 1930 ou maior"
    
    if ano > 2019:
        return "O ano deve ser 2019 ou menor"
    
    return ano


def verif_placa(placa):
    if len(placa) < 7:
        return "Quantidade de caracteres para placa menor que o necessario ({}). Deve ser 7".format(len(placa))

    if len(placa) > 7:
        return "Quantidade de caracteres para placa maior que o necessario ({}). Deve ser 7".format(len(placa))
    
    if placa[0:3].isalpha() == False:
        return "Formato incorreto da placa. Erro esta nos 3 primeiros caracteres (devem ser apenas letras)"
    
    if placa[3:].isdigit() == False:
        return "Formato incorreto da placa. Erro esta nos 4 ultimos caracteres (devem ser apenas numeros)"

    return placa.upper()

class Interface:
    def __init__(self, instancia_Tk):
        self.registros = []
        self.desordenado = []
        self.ordenado = False
        
        topo = Frame(instancia_Tk, background=bg_color, pady=50)
        topo.pack()
        frame1 = Frame(instancia_Tk, background=bg_color, pady=6)
        frame1.pack()
        frame2 = Frame(instancia_Tk, background=bg_color, pady=6)
        frame2.pack()
        frame3 = Frame(instancia_Tk, background=bg_color, pady=6)
        frame3.pack()
        frame4 = Frame(instancia_Tk, background=bg_color, pady=6)
        frame4.pack()
        frame5 = Frame(instancia_Tk, background=bg_color, pady=6)
        frame5.pack()

        self.msgResgistros = Label(topo, text = "Quantidade de Registros: 0")
        self.msgResgistros.config(background=bg_color, font=text_font, padx=150)
        self.msgResgistros.pack(side=LEFT)

        self.msgOrdenacao = Label(topo, text = "Tipo de Ordenacao: Nenhuma")
        self.msgOrdenacao.config(background=bg_color, font=text_font, padx=150)
        self.msgOrdenacao.pack(side=RIGHT)

        B1 = Button(frame1, text="Gerar Registros Aleatoriamente", width=55, bg=button_color, font=option_button_font, command=self.gerar_regist_aleat)
        B1.pack(side=LEFT)

        B2 = Button(frame1, text="Cadastrar Registro Individual", width=55, bg=button_color, font=option_button_font, command=self.cadastro)
        B2.pack(side=RIGHT)

        B3 = Button(frame2, text="Ordenar", width=112, bg=button_color, font=option_button_font, command=self.ordenar)
        B3.pack(side=LEFT)

        B4 = Button(frame3, text="Mostrar Registros (Ordem de Cadastro)", width=55, bg=button_color, font=option_button_font, command=lambda: mostrar_registros(self.desordenado, len(self.desordenado)))
        B4.pack(side=LEFT)

        B5 = Button(frame3, text="Mostrar Registros (Ordenado por Ano)", width=55, bg=button_color, font=option_button_font, command=self.mostrar_registros_ordenado)
        B5.pack(side=RIGHT)

        B6 = Button(frame4, text="Comparar Metodos de Ordenacao (Registro atual)", width=55, bg=button_color, font=option_button_font, command=lambda: comparar_ordenacoes(self.registros, self.desordenado))
        B6.pack(side=LEFT)

        B7 = Button(frame4, text="Comparar Metodos de Ordenacao (Varios Registros Aleatorios)", width=55, bg=button_color, font=option_button_font, command=comparacoes)
        B7.pack(side=RIGHT)

        B8 = Button(frame5, text="Ler Registros de Arquivo", width=55, bg=button_color, font=option_button_font, command=self.abre_arquivo)
        B8.pack(side=LEFT)

        B9 = Button(frame5, text="Salvar Registros em Arquivo", width=55, bg=button_color, font=option_button_font, command=self.salva_arquivo)
        B9.pack(side=RIGHT)
    

    def gerar_regist_aleat(self):
        tela = Tk()
        tela.title('Gerar Registros Aleatoriamente')

        texto = Frame(tela, pady=10)
        texto.pack()
        campo = Frame(tela, pady=10)
        campo.pack()
        botoes = Frame(tela, pady=10)
        botoes.pack()
        msg = Frame(tela, pady=10)
        msg.pack()

        text = Label(texto, text="Digite quantos registros voce quer criar", font=text_font)
        text.pack()

        valor = Entry(campo)
        valor.pack()

        mensagem = Label(msg, text=" ", font=error_msg_font)
        mensagem.pack()

        botaoCancel = Button(botoes, text="CANCELAR", font=confirmation_button_font, bg='red2', command=tela.destroy)
        botaoCancel.pack(side=LEFT)

        botaoSend = Button(botoes, text="ENVIAR", font=confirmation_button_font, bg='green2', command=lambda: self.verif_valor(valor.get(), mensagem, tela))
        botaoSend.pack(side=RIGHT)

        tela.geometry("600x200+700+400")
        tela.mainloop()
    

    def verif_valor(self, valor, mensagem, tela):
        try:
            valor = int(valor)
            if valor > 0:
                gerar_registros_aleatorios(self.registros, valor)
                self.desordenado = self.registros.copy()
                self.ordenado = False
                tela.destroy()
                self.msgResgistros["text"] = "Quantidade de Registros: {}".format(len(self.registros))
                self.msgOrdenacao["text"] = "Tipo de Ordenacao: Nenhuma"
            else:
                mensagem["text"] = "Numero deve ser maior do que 0"
        except ValueError:
            mensagem["text"] = "Deve ser um numero valido"
    

    def cadastro(self):
        tela = Tk()
        tela.title('Cadastrar Registro Individual')

        texto = Frame(tela, pady=10)
        texto.pack()
        frame1 = Frame(tela, pady=10)
        frame1.pack()
        frame2 = Frame(tela, pady=10)
        frame2.pack()
        frame3 = Frame(tela, pady=10)
        frame3.pack()
        frame4 = Frame(tela, pady=10)
        frame4.pack()
        botoes = Frame(tela, pady=10)
        botoes.pack()        
        msg = Frame(tela, pady=10)
        msg.pack()

        text = Label(texto, text="Digite os dados do Registro", font=text_font, pady=10)
        text.pack()

        anotext = Label(frame1, text="Ano: ", padx=13)
        anotext.pack(side=LEFT)
        ano = Entry(frame1)
        ano.pack(side=RIGHT)

        placatext = Label(frame2, text="Placa: ", padx=8)
        placatext.pack(side=LEFT)
        placa = Entry(frame2)
        placa.pack(side=RIGHT)

        donotext = Label(frame3, text="Dono: ", padx=8)
        donotext.pack(side=LEFT)
        dono = Entry(frame3)
        dono.pack(side=RIGHT)

        modelotext = Label(frame4, text="Modelo: ")
        modelotext.pack(side=LEFT)
        modelo = Entry(frame4)
        modelo.pack(side=RIGHT)

        mensagem = Label(msg, text=" ", font=error_msg_font)
        mensagem.pack()

        botaoCancel = Button(botoes, text="CANCELAR", font=confirmation_button_font, bg='red2', command=tela.destroy)
        botaoCancel.pack(side=LEFT)

        botaoSend = Button(botoes, text="ENVIAR", font=confirmation_button_font, bg='green2', command=lambda: self.verif_cadastro(ano.get(), placa.get(), dono.get(), modelo.get(), mensagem, tela))
        botaoSend.pack(side=RIGHT)

        tela.geometry("650x350+650+300")
        tela.mainloop()
    

    def verif_cadastro(self, ano, placa, dono, modelo, mensagem, tela):
        try:
            ano = verif_ano(ano)
            ano = int(ano)
            placa = verif_placa(placa)
            if len(placa) != 7:
                mensagem["text"] = placa
            elif len(dono) == 0:
                mensagem["text"] = "Dono em branco"
            elif len(modelo) == 0:
                mensagem["text"] = "Modelo em branco"
            else:
                registro_unico(self.registros, ano, placa, dono, modelo)
                self.desordenado.append(self.registros[len(self.registros)-1])
                self.ordenado = False
                self.msgResgistros["text"] = "Quantidade de Registros: {}".format(len(self.registros))
                self.msgOrdenacao["text"] = "Tipo de Ordenacao: Nenhuma"
                tela.destroy()
        except ValueError:
            mensagem["text"] = ano
    

    def ord_aux(self, tipo, registros, tela):
        if tipo == "MS":
            merge_sort(registros)
            self.msgOrdenacao["text"] = "Tipo de Ordenacao: Merge Sort"
        elif tipo == "QSIR":
            quick_sort_inst_rec(registros, 0, len(registros)-1)
            self.msgOrdenacao["text"] = "Tipo de Ordenacao: Quick Sort (Instavel e Recursivo)"
        elif tipo == "QSER":
            self.registros = quick_sort_est_rec(registros)
            self.msgOrdenacao["text"] = "Tipo de Ordenacao: Quick Sort (Estavel e Recursivo)"
        elif tipo == "QSII":
            quick_sort_inst_iterat(registros, 0, len(registros)-1)
            self.msgOrdenacao["text"] = "Tipo de Ordenacao: Quick Sort (Instavel e Interativo)"
        else:
            self.registros = bucket_sort(registros)
            self.msgOrdenacao["text"] = "Tipo de Ordenacao: Bucket Sort"
        
        self.ordenado = True
        tela.destroy()


    def ordenar(self):
        if len(self.registros) == 0:
            self.aviso("Nao ha nenhum registro")
        elif self.ordenado == True:
            self.aviso("Os Registros ja estao Ordenados")
        else:
            tela = Tk()
            tela.title('Ordenar')

            top = Frame(tela)
            middle = Frame(tela)
            top.pack()
            middle.pack()

            text = Label(top, text="Escolha um dos metodos abaixo", font=text_font, pady=10)
            text.grid(row=0, pady=5)

            B1 = Button(middle, text="Merge Sort", width=30, bg=button_color, font=option_button_font, command=lambda: self.ord_aux("MS", self.registros, tela))
            B1.grid(row=1, padx=10, pady=5)

            B2 = Button(middle, text="Quick Sort (Instavel e Recursivo)", width=30, bg=button_color, font=option_button_font, command=lambda: self.ord_aux("QSIR", self.registros, tela))
            B2.grid(row=2, padx=10, pady=5)

            B3 = Button(middle, text="Quick Sort (Estavel e Recursivo)", width=30, bg=button_color, font=option_button_font, command=lambda: self.ord_aux("QSER", self.registros, tela))
            B3.grid(row=3, padx=10, pady=5)

            B4 = Button(middle, text="Quick Sort (Instavel e Interativo)", width=30, bg=button_color, font=option_button_font, command=lambda: self.ord_aux("QSII", self.registros, tela))
            B4.grid(row=4, padx=10, pady=5)

            B5 = Button(middle, text="Bucket Sort", width=30, bg=button_color, font=option_button_font, command=lambda: self.ord_aux("BS", self.registros, tela))
            B5.grid(row=5, padx=10, pady=5)

            tela.geometry("500x330+750+300")
            tela.mainloop()
    

    def abre_arquivo(self):
        self.registros.clear()
        path = filedialog.askopenfilename(initialdir = "/",title = "Selecione o Arquivo",filetypes = [("eda2 files","*.eda2")])

        i = 0
        ano = 0
        placa = ""
        dono = ""
        modelo = ""
        try:
            with open(path, 'r') as arq:
                for linha in arq:
                    linha = linha.strip()
                    if i == 0:
                        ano = int(linha)
                    elif i == 1:
                        placa = linha
                    elif i == 2:
                        dono = linha
                    else:
                        modelo = linha
                
                    i += 1

                    if i == 4:
                        self.registros.append(Registro(ano, placa, dono, modelo, len(self.registros)+1))
                        i = 0

            arq.close()
            self.msgResgistros["text"] = "Quantidade de Registros: {}".format(len(self.registros))
            self.msgOrdenacao["text"] = "Tipo de Ordenacao: Nenhuma"
            self.ordenado = False
        except:
            return


    def salva_arquivo(self):
        path = filedialog.asksaveasfilename(initialdir = "/",title = "Selecione o Local para Salvar",filetypes = [("eda2 files","*.eda2")])
        
        try:
            arq = open(path, 'w')

            for i in range(len(self.registros)):
                arq.write('{}\n'.format(self.registros[i].ano))
                arq.write('{}\n'.format(self.registros[i].placa))
                arq.write('{}\n'.format(self.registros[i].dono))
                arq.write('{}\n'.format(self.registros[i].modelo))
        
            arq.close()
        except:
            return
    
    def aviso(self, mensagem):
        tela = Tk()
        tela.title('Aviso')

        msg = Frame(tela)
        botaoFrame = Frame(tela)
        msg.pack()
        botaoFrame.pack()

        text = Label(msg, text=mensagem, font=text_font, pady=10)
        text.pack()

        botao = Button(botaoFrame, text=" OK ", command=tela.destroy)
        botao.pack()

        tela.geometry("550x100+700+400")
        tela.mainloop()

    def mostrar_registros_ordenado(self):
        if len(self.registros) == 0:
            self.aviso("Nao ha nenhum registro")
        elif self.ordenado == False:
            self.aviso("Primeiro use algum Metodo de Ordenacao")
        else:
            mostrar_registros(self.registros, len(self.registros))


if __name__ == '__main__':
    menu=Tk()
    menu.title('LISTA 3 - ESTRUTURA DE DADOS 2')
    menu.config(background=bg_color)
    menu.geometry("1400x450+300+200")
    Interface(menu)
    menu.mainloop()
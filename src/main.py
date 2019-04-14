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
        self.topo = Frame(instancia_Tk)
        self.topo["pady"] = 50
        self.topo.config(background=bg_color)
        self.topo.pack()
        self.frame1 = Frame(instancia_Tk)
        self.frame1["pady"] = 6
        self.frame1.config(background=bg_color)
        self.frame1.pack()
        self.frame2 = Frame(instancia_Tk)
        self.frame2["pady"] = 6
        self.frame2.config(background=bg_color)
        self.frame2.pack()
        self.frame3 = Frame(instancia_Tk)
        self.frame3["pady"] = 6
        self.frame3.config(background=bg_color)
        self.frame3.pack()
        self.frame4 = Frame(instancia_Tk)
        self.frame4["pady"] = 6
        self.frame4.config(background=bg_color)
        self.frame4.pack()
        self.frame5 = Frame(instancia_Tk)
        self.frame5["pady"] = 6
        self.frame5.config(background=bg_color)
        self.frame5.pack()

        self.msg1 = Label(self.topo, text = "Quantidade de Registros: 0")
        self.msg1["padx"] = 150
        self.msg1["font"] = text_font
        self.msg1.config(background=bg_color)
        self.msg1.pack(side=LEFT)

        self.msg2 = Label(self.topo, text = "Tipo de Ordenacao: Nenhuma")
        self.msg2["padx"] = 150
        self.msg2["font"] = text_font
        self.msg2.config(background=bg_color)
        self.msg2.pack(side=RIGHT)

        self.B1 = Button(self.frame1, text="Gerar Registros Aleatoriamente", width=55, bg=button_color)
        self.B1["font"] = option_button_font
        self.B1.pack(side=LEFT)
        self.B1["command"] = self.gerar_regist_aleat

        self.B2 = Button(self.frame1, text="Cadastrar Registro Individual", width=55, bg=button_color)
        self.B2["font"] = option_button_font
        self.B2.pack(side=RIGHT)
        self.B2["command"] = self.cadastro

        self.B3 = Button(self.frame2, text="Ordenar", width=112, bg=button_color)
        self.B3["font"] = option_button_font
        self.B3.pack(side=LEFT)
        self.B3["command"] = self.ordenar

        self.B4 = Button(self.frame3, text="Mostrar Registros (Desordenado)", width=55, bg=button_color)
        self.B4["font"] = option_button_font
        self.B4.pack(side=LEFT)
        self.B4["command"] = lambda: mostrar_registros(self.desordenado, len(self.desordenado))

        self.B5 = Button(self.frame3, text="Mostrar Registros (Ordenado)", width=55, bg=button_color)
        self.B5["font"] = option_button_font
        self.B5.pack(side=RIGHT)
        self.B5["command"] = self.mostrar_registros_ordenado

        self.B6 = Button(self.frame4, text="Comparar Metodos de Ordenacao (Registro atual)", width=55, bg=button_color)
        self.B6["font"] = option_button_font
        self.B6.pack(side=LEFT)
        self.B6["command"] = lambda: comparar_ordenacoes(self.registros, self.desordenado)

        self.B7 = Button(self.frame4, text="Comparar Metodos de Ordenacao (Varios Registros Aleatorios)", width=55, bg=button_color)
        self.B7["font"] = option_button_font
        self.B7.pack(side=RIGHT)
        #self.B7["command"] = lambda: 

        self.B8 = Button(self.frame5, text="Ler Registros de Arquivo", width=55, bg=button_color)
        self.B8["font"] = option_button_font
        self.B8.pack(side=LEFT)
        self.B8["command"] = self.abre_arquivo

        self.B9 = Button(self.frame5, text="Salvar Registros em Arquivo", width=55, bg=button_color)
        self.B9["font"] = option_button_font
        self.B9.pack(side=RIGHT)
        self.B9["command"] = self.salva_arquivo
    

    def gerar_regist_aleat(self):
        tela = Tk()
        tela.title('Gerar Registros Aleatoriamente')
        texto = Frame(tela)
        campo = Frame(tela)
        botoes = Frame(tela)
        msg = Frame(tela)
        texto["pady"] = 10
        campo["pady"] = 10
        botoes["pady"] = 10
        msg["pady"] = 10
        texto.pack()
        campo.pack()
        botoes.pack()
        msg.pack()

        text = Label(texto, text="Digite quantos registros voce quer criar")
        text["font"] = text_font
        text.pack()

        valor = Entry(campo)
        valor.pack()

        mensagem = Label(msg, text=" ")
        mensagem["font"] = error_msg_font
        mensagem.pack()

        botaoCancel = Button(botoes, text="CANCELAR", bg='red2')
        botaoCancel["command"] = tela.destroy
        botaoCancel["font"] = confirmation_button_font
        botaoCancel.pack(side=LEFT)

        botaoSend = Button(botoes, text="ENVIAR", bg='green2')
        botaoSend["command"] = lambda: self.verif_valor(valor.get(), mensagem, tela)
        botaoSend["font"] = confirmation_button_font
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
                self.msg1["text"] = "Quantidade de Registros: {}".format(len(self.registros))
                self.msg2["text"] = "Tipo de Ordenacao: Nenhuma"
            else:
                mensagem["text"] = "Numero deve ser maior do que 0"
        except ValueError:
            mensagem["text"] = "Deve ser um numero valido"
    

    def cadastro(self):
        tela = Tk()
        tela.title('Cadastrar Registro Individual')
        texto = Frame(tela)
        frame1 = Frame(tela)
        frame2 = Frame(tela)
        frame3 = Frame(tela)
        frame4 = Frame(tela)
        botoes = Frame(tela)
        msg = Frame(tela)
        texto["pady"] = 10
        frame1["pady"] = 10
        frame2["pady"] = 10
        frame3["pady"] = 10
        frame4["pady"] = 10
        botoes["pady"] = 10
        msg["pady"] = 10
        texto.pack()
        frame1.pack()
        frame2.pack()
        frame3.pack()
        frame4.pack()
        botoes.pack()
        msg.pack()

        text = Label(texto, text="Digite quantos registros voce quer criar")
        text["font"] = text_font
        text["pady"] = 10
        text.pack()

        anotext = Label(frame1, text="Ano: ")
        anotext["padx"] = 13
        anotext.pack(side=LEFT)
        ano = Entry(frame1)
        ano.pack(side=RIGHT)

        placatext = Label(frame2, text="Placa: ")
        placatext["padx"] = 8
        placatext.pack(side=LEFT)
        placa = Entry(frame2)
        placa.pack(side=RIGHT)

        donotext = Label(frame3, text="Dono: ")
        donotext["padx"] = 8
        donotext.pack(side=LEFT)
        dono = Entry(frame3)
        dono.pack(side=RIGHT)

        modelotext = Label(frame4, text="Modelo: ")
        modelotext.pack(side=LEFT)
        modelo = Entry(frame4)
        modelo.pack(side=RIGHT)

        mensagem = Label(msg, text=" ")
        mensagem["font"] = error_msg_font
        mensagem.pack()

        botaoCancel = Button(botoes, text="CANCELAR", bg='red2')
        botaoCancel["command"] = tela.destroy
        botaoCancel["font"] = confirmation_button_font
        botaoCancel.pack(side=LEFT)

        botaoSend = Button(botoes, text="ENVIAR", bg='green2')
        botaoSend["command"] = lambda: self.verif_cadastro(ano.get(), placa.get(), dono.get(), modelo.get(), mensagem, tela)
        botaoSend["font"] = confirmation_button_font
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
                self.msg1["text"] = "Quantidade de Registros: {}".format(len(self.registros))
                self.msg2["text"] = "Tipo de Ordenacao: Nenhuma"
                tela.destroy()
        except ValueError:
            mensagem["text"] = ano
    

    def ord_aux(self, tipo, registros, tela):
        if tipo == "MS":
            merge_sort(registros)
            self.msg2["text"] = "Tipo de Ordenacao: Merge Sort"
        elif tipo == "QSIR":
            quick_sort_inst_rec(registros, 0, len(registros)-1)
            self.msg2["text"] = "Tipo de Ordenacao: Quick Sort (Instavel e Recursivo)"
        elif tipo == "QSER":
            self.registros = quick_sort_est_rec(registros)
            self.msg2["text"] = "Tipo de Ordenacao: Quick Sort (Estavel e Recursivo)"
        elif tipo == "QSII":
            quick_sort_inst_iterat(registros, 0, len(registros)-1)
            self.msg2["text"] = "Tipo de Ordenacao: Quick Sort (Instavel e Interativo)"
        else:
            self.registros = bucket_sort(registros)
            self.msg2["text"] = "Tipo de Ordenacao: Bucket Sort"
        
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

            text = Label(top, text="Escolha um dos metodos abaixo")
            text["pady"] = 10
            text["font"] = text_font
            text.grid(row=0, pady=5)

            B1 = Button(middle, text="Merge Sort", width=30, bg=button_color)
            B1["font"] = option_button_font
            B1.grid(row=1, padx=10, pady=5)
            B1["command"] = lambda: self.ord_aux("MS", self.registros, tela)

            B2 = Button(middle, text="Quick Sort (Instavel e Recursivo)", width=30, bg=button_color)
            B2["font"] = option_button_font
            B2.grid(row=2, padx=10, pady=5)
            B2["command"] = lambda: self.ord_aux("QSIR", self.registros, tela)

            B3 = Button(middle, text="Quick Sort (Estavel e Recursivo)", width=30, bg=button_color)
            B3["font"] = option_button_font
            B3.grid(row=3, padx=10, pady=5)
            B3["command"] = lambda: self.ord_aux("QSER", self.registros, tela)

            B4 = Button(middle, text="Quick Sort (Instavel e Interativo)", width=30, bg=button_color)
            B4["font"] = option_button_font
            B4.grid(row=4, padx=10, pady=5)
            B4["command"] = lambda: self.ord_aux("QSII", self.registros, tela)

            B5 = Button(middle, text="Bucket Sort", width=30, bg=button_color)
            B5["font"] = option_button_font
            B5.grid(row=5, padx=10, pady=5)
            B5["command"] = lambda: self.ord_aux("BS", self.registros, tela)

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
            self.msg1["text"] = "Quantidade de Registros: {}".format(len(self.registros))
            self.msg2["text"] = "Tipo de Ordenacao: Nenhuma"
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

        text = Label(msg, text=mensagem)
        text["font"] = text_font
        text["pady"] = 10
        text.pack()

        botao = Button(botaoFrame, text=" OK ")
        botao["command"] = tela.destroy
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
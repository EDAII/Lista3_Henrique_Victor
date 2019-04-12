from tkinter import *
from funcoes import *

registros = []
desordenado = []
ordenado = False

def verif_placa(placa):
    pass

class Interface:
    def __init__(self, instancia_Tk):
        self.topo = Frame(instancia_Tk)
        self.topo["pady"] = 50
        self.topo.pack()
        self.frame1 = Frame(instancia_Tk)
        self.frame1["pady"] = 6
        self.frame1.pack()
        self.frame2 = Frame(instancia_Tk)
        self.frame2["pady"] = 6
        self.frame2.pack()
        self.frame3 = Frame(instancia_Tk)
        self.frame3["pady"] = 6
        self.frame3.pack()
        self.frame4 = Frame(instancia_Tk)
        self.frame4["pady"] = 6
        self.frame4.pack()
        self.frame5 = Frame(instancia_Tk)
        self.frame5["pady"] = 6
        self.frame5.pack()

        self.msg1 = Label(self.topo, text = "Quantidade de Registros: 0")
        self.msg1["padx"] = 150
        self.msg1["font"] = ("Arial", "20", "bold")
        self.msg1.pack(side=LEFT)

        self.msg2 = Label(self.topo, text = "Tipo de Ordenacao: Nenhuma")
        self.msg2["padx"] = 150
        self.msg2["font"] = ("Arial", "20", "bold")
        self.msg2.pack(side=RIGHT)

        self.B1 = Button(self.frame1, text="Gerar Registros Aleatoriamente", width=55)
        self.B1["font"] = ("Arial", "15", "bold")
        self.B1.pack(side=LEFT)
        self.B1["command"] = self.gerar_regist_aleat

        self.B2 = Button(self.frame1, text="Cadastrar Registro Individual", width=55)
        self.B2["font"] = ("Arial", "15", "bold")
        self.B2.pack(side=RIGHT)
        self.B2["command"] = self.cadastro

        self.B3 = Button(self.frame2, text="Ordenar", width=112)
        self.B3["font"] = ("Arial", "15", "bold")
        self.B3.pack(side=LEFT)
        self.B3["command"] = self.ordenar

        self.B4 = Button(self.frame3, text="Mostrar Registros (Desordenado)", width=55)
        self.B4["font"] = ("Arial", "15", "bold")
        self.B4.pack(side=LEFT)
        self.B4["command"] = lambda: mostrar_registros(desordenado, len(registros)) # Mudar

        self.B5 = Button(self.frame3, text="Mostrar Registros (Ordenado)", width=55)
        self.B5["font"] = ("Arial", "15", "bold")
        self.B5.pack(side=RIGHT)
        self.B5["command"] = lambda: mostrar_registros(registros, len(registros)) # Mudar

        self.B6 = Button(self.frame4, text="Comparar Metodos de Ordenacao (Registro atual)", width=55)
        self.B6["font"] = ("Arial", "15", "bold")
        self.B6.pack(side=LEFT)
        self.B6["command"] = lambda: comparar_ordenacoes(registros, desordenado)

        self.B7 = Button(self.frame4, text="Comparar Metodos de Ordenacao (Varios Registros Aleatorios)", width=55)
        self.B7["font"] = ("Arial", "15", "bold")
        self.B7.pack(side=RIGHT)
        #self.B7["command"] = lambda: 

        self.B8 = Button(self.frame5, text="Ler Registros de Arquivo", width=55)
        self.B8["font"] = ("Arial", "15", "bold")
        self.B8.pack(side=LEFT)
        #self.B8["command"] = lambda: 

        self.B9 = Button(self.frame5, text="Salvar Registros em Arquivo", width=55)
        self.B9["font"] = ("Arial", "15", "bold")
        self.B9.pack(side=RIGHT)
        #self.B9["command"] = lambda: 
    

    def gerar_regist_aleat(self):
        tela = Tk()
        tela.title('Gerar Registros Aleatoriamente')
        campo = Frame(tela)
        confirmacao = Frame(tela)
        campo["pady"] = 30
        confirmacao["pady"] = 5
        campo.pack()
        confirmacao.pack()

        text = Label(campo, text="Digite quantos registros voce quer criar")
        text["font"] = ("Arial", "15")
        text.grid(row=0, pady=5)
        valor = Entry(campo)
        valor.grid(row=1, pady=5)

        mensagem = Label(confirmacao, text="")
        mensagem["font"] = ("Arial", "10")

        botao = Button(confirmacao, text="ENVIAR", height=1)
        botao["command"] = lambda: self.verif_valor(valor.get(), mensagem, tela)
        botao.grid(row=2, pady=5)
        mensagem.grid(row=3, pady=5)

        tela.geometry("400x200+700+400")
        tela.mainloop()
    

    def verif_valor(self, valor, mensagem, tela):
        try:
            valor = int(valor)
            if valor > 0:
                gerar_registros_aleatorios(registros, valor)
                desordenado = registros.copy()
                tela.destroy()
                self.msg1["text"] = "Quantidade de Registros: {}".format(len(registros))
                self.msg2["text"] = "Tipo de Ordenacao: Nenhuma"
            else:
                mensagem["text"] = "Numero deve ser maior do que 0"
        except ValueError:
            mensagem["text"] = "Deve ser um numero valido"
    

    def cadastro(self):
        tela = Tk()
        tela.title('Cadastrar Registro Individual')
        top = Frame(tela)
        middle = Frame(tela)
        bottom = Frame(tela)
        top.pack()
        middle.pack()
        bottom.pack()

        text = Label(top, text="Digite quantos registros voce quer criar")
        text["pady"] = 10
        text.pack()

        anotext = Label(middle, text="Ano:")
        anotext.grid(row=0, column=0, pady=10)
        ano = Entry(middle)
        ano.grid(row=0, column=1, pady=10)

        placatext = Label(middle, text="Placa:")
        placatext.grid(row=1, column=0, pady=10)
        placa = Entry(middle)
        placa.grid(row=1, column=1, pady=10)

        donotext = Label(middle, text="Dono:")
        donotext.grid(row=2, column=0, pady=10)
        dono = Entry(middle)
        dono.grid(row=2, column=1, pady=10)

        modelotext = Label(middle, text="Modelo:")
        modelotext.grid(row=3, column=0, pady=10)
        modelo = Entry(middle)
        modelo.grid(row=3, column=1, pady=10)

        mensagem = Label(bottom, text="")
        mensagem["font"] = ("Arial", "10")

        botao = Button(bottom, text="ENVIAR", height=1)
        botao["command"] = lambda: self.verif_cadastro(ano.get(), placa.get(), dono.get(), modelo.get(), mensagem, tela)
        botao.grid(row=0, pady=5)
        mensagem.grid(row=1, pady=5)

        tela.geometry("400x300+400+400")
        tela.mainloop()
    

    def verif_cadastro(self, ano, placa, dono, modelo, mensagem, tela):
        try:
            ano = int(ano)
            placa = int(placa)

            if len(dono) == 0:
                mensagem["text"] = "Dono em branco"
            elif len(modelo) == 0:
                mensagem["text"] = "Modelo em branco"
            else:
                registro_unico(registros, ano, placa, dono, modelo)
                desordenado = registros.copy()
                self.msg2["text"] = "Tipo de Ordenacao: Nenhuma"
                tela.destroy()
        except ValueError:
            mensagem["text"] = "Ano e Placa devem ser um numero valido"
    

    def ord_aux(self, tipo, registros, tela):
        if tipo == "MS":
            merge_sort(registros)
            self.msg2["text"] = "Tipo de Ordenacao: Merge Sort"
        elif tipo == "QSIR":
            quick_sort_inst_rec(registros, 0, len(registros)-1)
            self.msg2["text"] = "Tipo de Ordenacao: Quick Sort (Instavel e Recursivo)"
        elif tipo == "QSER":
            registros = quick_sort_est_rec(registros)
            self.msg2["text"] = "Tipo de Ordenacao: Quick Sort (Estavel e Recursivo)"
        elif tipo == "QSII":
            quick_sort_inst_iterat(registros, 0, len(registros)-1)
            self.msg2["text"] = "Tipo de Ordenacao: Quick Sort (Instavel e Interativo)"
        else:
            registros = bucket_sort(registros)
            self.msg2["text"] = "Tipo de Ordenacao: Bucket Sort"
        
        tela.destroy()


    def ordenar(self):
        tela = Tk()
        tela.title('Ordenar')
        top = Frame(tela)
        middle = Frame(tela)
        top.pack()
        middle.pack()

        text = Label(top, text="Escolha um dos metodos abaixo")
        text["pady"] = 10
        text["font"] = ("Arial", "15")
        text.grid(row=0, pady=5)

        B1 = Button(middle, text="Merge Sort", width=30)
        B1.grid(row=1, padx=10, pady=5)
        B1["command"] = lambda: self.ord_aux("MS", registros, tela)

        B2 = Button(middle, text="Quick Sort (Instavel e Recursivo)", width=30)
        B2.grid(row=2, padx=10, pady=5)
        B2["command"] = lambda: self.ord_aux("QSIR", registros, tela)

        B3 = Button(middle, text="Quick Sort (Estavel e Recursivo)", width=30)
        B3.grid(row=3, padx=10, pady=5)
        B3["command"] = lambda: self.ord_aux("QSER", registros, tela)

        B4 = Button(middle, text="Quick Sort (Instavel e Interativo)", width=30)
        B4.grid(row=4, padx=10, pady=5)
        B4["command"] = lambda: self.ord_aux("QSII", registros, tela)

        B5 = Button(middle, text="Bucket Sort", width=30)
        B5.grid(row=5, padx=10, pady=5)
        B5["command"] = lambda: self.ord_aux("BS", registros, tela)

        tela.geometry("400x270+400+400")
        tela.mainloop()


if __name__ == '__main__':
    menu=Tk()
    menu.title('LISTA 3 - ESTRUTURA DE DADOS 2')
    menu.geometry("1400x450+300+200")
    Interface(menu)
    menu.mainloop()
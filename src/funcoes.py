import os
import random
import string
import time
import matplotlib
import matplotlib.pyplot as plt
from registros import Registro
from ordenacoes import *
import plotly
import plotly.graph_objs as go
import numpy as np

modelos = [
    'A1',
    'A3 Sedan',
    'Agile',
    'Astra',
    'Blazer',
    'Camaro',
    'Captiva',
    'Celta',
    'Classic',
    'Cobalt',
    'Corsa',
    'Cruze',
    'Civic',
    'Amarok',
    'S10',
    'Hilux',
    'QQ',
    'Onix',
    'Eclipse',
    'Vectra',
    'Zafira',
    'Palio',
    'EcoSport',
    'Punto',
    'Mobi',
    'Uno',
    'Toro',
    'Renegade',
    'Freemont',
    'Strada',
    'Saveiro',
    'Ranger',
    'Frontier',
    'Accord',
    'City',
    'Fit',
    'Corolla',
    'Azera',
    'HB20',
    'Tucson',
    'Veloster',
    'i30',
    'Sonata',
    'Range Rover Evoque',
    'L200',
    'Kicks',
    'Sentra',
    'Tiida',
    'Versa',
    'Pajero',
    '208',
    '3008',
    'Cayman',
    'RAM 2500',
    'Clio',
    'Sandero',
    'Kwid',
    'Camry',
    'Etios',
    'Prius',
    'Fox',
    'Gol',
    'Crossfox',
    'Fusca',
    'Golf',
    'Jetta',
    'Kombi',
    'Parati',
    'Passat',
    'Polo',
    'Argo',
    'Tiguan',
    'Up!',
    'Voyage',
    'Fiesta',
    'Ka',
    'Focus',
    'Fusion',
    'Spin',
    'Aventador',
    'i8',
    'Monza',
    'Opala',
    'Mustang',
    '350Z',
    '370Z'

]


def clear():
    input("Pressione uma tecla para continuar...")
    os.system('clear')


def gerar_registros_aleatorios(registros, tamanho):

    maiuscula = string.ascii_uppercase
    minuscula = string.ascii_lowercase
    numeros = string.digits

    registros.clear()

    for i in range(tamanho):

        ano = random.randrange(1930, 2020)

        placa = ''.join(random.choice(maiuscula) for _ in range(3))
        placa += ''.join(random.choice(numeros) for _ in range(4))

        dono = ''.join([random.choice(maiuscula)])
        dono += ''.join(random.choice(minuscula)
                        for _ in range(random.randrange(3, 10)))

        modelo = modelos[random.randrange(0, len(modelos))]

        ordemCadastro = i+1

        registro = Registro(ano, placa, dono, modelo, ordemCadastro)
        registros.append(registro)


def registro_unico(registros, ano, placa, dono, modelo):
    ordemCadastro = len(registros) + 1
    registro = Registro(ano, placa, dono, modelo, ordemCadastro)
    registros.append(registro)


"""
def mostrar_registros(registros, tamanho):
    linha = '-' * 83
    print(linha)

    print("|{:^81}|".format("REGISTROS DE {} VEICULOS CADASTRADOS".format(tamanho)))
    print(linha)
    print('|      MODELO      |   PLACA   |   ANO   |      DONO      |   ORDEM DE CADASTRO   |')
    print(linha)
    for i in range(tamanho):
        print("|{:^18}|{:^11}|{:^9}|{:^16}|{:^23}|".format(
            registros[i].modelo, registros[i].placa, registros[i].ano, registros[i].dono, registros[i].ordemCadastro
        ))
        print(linha)
    mostrar_tabela(registros, tamanho)
"""


def mostrar_registros(registros, tamanho):

    modelos = []
    placas = []
    anos = []
    donos = []
    ordemCadastros = []

    for i in range(tamanho):
        modelos.append(registros[i].modelo)
        placas.append(registros[i].placa)
        anos.append(registros[i].ano)
        donos.append(registros[i].dono)
        ordemCadastros.append(registros[i].ordemCadastro)

    indices = ['<b>MODELOS</b>', '<b>PLACA</b>', '<b>ANO</b>',
               '<b>DONO</b>', '<b>ORDEM DE CADASTRO</b>']
    trace = go.Table(
        header=dict(
            values=indices,
            line=dict(color='#000'),
            fill=dict(color='blue'),
            font=dict(color='#fff', size=20)
        ),
        cells=dict(
            values=[modelos, placas, anos, donos, ordemCadastros],
            font=dict(color='#000', size=14),
            fill=dict(color='#F1F8FB'),
            height=25
        )
    )

    data = [trace]
    plotly.offline.plot(data, filename='registros.html')


def comparar_ordenacoes(registros, desordenado):
    lista_tempos = {}

    # Merge Sort - MS
    registros = desordenado.copy()
    inicio = time.time()
    merge_sort(registros)
    fim = time.time()
    lista_tempos['MS'] = (fim - inicio)

    # Quick Sort (Instavel e Recursivo) - QSIR
    registros = desordenado.copy()
    inicio = time.time()
    quick_sort_inst_rec(registros, 0, len(registros)-1)
    fim = time.time()
    lista_tempos['QSIR'] = (fim - inicio)

    # Quick Sort (Estavel e Recursivo) - QSER
    registros = desordenado.copy()
    inicio = time.time()
    registros = quick_sort_est_rec(registros)
    fim = time.time()
    lista_tempos['QSER'] = (fim - inicio)

    # Quick Sort (Instavel e Interativo) - QSII
    registros = desordenado.copy()
    inicio = time.time()
    quick_sort_inst_iterat(registros, 0, len(registros)-1)
    fim = time.time()
    lista_tempos['QSII'] = (fim - inicio)

    # Bucket Sort - BS
    registros = desordenado.copy()
    inicio = time.time()
    bucket_sort(registros)
    fim = time.time()
    lista_tempos['BS'] = (fim - inicio)

    tipos = ['Merge Sort', 'Quick Sort IR',
             'Quick Sort ER', 'Quick Sort II', 'Bucket Sort']
    tempos = [lista_tempos['MS'], lista_tempos['QSIR'],
              lista_tempos['QSER'], lista_tempos['QSII'], lista_tempos['BS']]

    _, ax = plt.subplots(figsize=(16, 9))
    ax.set(xlabel='Metodo de Ordenacao', ylabel='Tempo (s)')
    plt.figure(1)
    plt.bar(tipos, tempos)

    for i, v in enumerate(tempos):
        plt.text(i-0.4, max(tempos)/100, " "+str(v), color='black',
                 va='center', fontweight='bold', fontsize=12)

    plt.suptitle(
        'Tempo em segundos para ordenar {} registros'.format(len(registros)))
    plt.show()


def comparacoes():
    registro = []
    # merge = np.array([])
    quickSortIR = np.array([])
    quickSortER = np.array([])
    quickSortII = np.array([])
    bucket = np.array([])
    merge = []

    for i in range(19):
        gerar_registros_aleatorios(registro, 2**(i+1))
        desordenado = registro.copy()
        # ordenar e guardar os tempos

        # Merge Sort - MS
        registro = desordenado.copy()
        inicio = time.time()
        merge_sort(registro)
        fim = time.time()
        merge = np.append(merge, (fim - inicio))
        # merge.append(fim - inicio)

        # Bucket Sort - BS
        registro = desordenado.copy()
        inicio = time.time()
        bucket_sort(registro)
        fim = time.time()
        bucket = np.append(bucket, (fim - inicio))
        # bucket.append(fim - inicio)

        if i <= 15:
            # Quick Sort (Instavel e Recursivo) - QSIR
            registro = desordenado.copy()
            inicio = time.time()
            quick_sort_inst_rec(registro, 0, len(registro)-1)
            fim = time.time()
            quickSortIR = np.append(quickSortIR, (fim - inicio))
            #quickSortIR.append(fim - inicio)
            
            
            # Quick Sort (Estavel e Recursivo) - QSER
            registro = desordenado.copy()
            inicio = time.time()
            registro = quick_sort_est_rec(registro)
            fim = time.time()
            quickSortER = np.append(quickSortER, (fim - inicio))
            #quickSortER.append(fim - inicio)

            # Quick Sort (Instavel e Interativo) - QSII
            registro = desordenado.copy()
            inicio = time.time()
            quick_sort_inst_iterat(registro, 0, len(registro)-1)
            fim = time.time()
            quickSortII = np.append(quickSortII, (fim - inicio))
            # quickSortII.append(fim - inicio)
            

        print(merge)
        print(quickSortER)
        print(quickSortII)
        print(quickSortIR)
        print(bucket)

    # Data for plotting
    x = np.array([])

    for i in range(19):
        z = 2**(i+1)
        x = np.append(x, z)

        if i <= 15:
            t_menor = np.copy(x)
        # x.append(z)

    t = x

    fig, ax = plt.subplots()
    ax.set_title('Comparação entre os Algoritmos')
    ax.set(xlabel='Quantidade de elementos', ylabel='Tempo (s)')
    line1, = ax.plot(t, merge, lw=2, color='red', label='Merge Sort')
    line2, = ax.plot(t, bucket, lw=2, color='blue', label='BucketSort')
    line3, = ax.plot(t_menor, quickSortIR, lw=2, color='green', label='QuickSort IR')
    line4, = ax.plot(t_menor, quickSortII, lw=2, color='cyan', label='QuickSort II')
    line5, = ax.plot(t_menor, quickSortER, lw=2, color='pink', label='QuickSort ER')
    leg = ax.legend(loc='upper left', fancybox=True, shadow=True)
    leg.get_frame().set_alpha(0.4)


    # we will set up a dict mapping legend line to orig line, and enable
    # picking on the legend line
    lines = [line1, line2, line3, line4, line5]
    lined = dict()
    for legline, origline in zip(leg.get_lines(), lines):
        legline.set_picker(5)  # 5 pts tolerance
        lined[legline] = origline


    def onpick(event):
        # on the pick event, find the orig line corresponding to the
        # legend proxy line, and toggle the visibility
        legline = event.artist
        origline = lined[legline]
        vis = not origline.get_visible()
        origline.set_visible(vis)
        # Change the alpha on the line in the legend so we can see what lines
        # have been toggled
        if vis:
            legline.set_alpha(1.0)
        else:
            legline.set_alpha(0.2)
        fig.canvas.draw()

    fig.canvas.mpl_connect('pick_event', onpick)

    plt.show()

    print(merge)
    print(quickSortER)
    print(quickSortII)
    print(quickSortIR)
    print(bucket)

        # printar grafico

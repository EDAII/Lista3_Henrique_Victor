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
    mostrar_tabela(registros, tamanho);

def mostrar_tabela(registros, tamanho):

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
    
    indices = ['MODELOS', 'PLACA', 'ANO', 'DONO', 'ORDEM DE CADASTRO']
    trace = go.Table(
        header=dict(values=indices),
        cells=dict(values=[modelos, placas, anos, donos, ordemCadastros]))

    data = [trace]
    plotly.offline.plot(data, filename = 'basic_table')


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

    tipos = ['Merge Sort', 'Quick Sort IR', 'Quick Sort ER', 'Quick Sort II', 'Bucket Sort']
    tempos = [lista_tempos['MS'], lista_tempos['QSIR'], lista_tempos['QSER'], lista_tempos['QSII'], lista_tempos['BS']]

    _, ax = plt.subplots(figsize=(16, 9))
    ax.set(xlabel='Metodo de Ordenacao', ylabel='Tempo (s)')
    plt.figure(1)
    plt.bar(tipos, tempos)

    for i, v in enumerate(tempos):
        plt.text(i-0.4, max(tempos)/100, " "+str(v), color='black', va='center', fontweight='bold', fontsize=12)
                
    plt.suptitle('Tempo em segundos para ordenar {} registros'.format(len(registros)))
    plt.show()


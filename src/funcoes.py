import os
import random
import string
import time
import matplotlib
import matplotlib.pyplot as plt
from registros import Registro
from ordenacoes import *

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
    'RAM 2500'
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


def registro_unico(registros):
    modelo = input("Digite o modelo do veiculo: ")
    while len(modelo) > 18:
        modelo = input("Nome do modelo muito grande, escreva uma versão reduzida: ")

    placa = input("Digite a placa do veiculo: ")
    while len(placa) >  7:
        placa = input("Placa incorreta, digite novamente: ")

    ano = input("Digite o ano do veiculo: ")
    while len(ano) > 4:
        ano = input("Ano incorreto, tente novamente: ")
    
    dono = input("Digite o nome do dono do veiculo: ")
    while len(dono) > 16:
        dono = input("Nome muito grande, escreva um nome menor: ")
    
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


def comparar_ordenacoes(registros, desordenado):
    lista_tempos = {}

    # Merge Sort - MS
    registros = desordenado.copy()
    print('Merge Sort')
    inicio = time.time()
    merge_sort(registros)
    fim = time.time()         
    lista_tempos['MS'] = (fim - inicio)
    print('Tempo decorrido:',lista_tempos['MS'], 's\n')
    
    # Quick Sort (Instavel e Recursivo) - QSR
    registros = desordenado.copy()
    print('Quick Sort (Instavel e Recursivo)')
    inicio = time.time()
    quick_sort_recursivo(registros, 0, len(registros)-1)
    fim = time.time()         
    lista_tempos['QSR'] = (fim - inicio)
    print('Tempo decorrido:',lista_tempos['QSR'], 's\n')
    
    # Quick Sort (Estavel) - QSE
    registros = desordenado.copy()
    print('Quick Sort (Estavel)')
    inicio = time.time()
    registros = quick_sort_estavel(registros)
    fim = time.time()         
    lista_tempos['QSE'] = (fim - inicio)
    print('Tempo decorrido:',lista_tempos['QSE'], 's\n')
    
    # Bucket Sort - BS
    registros = desordenado.copy()
    print('Bucket Sort')
    inicio = time.time()
    bucket_sort(registros)
    fim = time.time()         
    lista_tempos['BS'] = (fim - inicio)
    print('Tempo decorrido:',lista_tempos['BS'], 's\n')

    tipos = ['MS', 'QSR', 'QSE', 'BS']
    tempos = [lista_tempos['MS'], lista_tempos['QSR'], lista_tempos['QSE'], lista_tempos['BS']]

    _, ax = plt.subplots(figsize=(16, 9))
    ax.set(xlabel='Metodo de Ordenacao', ylabel='Tempo (s)')
    plt.figure(1)
    plt.bar(tipos, tempos)

    for i, v in enumerate(tempos):
        plt.text(i-0.4, max(tempos)/100, " "+str(v), color='black', va='center', fontweight='bold', fontsize=12)
                
    plt.suptitle('Tempo em segundos para ordenar {} registros'.format(len(registros)))
    plt.show()
                
    clear()
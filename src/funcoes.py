import os
import random
import string
import matplotlib
import matplotlib.pyplot as pyplot
from registros import Registro

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

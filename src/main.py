from funcoes import *
from ordenacoes import *
import time

def menu():
    os.system('clear')
    print('ESCOLHA UMA OPCAO:\n')

    print('1. Gerar ? Aleatoriamente')
    print('2. Cadastrar ? Individual')
    print('3. Ordenar com Merge Sort')
    print('4. Ordenar com ? Sort')
    print('5. Ordenar com ? Sort')
    print('0. Encerrar Programa')
    print('')

if __name__ == '__main__':
    while True:
        menu()
        opcao = int(input('Opcao: '))
        if opcao == 1:
            print('Opcao escolhida: Gerar ? Aleatoriamente')
            # Funcao
            clear()
        elif opcao == 2:
            print('Opcao escolhida: Cadastrar ? Individual')
            # Funcao
            clear()
        elif opcao == 3:
            print('Opcao escolhida: Ordenar com Merge Sort')
            # Funcao
            clear()
        elif opcao == 4:
            print('Opcao escolhida: Ordenar com ? Sort')
            # Funcao
            clear()
        elif opcao == 5:
            print('Opcao escolhida: Ordenar com ? Sort')
            # Funcao
            clear()
        elif opcao == 0:
            print('Encerrando programa')
            break
        else:
            print('Opcao Invalida')
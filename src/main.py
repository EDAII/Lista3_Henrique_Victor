from funcoes import *
from ordenacoes import *
import time

def menu():
    os.system('clear')
    print('ESCOLHA UMA OPCAO:\n')

    print('1. Gerar Registros Aleatoriamente')
    print('2. Cadastrar Registro Individual')
    print('3. Ordenar com Merge Sort')
    print('4. Ordenar com Quick Sort (Instavel e Recursivo)')
    print('5. Ordenar com Quick Sort (Estavel)')
    print('10. Ordenar com Bucket Sort')
    print('6. Mostrar Registros (Desordenado)')
    print('7. Mostrar Registros (Ordenado)')
    print('8. Comparar Metodos de Ordenacao')
    print('0. Encerrar Programa\n')

if __name__ == '__main__':
    registros = []
    desordenado = []
    ordenado = False
    while True:
        menu()
        opcao = int(input('Opcao: '))
        if opcao == 1:
            print('Opcao escolhida: Gerar Registros Aleatoriamente')
            tamanho = int(input('Digite quantos registros voce quer criar: '))

            while tamanho < 1:
                tamanho = int(input('Tamanho nao pode ser menor que 1, tente novamente: '))
            
            inicio = time.time()
            gerar_registros_aleatorios(registros, tamanho)
            fim = time.time()
            tempo_total = fim - inicio
            print('{} registros gerados.'.format(len(registros)))
            print('Tempo decorrido:',round(tempo_total, 6), 's\n')
            desordenado = registros.copy()

            ordenado = False
            clear()
        elif opcao == 2:
            print('Opcao escolhida: Cadastrar Registro Individual')
            registro_unico(registros)
            ordenado = False
            clear()
        elif opcao == 3:
            if len(registros) > 0:
                print('Opcao escolhida: Ordenar com Merge Sort')
                inicio = time.time()
                merge_sort(registros)
                fim = time.time()
                tempo_total = fim - inicio
                print('\nTempo decorrido:',round(tempo_total, 6), 's')
                print('A Ordenacao terminou.\n')
                ordenado = True
            else:
                print('Nao ha nenhum registro.')

            clear()
        elif opcao == 4:
            if len(registros) > 0:
                print('Opcao escolhida: Ordenar com Quick Sort (Instavel e Recursivo)')
                inicio = time.time()
                quick_sort_recursivo(registros, 0, len(registros)-1)
                fim = time.time()
                tempo_total = fim - inicio
                print('\nTempo decorrido:',round(tempo_total, 6), 's')
                print('A Ordenacao terminou.\n')
                ordenado = True
            else:
                print('Nao ha nenhum registro.')

            clear()


        elif opcao == 10:
            if(len(registros) > 0):
                print('Opcao escolhida: Ordenar com Bucket Sort')
                inicio = time.time()
                bucket_sort(registros)
                fim = time.time()
                tempo_total = fim - inicio
                print("\nTempo decorrido:", round(tempo_total, 6), 's')
                print('A Ordenacao terminou.\n')
                ordenado = True
            else:
                print("nao ha registros")
            
            clear()
        elif opcao == 5:
            if len(registros) > 0:
                print('Opcao escolhida: Ordenar com Quick Sort (Estavel)')
                inicio = time.time()
                registros = quick_sort_estavel(registros)
                fim = time.time()
                tempo_total = fim - inicio
                print('\nTempo decorrido:',round(tempo_total, 6), 's')
                print('A Ordenacao terminou.\n')
                ordenado = True
            else:
                print('Nao ha nenhum registro.')

            clear()
        elif opcao == 6:
            if len(registros) > 0:
                print('Opcao escolhida: Mostrar Registros (Desordenado)')
                print("Ha {} registros".format(len(registros)))
                tamanho = int(input('Quantos registros voce quer ver? '))

                while tamanho > len(registros):
                    tamanho = int(input('Tamanho nao pode ser maior que o maximo de registros, tente novamente: '))

                mostrar_registros(registros, tamanho)
            else:
                print('Nao ha nenhum registro.')
                
            clear()
        elif opcao == 7:
            print('Opcao escolhida: Mostrar Registros (Ordenado)')
            if ordenado == True:
                print("Ha {} registros".format(len(registros)))
                tamanho = int(input('Quantos registros voce quer ver? '))

                while tamanho > len(registros):
                    tamanho = int(input('Tamanho nao pode ser maior que o maximo de registros, tente novamente: '))

                mostrar_registros(registros, tamanho)
            else:
                print('Primeiro use algum mecanismo de ordenacao para ver os registros.')

            clear()
        elif opcao == 8:
            print('Opcao escolhida: Comparar Metodos de Ordenacao')
            # Funcao
            clear()
        elif opcao == 0:
            print('Encerrando programa')
            break
        else:
            print('Opcao Invalida')
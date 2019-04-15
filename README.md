# LISTA 3 - ESTRUTURA DE DADOS 2 - 2019/1

### Henrique Martins de Messias - 17/0050394
### Victor Rodrigues Silva - 16/0019516

<br>

### Instalações necessárias
- No teminal, digite o seguinte comando para instalar as dependências:
  ```bash
    $ pip3 install -r requirements.txt
  ```


### Instruções de uso

- No terminal, vá até o diretório do exercício, que contém, além de arquivos como o README, a pasta "src"
- Digite o seguinte comando:

  ```bash
    $ cd src
  ```

- Para executar o código, digite:

  ```bash
    $ python3 main.py
  ```

### Detalhes da Lista 3

O software deste repositório é de um <b>Registro de Carros</b>.

Cada registro possui as seguintes informações:
 - Ano em que o veículo foi fabricado (ano)
 - Placa do veículo (placa)
 - Nome do dono do veículo (dono)
 - Modelo do veículo (modelo)
 - Número que indica em que ordem o veículo foi cadastrado (ordemCadastro)

O usuário pode criar uma quantidade determinada de registros aleatórios, ou criar um registro individual, ao inserir os dados necessários.

A partir do momento em que houver registros, o usuário pode ordená-los com:
 - Merge Sort
 - Quick Sort (Instavel e Recursivo)
 - Quick Sort (Estavel e Recursivo)
 - Quick Sort (Instavel e Interativo)
 - Bucket Sort

O usuário pode visualizar todos os registros, quandou houver algum para ver. Ele pode ver em ordem de cadastro ou ordenado pelo ano do veículo.

Se quiser, o usuário pode comparar os métodos de ordenação de duas maneiras diferentes:
 - Comparar o tempo que cada método leva para ordenar os registros atuais
 - Comparar o tempo que cada método leva para ordenar registros aleatórios de tamanhos diferentes

O usuário pode também salvar os registros em um arquivo e carregar os dados de um arquivo no programa.
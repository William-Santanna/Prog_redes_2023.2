def gerar_lista(quantidade:int, minimo:int=1, maximo:int=1000000):
    import random
    lista = []
    gerada = False
    try:
        for _ in range(0,quantidade):
            lista.append(random.randint(minimo, maximo))
        gerada = True
    except:
        lista = None
    return(gerada, lista)
#-------------------------------------------------------------------------------------

def salvar_lista(nome_lista: list, nome_arquivo: str, diretorio_programa: str):
    import os
    sucesso  = False

    caminho_arquivo = os.path.join(diretorio_programa, nome_arquivo)
    try:
        with open(caminho_arquivo, 'w') as arquivo:
            for item in nome_lista:
                arquivo.write(str(item) + '\n')
        sucesso = True
    except:
        print(f"Erro ao salvar a lista.")
    return sucesso
#-------------------------------------------------------------------------------------

def ler_arquivo(nome_arquivo: str, diretorio: str):
    import os,sys
    lido = False
    lista = []

    caminho_completo = os.path.join(diretorio, nome_arquivo)

    if os.path.isfile(caminho_completo):
        with open(caminho_completo, 'r') as arquivo:
            conteudo = arquivo.readlines()
            for linha in conteudo:
                lista.append(linha.strip())
            lido = True
    else:
        print(f"O arquivo {nome_arquivo} não foi encontrado no diretório do programa.")
        sys.exit()

    if not lido:
        lista = None

    return lido, lista
#-------------------------------------------------------------------------------------

def ordena_lista(nome_lista: list, metodo_ordena: str):
    bool_ordenada = False
    lista_ordenada = []

    if metodo_ordena   == "BUBBLE":
        lista_ordenada = ordena_bubble(nome_lista)
        bool_ordenada  = True
    elif metodo_ordena == "INSERTION":
        lista_ordenada = ordena_insertion(nome_lista)
        bool_ordenada  = True
    elif metodo_ordena == "SELECTION":
        lista_ordenada = ordena_selection(nome_lista)
        bool_ordenada  = True
    elif metodo_ordena == "QUICK":
        lista_ordenada = ordena_quick(nome_lista)
        bool_ordenada  = True

    if bool_ordenada == False:
        lista_ordenada = None

    return bool_ordenada, lista_ordenada
#-------------------------------------------------------------------------------------

def ordena_bubble(lista: list):
    ordenada = False
    for i in range(len(lista)):
        for j in range(len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    ordenada = verifica_ordenacao(lista)
    if ordenada == False:
        lista = None
    return ordenada, lista
#-------------------------------------------------------------------------------------

def ordena_insertion(lista: list):
    ordenada = False
    for i in range(len(lista)):
        for j in range(i, 0, -1):
            if lista[j] < lista[j - 1]:
                lista[j], lista[j - 1] = lista[j - 1], lista[j]
    ordenada = verifica_ordenacao(lista)
    if ordenada == False:
        lista = None
    return True, lista
#-------------------------------------------------------------------------------------

def ordena_selection(lista: list):
    for i in range(len(lista)):
        menor = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[menor]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
    ordenada = verifica_ordenacao(lista)
    if ordenada == False:
        lista = None
    return ordenada, lista
#-------------------------------------------------------------------------------------

def ordena_quick(lista):
    def partition(arr, low, high):
        i = low - 1
        pivot = arr[high]
        for j in range(low, high):
            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort(arr, low, pi - 1)
            quick_sort(arr, pi + 1, high)

    quick_sort(lista, 0, len(lista) - 1)
    return True, lista

#-------------------------------------------------------------------------------------

def verifica_ordenacao(lista):
    ordenada = True
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            ordenada = False
            break

    return ordenada
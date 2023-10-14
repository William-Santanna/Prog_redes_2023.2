import os,sys
dir_app = os.path.abspath(__file__)
dir_app = os.path.dirname(dir_app)
dir_lib = dir_app + '\\funcoes'
sys.path.append(dir_lib)

import funcoes

nome_arquivo = input("Digite o nome do arquivo (sem a extensão .txt): ")

nome_arquivo += ".txt"

lido, lista = funcoes.ler_arquivo(nome_arquivo, dir_app)
if lido:
    print(lista)
else:
    print("O arquivo não foi lido com sucesso.")
    sys.exit()

metodo_ordena = input("Qual método de ordenamento deseja?\n"
                     "Digite 1 para BUBBLE\n"
                     "Digite 2 para INSERTION\n"
                     "Digite 3 para SELECTION\n"
                     "Digite 4 para QUICK\n")

if metodo_ordena == '1':
    metodo_ordena = "BUBBLE"
    lista_ordenada = funcoes.ordena_bubble(lista)
    print("Você escolheu BUBBLE.")
elif metodo_ordena == '2':
    metodo_ordena = "INSERTION"
    lista_ordenada = funcoes.ordena_insertion(lista)
    print("Você escolheu INSERTION.")
elif metodo_ordena == '3':
    metodo_ordena = "SELECTION"
    lista_ordenada = funcoes.ordena_selection(lista)
    print("Você escolheu SELECTION.")
elif metodo_ordena == '4':
    metodo_ordena = "QUICK"
    lista_ordenada = funcoes.ordena_quick(lista)
    print("Você escolheu QUICK.")
else:
    print("Digite uma opção de ordenamento válida")
    sys.exit()
print(lista_ordenada)

if lista_ordenada[0]:
    diretorio_programa = os.path.dirname(os.path.abspath(__file__))
    retSalvarArquivo = funcoes.salvar_lista(lista_ordenada[1], 'valoresordenados' + metodo_ordena + '.txt', diretorio_programa)

if retSalvarArquivo:
    print('\nArquivo Salvo com Sucesso.')
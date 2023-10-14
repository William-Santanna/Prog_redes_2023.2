import sys, os
dir_app = os.path.abspath(__file__)
dir_app = os.path.dirname(dir_app)
dir_lib = dir_app + '\\funcoes'
sys.path.append(dir_lib)

import funcoes


#-------------------------------------------------------------------------------------

try:
    quantidade = int(input("digite a quantidade de numeros:"))
    if quantidade <= 0:
        print(f'\nDigite um valor positivo válido')
        sys.exit()
    minimo     = int(input("digite o valor mínimo:"))
    maximo     = int(input("digite o valor máximo:"))
    if maximo <= minimo:
        print(f'\nO minimo digitado é maior que o máximo')
        sys.exit()
except ValueError:
    print(f'\nDigite um valor inteiro válido')
    sys.exit()
except:
    print(f'\nERRO DESCONHECIDO: {sys.exc_info()[0]}')
    sys.exit()


retGerarLista= funcoes.gerar_lista(quantidade, minimo,maximo)

if retGerarLista[0]:
    diretorio_programa = os.path.dirname(os.path.abspath(__file__))
    retSalvarArquivo = funcoes.salvar_lista(retGerarLista[1], 'valores_nao_ordenados.txt', diretorio_programa)

if retSalvarArquivo:
    print('\nArquivo Salvo com Sucesso.')
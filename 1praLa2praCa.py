from tabulate import tabulate

path = 'text.txt'
print(path)


def read_question(path):
    try: 
        with open(path, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            return(conteudo)
    except FileNotFoundError: 
        print(f"O arquivo não foi encontrado no {path}")
    except Exception as e:
        print(f"Erro ocorrido em ler o arquivo: {e}")
    return None






# ler_conteudo = read_question(path)
# if ler_conteudo is not None:
#     print(ler_conteudo)

matriz = [[f'({colum},{row})' for row in range(16)] for colum in range(16)]

def imprimir_matriz_com_linhas_adicionais(matriz):
    tabela = tabulate(matriz, tablefmt='pretty')
    tabela_linhas = tabela.split('\n')

    
    for i in range(7, len(tabela_linhas), 6):
        tabela_linhas.insert(i, '-' * len(tabela_linhas[i]))

    tabela_com_linhas_adicionais = '\n'.join(tabela_linhas)
    print(tabela_com_linhas_adicionais)
# imprimir_matriz_com_linhas_adicionais(matriz)

def positionMatriz(matriz, cordenation, valor):
    try: 
        linha, coluna = map(int, cordenation.split(','))
        if 0 <= linha < 16 and 0 <= coluna <16:
            matriz[linha][coluna] = valor
        else: 
            print("Posição inválida, fora dos limites da  matriz(0-15).")
    except ValueError as e:
        print(f"{e}forato da cordenadas ta invalido: x,y ")

while True: 
    imprimir_matriz_com_linhas_adicionais(matriz)
    entrada = input("informe as cordenas (linha, coluna) e  o valor e o valor (Exemplo: 1,0 Pedro):")
    if entrada.lower() == 'sair':
        break
    partes = entrada.split(' ', 1)
    if len(partes) == 2:
        cordenation, valor = partes
        positionMatriz(matriz, cordenation, valor)
    else: 
        print("Formato de entrada inválido. Use (linha, coluna) valor.")
        
imprimir_matriz_com_linhas_adicionais(matriz)
        
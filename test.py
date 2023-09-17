from tabulate import tabulate
import os
import re

matriz = [[f'({colum},{row})' for row in range(16)] for colum in range(16)]

def imprimir_matriz_com_linhas_adicionais(matriz):
    tabela = tabulate(matriz, tablefmt='pretty')
    tabela_linhas = tabela.split('\n')

    
    for i in range(7, len(tabela_linhas), 6):
        tabela_linhas.insert(i, '-' * len(tabela_linhas[i]))

    tabela_com_linhas_adicionais = '\n'.join(tabela_linhas)
    return tabela_com_linhas_adicionais
    

# Função para inserir um valor em uma coordenada específica
def inserir_valor_na_matriz(matriz, coordenadas, valor):
    try:
        linha, coluna = map(int, coordenadas.split(','))
        if 0 <= linha < 16 and 0 <= coluna < 16:
            matriz[linha][coluna] = valor
        else:
            print("Coordenadas fora dos limites da matriz (0-15).")
    except ValueError:
        print("Formato de coordenadas inválido. Use (linha, coluna) para inserir valores.")

# Função para inserir valores em uma linha específica
def inserir_valores_na_linha(matriz, linha, valores):
    try:
        linha = int(linha)
        if 0 <= linha < 16:
            matriz[linha][:len(valores)] = valores
        else:
            print("Linha fora dos limites da matriz (0-15).")
    except ValueError:
        print("Número de linha inválido.")

# Função para inserir valores em várias coordenadas consecutivas a partir de uma coordenada de referência
def inserir_valores_em_multiplas_coordenadas(matriz, coordenadas, valores):
    try:
        linha, coluna = map(int, coordenadas.split(','))
        if 0 <= linha < 16 and 0 <= coluna < 16:
            for i, valor in enumerate(valores):
                if coluna + i < 16:
                    matriz[linha][coluna + i] = valor
                else:
                    print("Linha da matriz preenchida completamente.")
                    break
        else:
            print("Coordenadas de referência fora dos limites da matriz (0-15).")
    except ValueError:
        print("Formato de coordenadas inválido. Use (linha, coluna) para inserir valores.")

def inserir_valores_em_multiplas_coordenadas_coluns(matriz, coordenadas, valores):
    try:
        linha, coluna = map(int, coordenadas.split(','))
        
        if 0 <= coluna < 16 and 0 <= linha < 16:
            for i, valor in enumerate(valores):
                if coluna + i < 16:
                    matriz[linha + i][coluna] = valor
                else:
                    print("Linha da matriz preenchida completamente.")
                    break
        else:
            print("Coordenadas de referência fora dos limites da matriz (0-15).")
    except ValueError:
        print("Formato de coordenadas inválido. Use (linha, coluna) para inserir valores.")
    
def limpar_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
def pularLine(qtd):
    for _ in range(qtd):
        print()
    

                            
def parametros(entrada):
   
    while True:
        partes = entrada.split(' ')
        if '-Lp' in entrada:
            coordenadas, valor = partes[0], partes[2:]
            if partes[1] == '-Lp':
                inserir_valores_em_multiplas_coordenadas(matriz, coordenadas, valor)
                break
            else:
                print(f"A parte 1 é {partes[1]}")
                break
        elif '-l' in entrada:
            linha, valor = partes[0], partes[2:]
            inserir_valores_na_linha(matriz, linha, valor)
            break
        elif '-c ' in entrada:
            coordenadas, valor = partes[0], partes[2:]
            if partes[1] == '-c':
                inserir_valores_em_multiplas_coordenadas_coluns(matriz, coordenadas, valor)
                break
        elif ',' in entrada:
            coordenadas, valor = partes[0], partes[1:]
            inserir_valor_na_matriz(matriz, coordenadas, ''.join(valor))
            break

        elif '-clear '.strip() in entrada:
            limpar_terminal()
            break
        
        

        else:
            if partes == '':
                continue
            print("Comando inválido. Use (linha, coluna) valor, -l linha valor ou -lp coordenadas valor.")
            break

def inserir_valores_na_matriz(matriz):
    intregex = r'-pl=(\d+)'
    while True:
        entrada = input("Informe as coordenadas e os valores (Exemplo: 0,1 Pedro ou 1 -l Ana Maria Joao): ")
        if entrada.lower() == 'sair':
            break
    def verbose():
        if '-V' in entrada:
            clearInt = entrada.strip()
            if len(clearInt) >= 3:
                entrada = entrada.replace('-V','').strip()
                parametros(entrada) 
                print(imprimir_matriz_com_linhas_adicionais(matriz))
                clearInt = None
                inserir_valores_na_matriz(matriz) 
            else: 
                print(imprimir_matriz_com_linhas_adicionais(matriz))
                inserir_valores_na_matriz(matriz)    
                
    def regex():
        correspode = re.search(intregex, entrada)
        if correspode == None:
            parametros(entrada)
            inserir_valores_na_matriz(matriz)            
        if correspode:
           valor_x = int(correspode.group(1)) 
        try: 
            if 0 <= valor_x <= 99:
                pularLine(valor_x)
                if len(entrada) >= 5:
                    parametros(entrada)  
            else: print("Só é permitido pular até 99 linhas.")
        except ValueError as e:
            print(f"Erro no pl\n{e}")
            
        
        
inserir_valores_na_matriz(matriz)

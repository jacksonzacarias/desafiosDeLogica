import sys
from tabulate import tabulate
import os
import re
import msvcrt
import threading
cor_amarela = '\033[93m'
RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"


def sair():
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'\x1b':
                respond = input("Você tem certeza que quer sair 'S' ou 'N': ").strip().upper()
                if respond == 'S':
                    return True
                elif respond == 'N':
                    print("Continuando...")
                    break
                else: 
                    print("Resposta inválida. Digite 'S' para sair ou 'N' para continuar.")
                    continue
thread_esc = threading.Thread(target=sair)
thread_esc.start()


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
            if re.search(r'S', valor):
                valor_formatado = re.sub(r'S', f'{GREEN}S{RESET}', valor)
                matriz[linha][coluna] = valor_formatado
            else:
                valor_formatado = re.sub(r'N', f'{RED}N{RESET}', valor)
                matriz[linha][coluna] = valor_formatado
           
        else:
            print("Coordenadas fora dos limites da matriz (0-15).")
    except ValueError:
        print("Formato de coordenadas inválido. Use (linha, coluna) para inserir valores.")

# Função para inserir valores em uma linha específica
def inserir_valores_na_linha(matriz, linha, valores):
    try:
        linha = int(linha)
        if 0 <= linha < 16:
            linha_formata = []
            for char in valores:
                if re.search(r'(?<!\w)S(?!\w)', char):
                    valor_formatado = re.sub(r'S', f'{GREEN}S{RESET}', char)
                    linha_formata.append(valor_formatado)
                elif re.search(r'(?<!\w)N(?!\w)', char):
                    valor_formatado = re.sub(r'N', f'{RED}N{RESET}', char)
                    linha_formata.append(valor_formatado)
                else: 
                    linha_formata.append(char)
            matriz[linha][:len(valores)] = linha_formata

        else:
            print("Linha fora dos limites da matriz (0-15).")
    except ValueError:
        print("Número de linha inválido exp de uso(: 1 -l N N S)")
        
def regexSN(valor):
    if re.search(r'(?<!\w)S(?!\w)', valor):
        valor_formatado = re.sub(r'S', f'{GREEN}S{RESET}', valor)
        return valor_formatado
    elif re.search(r'(?<!\w)N(?!\w)', valor):
        valor_formatado = re.sub(r'N', f'{RED}N{RESET}', valor)
        return valor_formatado 
    else: 
        return valor 
        

# Função para inserir valores em várias coordenadas consecutivas a partir de uma coordenada de referência
def inserir_valores_em_multiplas_coordenadas(matriz, coordenadas, valores):
    try:
        linha, coluna = map(int, coordenadas.split(','))
        if 0 <= linha < 16 and 0 <= coluna < 16:
            for i, valor in enumerate(valores):
                if coluna + i < 16:
                    matriz[linha][coluna + i] = regexSN(valor)
                    # if re.search(r'(?<!\w)S(?!\w)', valor):
                    #     valor_formatado = re.sub(r'S', f'{GREEN}S{RESET}', valor)
                    #     matriz[linha + i][coluna] = valor_formatado
                    # elif re.search(r'(?<!\w)N(?!\w)', valor):
                    #     valor_formatado = re.sub(r'N', f'{RED}N{RESET}', valor)
                    #     matriz[linha + i][coluna] = valor_formatado
                    # else: 
                    #     matriz[linha + i][coluna] = valor
                    
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
                    if re.search(r'(?<!\w)S(?!\w)', valor):
                        valor_formatado = re.sub(r'S', f'{GREEN}S{RESET}', valor)
                        matriz[linha + i][coluna] = valor_formatado
                    elif re.search(r'(?<!\w)N(?!\w)', valor):
                        valor_formatado = re.sub(r'N', f'{RED}N{RESET}', valor)
                        matriz[linha + i][coluna] = valor_formatado
                    else: 
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
            print(f"Comando inválido. Use (linha, coluna) valor, -l linha valor ou -lp coordenadas valor.")
            break
        
        
        
def regexpl(entrada):
    intregex = r'-pl=(\d+)'
    corresponde = re.search(intregex, entrada)
    if corresponde: 
        entrada_sem = entrada.replace(corresponde.group(0),'').strip()
        valor_x = int(corresponde.group(1))
        if 0 <= valor_x <= 99:
            return valor_x, entrada_sem
        else: print("Só é permitido pular até 99 linhas.")
    return False   


def verboso(entrada):
    if '-V' in entrada:
        clearInt = entrada.strip()
        if len(clearInt) >= 3:
            entradav = entrada.replace('-V','').strip()
            clearInt = None
            return entradav, True
        else:
            print(imprimir_matriz_com_linhas_adicionais(matriz))
            inserir_valores_na_matriz(matriz)

    return False 
          
        
# def if_key_S(entrada):
#     intregex = r'S'
#     correspondencias = re.finditer(intregex, entrada)
#     if correspondencias:
#         entrada_formatada = entrada
#         offset = 0  # Offset para lidar com a mudança de tamanho ao inserir {RED}S{RESET}
        
#         for correspondencia in correspondencias:
#             posicao_S = correspondencia.start() + offset
#             entrada_formatada = entrada_formatada[:posicao_S] + '{RED}S{RESET}' + entrada_formatada[posicao_S + 1:]
#             offset += 10  # Tamanho de {RED}S{RESET} - 1 = 10 - 1 = 9
#         return entrada_formatada
#     return False
        

def inserir_valores_na_matriz(matriz):
    # while True:
    #     key = msvcrt.getch()
    #     if key == b'\x1b':
    #         sair(True)
    #     else: 
    #         continue
   
        while True:
            entrada = input("Informe as coordenadas e os valores (Exemplo: 0,1 Pedro ou 1 -l Ana Maria Joao): ")
            # key = msvcrt.getch()
    
        
            resut_regexpl = regexpl(entrada)
            result_verbose = verboso(entrada)
            if result_verbose:
                entradav, z = result_verbose
                parametros(entradav)
                print(imprimir_matriz_com_linhas_adicionais(matriz))
                inserir_valores_na_matriz(matriz)
            # elif resut_regexpl and result_verbose:
                    
            
            elif resut_regexpl:
                valo_x, entrada_sem = resut_regexpl
                if len(entrada_sem) >= 1:
                    parametros(entrada_sem)
                    pularLine(valo_x) 
                else:
                    pularLine(valo_x)
                    inserir_valores_na_matriz(matriz)
            else:
                # newentrada = if_key_S(entrada)  
                parametros(entrada)
                inserir_valores_na_matriz(matriz) 
        
        
            
inserir_valores_na_matriz(matriz)
if sair():
    sys.exit()
# key = msvcrt.getch()
# if key == b'\x1b':        
#      sair(True)

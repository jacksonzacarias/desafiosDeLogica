import re

# Sua string de entrada
entrada = "aaa 0,1 -lp -o -pl=3 aaa"

padrao = r'-pl=(\d+)'

correspondencia = re.search(padrao, entrada)

if correspondencia:
    valor_x = int(correspondencia.group(1))  # Obtém o valor de X como um número inteiro
    if 0 <= valor_x <= 99:
        print(valor_x)
    else:
        print("Só é permitido pular até 99 linhas.")
else:
    print("Padrão '-pl=X' não encontrado na entrada.")

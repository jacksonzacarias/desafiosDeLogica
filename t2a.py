import msvcrt

while True:
    key = msvcrt.getch()
    if key == b'\x1b':
        while True:
            resposta = input("Você tem certeza? Digite 'S' para sair ou 'N' para continuar: ").strip().upper()
            if resposta == 'S':
                break
            elif resposta == 'N':
                print("Continuando...")
                break
            else:
                print("Resposta inválida. Digite 'S' para sair ou 'N' para continuar.")
        if resposta == 'S':
            break
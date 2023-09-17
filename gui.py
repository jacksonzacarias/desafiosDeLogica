import tkinter as tk

class MatrizEditor:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Editor de Matriz")
        self.janela.geometry("800x800")

        self.matriz = [['' for _ in range(16)] for _ in range(16)]

        self.largura_celula = 50
        self.altura_celula = 50

        self.canvas = tk.Canvas(self.janela, width=self.largura_celula * 16, height=self.altura_celula * 16, bg="white")
        self.canvas.pack()

        self.estilizador = Estilizador(self.janela)

        self.criar_interface()
        self.iniciar_eventos()

    def criar_interface(self):
        self.estilizador.configurar_botoes()
        self.estilizador.configurar_entradas()
        self.estilizador.configurar_botoes_extra()
        self.exibir_matriz()

    def iniciar_eventos(self):
        self.canvas.bind("<Button-1>", self.posicao_clicada)
        self.canvas.bind("<Double-Button-1>", self.duplo_click)
        self.canvas.bind("<Triple-Button-1>", self.triplo_click)

        self.janela.bind("<Up>", self.mover_teclado)
        self.janela.bind("<Down>", self.mover_teclado)
        self.janela.bind("<Left>", self.mover_teclado)
        self.janela.bind("<Right>", self.mover_teclado)

        self.estilizador.botao_editar.config(command=self.editar_valor_selecionado)
        self.estilizador.botao_limpar_linha.config(command=self.limpar_linha)
        self.estilizador.botao_limpar_coluna.config(command=self.limpar_coluna)

    def posicao_clicada(self, event):
        coluna = event.x // self.largura_celula
        linha = event.y // self.altura_celula
        self.estilizador.entrada_coordenadas.delete(0, tk.END)
        self.estilizador.entrada_coordenadas.insert(0, f"{linha}, {coluna}")

    def duplo_click(self, event):
        coordenadas = self.estilizador.entrada_coordenadas.get().split(', ')
        if coordenadas:
            linha, coluna = int(coordenadas[0]), int(coordenadas[1])
            self.matriz[linha][coluna] = "X"
            self.exibir_matriz()

    def triplo_click(self, event):
        coordenadas = self.estilizador.entrada_coordenadas.get().split(', ')
        if coordenadas:
            linha, coluna = int(coordenadas[0]), int(coordenadas[1])
            self.matriz[linha][coluna] = "V"
            self.exibir_matriz()

    def mover_teclado(self, event):
        if self.estilizador.entrada_coordenadas.get():
            linha, coluna = self.estilizador.entrada_coordenadas.get().split(', ')
            linha, coluna = int(linha), int(coluna)

            if event.keysym == 'Up' and linha > 0:
                linha -= 1
            elif event.keysym == 'Down' and linha < 15:
                linha += 1
            elif event.keysym == 'Left' and coluna > 0:
                coluna -= 1
            elif event.keysym == 'Right' and coluna < 15:
                coluna += 1

            self.estilizador.entrada_coordenadas.delete(0, tk.END)
            self.estilizador.entrada_coordenadas.insert(0, f"{linha}, {coluna}")

    def editar_valor_selecionado(self):
        coordenadas = self.estilizador.entrada_coordenadas.get().split(', ')
        valor = self.estilizador.entrada_valor.get()
        if coordenadas:
            linha, coluna = int(coordenadas[0]), int(coordenadas[1])
            self.matriz[linha][coluna] = valor
            self.exibir_matriz()

    def limpar_linha(self):
        coordenadas = self.estilizador.entrada_coordenadas.get().split(', ')
        if coordenadas:
            linha = int(coordenadas[0])
            self.matriz[linha] = [''] * 16
            self.exibir_matriz()

    def limpar_coluna(self):
        coordenadas = self.estilizador.entrada_coordenadas.get().split(', ')
        if coordenadas:
            coluna = int(coordenadas[1])
            for linha in range(16):
                self.matriz[linha][coluna] = ''
            self.exibir_matriz()

    def exibir_matriz(self):
        self.canvas.delete("all")
        for linha in range(16):
            for coluna in range(16):
                valor = self.matriz[linha][coluna]
                x0 = coluna * self.largura_celula
                y0 = linha * self.altura_celula
                x1 = x0 + self.largura_celula
                y1 = y0 + self.altura_celula
                self.canvas.create_rectangle(x0, y0, x1, y1, outline="gray", fill="white")
                self.canvas.create_text(
                    x0 + self.largura_celula / 2,
                    y0 + self.altura_celula / 2,
                    text=valor,
                    fill="red" if valor == "X" else "green",
                    font=("Helvetica", 12, "bold"),
                )

class Estilizador:
    def __init__(self, janela):
        self.frame_botoes = tk.Frame(janela)
        self.frame_botoes.pack(side=tk.BOTTOM, pady=10)
        self.botao_editar = None
        self.botao_limpar_linha = None
        self.botao_limpar_coluna = None
        self.entrada_coordenadas = None
        self.entrada_valor = None

    # def configurar_botoes(self):
    #     for linha in range(16):
    #         for coluna in range(16):
    #             botao = tk.Button(
    #                 self.frame_botoes,
    #                 text="",
    #                 width=2,
    #                 height=1,
    #                 font=("Helvetica", 12),
    #             )
    #             botao.grid(row=linha, column=coluna, sticky="nsew")

    #     for i in range(16):
    #         self.frame_botoes.grid_rowconfigure(i, weight=1)
    #         self.frame_botoes.grid_columnconfigure(i, weight=1)

    def configurar_entradas(self):
        rotulo_coordenadas = tk.Label(self.frame_botoes, text="Coordenadas (linha, coluna):")
        self.entrada_coordenadas = tk.Entry(self.frame_botoes)
        rotulo_valor = tk.Label(self.frame_botoes, text="Valor:")
        self.entrada_valor = tk.Entry(self.frame_botoes)

        rotulo_coordenadas.grid(row=16, column=0, columnspan=2)
        self.entrada_coordenadas.grid(row=16, column=2, columnspan=2)
        rotulo_valor.grid(row=16, column=4, columnspan=2)
        self.entrada_valor.grid(row=16, column=6, columnspan=2)

    def configurar_botoes_extra(self):
        self.botao_editar = tk.Button(self.frame_botoes, text="Editar")
        self.botao_limpar_linha = tk.Button(self.frame_botoes, text="Limpar Linha")
        self.botao_limpar_coluna = tk.Button(self.frame_botoes, text="Limpar Coluna")

        self.botao_editar.grid(row=17, column=0, columnspan=2)
        self.botao_limpar_linha.grid(row=17, column=2, columnspan=2)
        self.botao_limpar_coluna.grid(row=17, column=4, columnspan=2)

if __name__ == "__main__":
    root = tk.Tk()
    editor = MatrizEditor(root)
    root.mainloop()

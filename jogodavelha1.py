import tkinter as tk


class JogoDaVelhaPet:

  def __init__(self, root):
    self.root = root
    self.root.title("Jogo da Velha - 🐱 vs 🐶")
    self.root.geometry("400x520")
    self.root.resizable(False, False)

    self.EMOJI_1 = "🐱"
    self.EMOJI_2 = "🐶"

    self.COR_FUNDO = "#1e1e2e"
    self.COR_PAINEL = "#181825"
    self.COR_BOTAO = "#313244"
    self.COR_TEXTO = "#cdd6f4"
    self.COR_GATO = "#fab387"
    self.COR_CACHORRO = "#f9e2af"
    self.COR_DESTAQUE = "#a6e3a1"

    self.root.configure(bg=self.COR_FUNDO)

    self.primeiro_a_jogar = self.EMOJI_1
    self.jogador_atual = self.primeiro_a_jogar

    self.tabuleiro = [""] * 9
    self.vencedor = None

    self.criar_header()
    self.criar_grade()
    self.criar_botao_reiniciar()

  def obter_cor_jogador(self, jogador):
    return self.COR_GATO if jogador == self.EMOJI_1 else self.COR_CACHORRO

  def criar_header(self):
    self.frame_header = tk.Frame(self.root, bg=self.COR_FUNDO)
    self.frame_header.pack(pady=20)

    self.label_status = tk.Label(
        self.frame_header,
        text=f"Vez do Jogador: {self.jogador_atual}",
        font=("Helvetica", 18, "bold"),
        bg=self.COR_FUNDO,
        fg=self.obter_cor_jogador(self.jogador_atual),
    )
    self.label_status.pack()

  def criar_grade(self):
    self.frame_grade = tk.Frame(self.root, bg=self.COR_PAINEL, pady=5, padx=5)
    self.frame_grade.pack()

    self.botoes = []
    for i in range(9):
      btn = tk.Button(
          self.frame_grade,
          text="",
          font=("Segoe UI Emoji", 32),
          width=3,
          height=1,
          bg=self.COR_BOTAO,
          fg=self.COR_TEXTO,
          activebackground="#45475a",
          activeforeground=self.COR_TEXTO,
          bd=0,
          relief="flat",
          command=lambda index=i: self.jogar(index),
      )
      row, col = divmod(i, 3)
      btn.grid(row=row, column=col, padx=4, pady=4)
      self.botoes.append(btn)

  def criar_botao_reiniciar(self):
    self.btn_reiniciar = tk.Button(
        self.root,
        text="Reiniciar Jogo",
        font=("Helvetica", 12, "bold"),
        bg="#f38ba8",
        fg="#11111b",
        activebackground="#f5e0dc",
        activeforeground="#11111b",
        bd=0,
        relief="flat",
        padx=20,
        pady=10,
        cursor="hand2",
        command=self.reiniciar,
    )
    self.btn_reiniciar.pack(pady=20)

  def jogar(self, index):
    if self.tabuleiro[index] == "" and not self.vencedor:
      self.tabuleiro[index] = self.jogador_atual

      self.botoes[index].config(
          text=self.jogador_atual,
          state="disabled",
      )

      if self.verificar_vitoria():
        self.vencedor = self.jogador_atual
        self.label_status.config(
            text=f"Jogador {self.vencedor} Venceu!", fg=self.COR_DESTAQUE
        )
      elif "" not in self.tabuleiro:
        self.label_status.config(text="Empate!", fg=self.COR_TEXTO)
      else:
        self.jogador_atual = (
            self.EMOJI_2
            if self.jogador_atual == self.EMOJI_1
            else self.EMOJI_1
        )
        cor_turno = self.obter_cor_jogador(self.jogador_atual)
        self.label_status.config(
            text=f"Vez do Jogador: {self.jogador_atual}", fg=cor_turno
        )

  def verificar_vitoria(self):
    combinacoes = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]

    for a, b, c in combinacoes:
      if (
          self.tabuleiro[a]
          == self.tabuleiro[b]
          == self.tabuleiro[c]
          == self.jogador_atual
      ):
        self.botoes[a].config(bg=self.COR_DESTAQUE)
        self.botoes[b].config(bg=self.COR_DESTAQUE)
        self.botoes[c].config(bg=self.COR_DESTAQUE)
        return True
    return False

  def reiniciar(self):
    self.primeiro_a_jogar = (
        self.EMOJI_2 if self.primeiro_a_jogar == self.EMOJI_1 else self.EMOJI_1
    )
    self.jogador_atual = self.primeiro_a_jogar

    self.tabuleiro = [""] * 9
    self.vencedor = None

    cor_turno = self.obter_cor_jogador(self.jogador_atual)
    self.label_status.config(
        text=f"Vez do Jogador: {self.jogador_atual}", fg=cor_turno
    )

    for btn in self.botoes:
      btn.config(text="", state="normal", bg=self.COR_BOTAO)


if __name__ == "__main__":
  root = tk.Tk()
  app = JogoDaVelhaPet(root)
  root.mainloop()

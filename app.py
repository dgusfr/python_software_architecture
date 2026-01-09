import tkinter as tk
from tkinter import messagebox

atendentes = []


def adicionar_atendente():
    nome = entrada_nome.get().strip()

    if not nome:
        messagebox.showwarning(
            "Entrada Inválida", "O nome do atendente não pode estar vazio."
        )
        return

    if nome in [atendente["nome"] for atendente in atendentes]:
        messagebox.showwarning("Duplicado", f"O atendente '{nome}' já está cadastrado.")
        return

    atendentes.append({"nome": nome, "vendas": 0})
    messagebox.showinfo("Sucesso", f"Atendente '{nome}' adicionado com sucesso.")


janela = tk.Tk()
janela.title("Controle de Vendas")

entrada_nome = tk.Entry(janela)
entrada_nome.pack(pady=5)

janela.mainloop()

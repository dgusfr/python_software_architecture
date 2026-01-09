import tkinter as tk
from tkinter import messagebox

atendentes = []


def adicionar_atendente():
    for widget in janela.winfo_children():

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

    entrada_nome.delete(0, tk.END)


def resetar_atendentes():
    atendentes.clear()
    if messagebox.askyesno(
        "Resetar", "Tem certeza que deseja resetar a lista de atendentes?"
    ):
        atendentes.clear()


def incrementar_venda(nome):
    for atendente in atendentes:
        if atendente["nome"] == nome:
            atendente["vendas"] += 1
            break


janela = tk.Tk()
janela.title("Controle de Vendas")

entrada_nome = tk.Entry(janela)
entrada_nome.pack(pady=5)

# Botões para adicionar e resetar atendentes
botao_adicionar = tk.Button(
    janela, text="Adicionar Atendente", command=adicionar_atendente
)
botao_adicionar.pack()

Botao_resetar = tk.Button(janela, text="Resetar Atendentes", command=resetar_atendentes)
Botao_resetar.pack()

# Iniciar a interface gráfica
janela.mainloop()

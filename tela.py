import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
import sqlite3
from database import gerardb,adicionar_paciente_db, adicionar_medicamento_db, carregar_pacientes_db, carregar_medicamentos_db

gerardb()

root = ctk.CTk()
root.title("MTC - Controle de Medicamentos")
root.geometry("1200x600")  # Ajuste o tamanho da janela

# Função para minimizar a janela principal e abrir a janela de Pacientes
def abrir_janela_pacientes():
    pacientes_janela = ctk.CTkToplevel(root)
    pacientes_janela.title("Pacientes")
    pacientes_janela.geometry("600x400+400+150")  # Ajustado para permitir o Treeview
    pacientes_janela.transient(root)  # Torna a janela sobreposta à principal
    pacientes_janela.deiconify()  # Garante que a janela seja mostrada

    # Frame para o botão e Treeview
    frame_pacientes = ctk.CTkFrame(pacientes_janela)
    frame_pacientes.pack(fill="both", expand=True)

    # Interface para adicionar um paciente
    def adicionar_paciente():
        nome = ctk.CTkInputDialog(title="Nome", text="Nome do paciente:")
        nome_retorno = nome.get_input() 
        idade = ctk.CTkInputDialog(title="Idade", text="Idade do paciente:") # Isso não é bom.
        idade_retorno = idade.get_input() 
        endereco = ctk.CTkInputDialog(title="Endereço", text="Endereço do paciente:")
        endereço_retorno = endereco.get_input()

        if nome_retorno and (idade_retorno.isdigit()) and endereço_retorno:
            idade_retorno = int(idade_retorno) # Gambiarra.
            adicionar_paciente_db(nome_retorno, idade_retorno, endereço_retorno)
            tree_pacientes.delete(*tree_pacientes.get_children())
            carregar_pacientes_db(tree_pacientes)
        else: # Outra gambiarra.
            messagebox.showwarning("Entrada inválida", (not (nome_retorno and idade_retorno and endereço_retorno) and "Alguns campos não foram preenchidos.") or ((not idade_retorno.isdigit()) and "O campo 'Idade' deve conter números."))

    # Botão para adicionar paciente
    btn_adicionar_paciente = ctk.CTkButton(frame_pacientes, text="Adicionar Paciente", command=adicionar_paciente)
    btn_adicionar_paciente.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

    # Treeview para informações dos pacientes
    columns_pacientes = ("Nome", "Idade", "Endereço")
    tree_pacientes = ttk.Treeview(frame_pacientes, columns=columns_pacientes, show="headings", height=15)
    for col in columns_pacientes:
        tree_pacientes.heading(col, text=col)
        tree_pacientes.column(col, width=150, anchor=tk.CENTER)

    # Carregar pacientes na treeview. - ¹ Que nos leva aqui. O recipiente de "carregar_pacientes()" é a própria variável da treeview.
    carregar_pacientes_db(tree_pacientes)
    # Tchau, exemplos. Serão eternamente honrados.

    # Posicionar o Treeview
    tree_pacientes.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    # Ajustar a proporção de colunas
    frame_pacientes.grid_columnconfigure(1, weight=1)

    # Função para restaurar a janela principal ao fechar a janela de Pacientes
    def fechar_janela_pacientes():
        pacientes_janela.destroy()


    pacientes_janela.protocol("WM_DELETE_WINDOW", fechar_janela_pacientes)

# Função para minimizar a janela principal e abrir a janela de Medicamentos
def abrir_janela_medicamentos():
    medicamentos_janela = ctk.CTkToplevel(root)
    medicamentos_janela.title("Medicamentos")
    medicamentos_janela.geometry("600x400+400+150")  # Ajustado para permitir o Treeview
    medicamentos_janela.transient(root)  # Torna a janela sobreposta à principal
    medicamentos_janela.deiconify()  # Garante que a janela seja mostrada

    # Frame para o botão e Treeview
    frame_medicamentos = ctk.CTkFrame(medicamentos_janela)
    frame_medicamentos.pack(fill="both", expand=True)

    # Interface para adicionar medicamento (isso não é o botão; é a função. Também não é o comando da database. O nome das minhas variáveis são terríveis.)
    def adicionar_medicamento():
        nome = ctk.CTkInputDialog(title="Nome", text="Nome do medicamento:")
        nome_retorno = nome.get_input() 
        estoque = ctk.CTkInputDialog(title="Estoque", text="Quantidade em estoque:") # Novamente, isso não é bom porque strings são permitidas.
        estoque_retorno = estoque.get_input() 
        vencimento = ctk.CTkInputDialog(title="Vencimento", text="Data de vencimento:")
        vencimento_retorno = vencimento.get_input() 

        if nome_retorno and (estoque_retorno.isdigit()) and vencimento_retorno:
            estoque_retorno = int(estoque_retorno)
            adicionar_medicamento_db(nome_retorno, estoque_retorno, vencimento_retorno)
            tree_medicamentos.delete(*tree_medicamentos.get_children())
            carregar_medicamentos_db(tree_medicamentos) # Mesma coisa que ¹
        else:
            messagebox.showwarning("Entrada inválida", (not (nome_retorno and estoque_retorno and vencimento_retorno) and "Alguns campos não foram preenchidos.") or ((not estoque_retorno.isdigit()) and "O campo 'Estoque' deve conter números."))

    # Botão para adicionar medicamento
    btn_adicionar_medicamento = ctk.CTkButton(frame_medicamentos, text="Adicionar Medicamento", command=adicionar_medicamento)
    btn_adicionar_medicamento.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

    # Treeview para informações dos medicamentos
    columns_medicamentos = ("Nome do Medicamento", "Estoque", "Vencimento")
    tree_medicamentos = ttk.Treeview(frame_medicamentos, columns=columns_medicamentos, show="headings", height=15)
    for col in columns_medicamentos:
        tree_medicamentos.heading(col, text=col)
        tree_medicamentos.column(col, width=150, anchor=tk.CENTER)

    # Carregar os medicamentos da db na treeview dos medicamentos.  
    carregar_medicamentos_db(tree_medicamentos) # A única mudança, novamente, é que a variável da treeview foi alterada. Talvez eu não odeie métodos tanto agora.

    # Posicionar o Treeview
    tree_medicamentos.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    # Ajustar a proporção de colunas
    frame_medicamentos.grid_columnconfigure(1, weight=1)

    # Função para restaurar a janela principal ao fechar a janela de Medicamentos
    def fechar_janela_medicamentos():
        tree.delete(*tree.get_children())
        carregar_medicamentos_db(tree)
        medicamentos_janela.destroy()

    medicamentos_janela.protocol("WM_DELETE_WINDOW", fechar_janela_medicamentos)

# Frame principal
main_frame = ctk.CTkFrame(root, corner_radius=10)
main_frame.pack(padx=20, pady=20, fill="both", expand=True)

# Frame esquerdo para botões
left_frame = ctk.CTkFrame(main_frame)
left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ns")

# Botão "Pacientes"
btn_pacientes = ctk.CTkButton(left_frame, text="Pacientes", width=150, command=abrir_janela_pacientes)
btn_pacientes.pack(pady=10)

# Botão "Medicamentos"
btn_medicamentos = ctk.CTkButton(left_frame, text="Medicamentos", width=150, command=abrir_janela_medicamentos)
btn_medicamentos.pack(pady=10)

# Frame direito para Treeview
right_frame = ctk.CTkFrame(main_frame)
right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

# Configurar as colunas do Treeview
columns = ("Nome do Medicamento", "Estoque", "Vencimento")
tree = ttk.Treeview(right_frame, columns=columns, show="headings", height=15)

# Definir as colunas
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=200, anchor=tk.CENTER)

# Adicionar algumas linhas de exemplo
# Isso seria substituído pelas informações em tempo real do banco de dados. E foi mesmo.
carregar_medicamentos_db(tree)

# Exibir o Treeview
tree.pack(fill="both", expand=True)

# Configurar redimensionamento
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)

# Rodar o aplicativo
root.mainloop()

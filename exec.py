import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
from database import carregar_pacientes_db, carregar_medicamentos_db

class JanelaPrincipal:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("MTC - Controle de Medicamentos")
        self.root.geometry("1200x600")
        
        # Frame principal
        main_frame = ctk.CTkFrame(self.root, corner_radius=10)
        main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Frame esquerdo para os botões Pacientes e Medicamentos
        left_frame = ctk.CTkFrame(main_frame)
        left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ns")
        
        btn_pacientes = ctk.CTkButton(left_frame, text="Pacientes", width=150, command=self.abrir_janela_pacientes)
        btn_pacientes.pack(pady=10)
        
        btn_medicamentos = ctk.CTkButton(left_frame, text="Medicamentos", width=150, command=self.abrir_janela_medicamentos)
        btn_medicamentos.pack(pady=10)

        # Frame direito para o TreeView de Medicamentos
        right_frame = ctk.CTkFrame(main_frame)
        right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Configurar o TreeView para exibir os medicamentos
        columns = ("Nome do Medicamento", "Estoque", "Vencimento")
        tree = ttk.Treeview(right_frame, columns=columns, show="headings", height=15)
        tree.pack(fill="both", expand=True)
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=200, anchor=tk.CENTER)

        # Carregar medicamentos do banco de dados
        carregar_medicamentos_db(tree)

        # Configurações de redimensionamento
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)

        self.root.mainloop()

    # Função para abrir a janela de Pacientes
    def abrir_janela_pacientes(self):
        pacientes_janela = ctk.CTkToplevel(self.root)
        pacientes_janela.title("Pacientes")
        pacientes_janela.geometry("1000x600")
        pacientes_janela.transient(self.root)
        pacientes_janela.deiconify()

        # Frame para exibir e manipular os pacientes
        frame_pacientes = ctk.CTkFrame(pacientes_janela)
        frame_pacientes.pack(fill="both", expand=True)

        # Botões para Adicionar, Remover e Editar Pacientes
        btn_adicionar_paciente = ctk.CTkButton(frame_pacientes, text="Adicionar Paciente", command=self.adicionar_paciente)
        btn_adicionar_paciente.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        btn_remover_paciente = ctk.CTkButton(frame_pacientes, text="Remover Paciente", command=self.remover_paciente)
        btn_remover_paciente.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        btn_editar_paciente = ctk.CTkButton(frame_pacientes, text="Editar Paciente", command=self.editar_paciente)
        btn_editar_paciente.grid(row=1, column=2, padx=10, pady=10, sticky="w")

        # Configuração do TreeView para os pacientes
        columns_pacientes = ("Nome", "Idade", "Endereço")
        tree_pacientes = ttk.Treeview(frame_pacientes, columns=columns_pacientes, show="headings", height=15)
        
        for col in columns_pacientes:
            tree_pacientes.heading(col, text=col)
            tree_pacientes.column(col, width=150, anchor=tk.CENTER)

        tree_pacientes.grid(row=0, column=0, padx=10, pady=10, sticky="nsew", columnspan=3)
        frame_pacientes.grid_columnconfigure(0, weight=1)
        
        # Carregar pacientes do banco de dados
        carregar_pacientes_db(tree_pacientes)

    # Função para abrir a janela de Medicamentos
    def abrir_janela_medicamentos(self):
        medicamentos_janela = ctk.CTkToplevel(self.root)
        medicamentos_janela.title("Medicamentos")
        medicamentos_janela.geometry("1000x600")
        medicamentos_janela.transient(self.root)
        medicamentos_janela.deiconify()

        # Frame para exibir e manipular os medicamentos
        frame_medicamentos = ctk.CTkFrame(medicamentos_janela)
        frame_medicamentos.pack(fill="both", expand=True)

        # Botões para Adicionar, Remover e Editar Medicamentos
        btn_adicionar_medicamento = ctk.CTkButton(frame_medicamentos, text="Adicionar Medicamento", command=self.adicionar_medicamento)
        btn_adicionar_medicamento.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        btn_remover_medicamento = ctk.CTkButton(frame_medicamentos, text="Remover Medicamento", command=self.remover_medicamento)
        btn_remover_medicamento.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        btn_editar_medicamento = ctk.CTkButton(frame_medicamentos, text="Editar Medicamento", command=self.editar_medicamento)
        btn_editar_medicamento.grid(row=1, column=2, padx=10, pady=10, sticky="w")

        # Configuração do TreeView para os medicamentos
        columns_medicamentos = ("Nome do Medicamento", "Estoque", "Vencimento")
        tree_medicamentos = ttk.Treeview(frame_medicamentos, columns=columns_medicamentos, show="headings", height=15)
        
        for col in columns_medicamentos:
            tree_medicamentos.heading(col, text=col)
            tree_medicamentos.column(col, width=150, anchor=tk.CENTER)

        tree_medicamentos.grid(row=0, column=0, padx=10, pady=10, sticky="nsew", columnspan=3)
        frame_medicamentos.grid_columnconfigure(0, weight=1)
        
        # Carregar medicamentos do banco de dados
        carregar_medicamentos_db(tree_medicamentos)

    # Funções para manipulação (ações fictícias)
    def adicionar_paciente(self):
        messagebox.showinfo("Adicionar Paciente", "Função de adicionar paciente aqui")
        
    def remover_paciente(self):
        messagebox.showinfo("Remover Paciente", "Função de remover paciente aqui")
        
    def editar_paciente(self):
        messagebox.showinfo("Editar Paciente", "Função de editar paciente aqui")
        
    def adicionar_medicamento(self):
        messagebox.showinfo("Adicionar Medicamento", "Função de adicionar medicamento aqui")
        
    def remover_medicamento(self):
        messagebox.showinfo("Remover Medicamento", "Função de remover medicamento aqui")
        
    def editar_medicamento(self):
        messagebox.showinfo("Editar Medicamento", "Função de editar medicamento aqui")

# Inicializar a aplicação
JanelaPrincipal()

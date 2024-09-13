# recriando a aplicação orientada a objetos
import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
from database import gerardb, conectardb, adicionar_paciente_db, adicionar_medicamento_db, carregar_pacientes_db, carregar_medicamentos_db
class JanelaPrincipal:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("MTC - Controle de Medicamentos")
        self.root.geometry("1200x600")
        
       
    # widgets da janela principal
        main_frame = ctk.CTkFrame(self.root, corner_radius=10)
        main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        left_frame = ctk.CTkFrame(main_frame)
        left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ns")
        btn_pacientes = ctk.CTkButton(left_frame, text="Pacientes", width=150, command=self.abrir_janela_pacientes) 
        btn_pacientes.pack(pady=10)
        btn_medicamentos = ctk.CTkButton(left_frame, text="Medicamentos", width=150, command=self.abrir_janela_medicamentos)
        btn_medicamentos.pack(pady=10)

        right_frame = ctk.CTkFrame(main_frame)
        right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        columns = ("Nome do Medicamento", "Estoque", "Vencimento")
        tree = ttk.Treeview(right_frame, columns=columns, show="headings", height=15)
        tree.pack(fill="both", expand=True)
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=200, anchor=tk.CENTER)

        carregar_medicamentos_db(tree)

        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)
        self.root.mainloop()
    def abrir_janela_pacientes(self):
        pacientes_janela = ctk.CTkToplevel(self.root)
        pacientes_janela.title("Pacientes")
        pacientes_janela.geometry("1000x600")  # Ajustado para permitir o Treeview
        pacientes_janela.transient(self.root)  # Torna a janela sobreposta à principal
        pacientes_janela.deiconify()  # Garante que a janela seja mostrada

        frame_pacientes = ctk.CTkFrame(pacientes_janela)
        frame_pacientes.pack(fill="both", expand=True)

        btn_adicionar_paciente = ctk.CTkButton(frame_pacientes, text="Adicionar Paciente", command=None)
        btn_adicionar_paciente.grid(row=3, column=0, padx=20, pady=10, sticky="se")

        columns_pacientes = ("Nome", "Idade", "Endereço")
        tree_pacientes = ttk.Treeview(frame_pacientes, columns=columns_pacientes, show="headings", height=15)

        for col in columns_pacientes:
            tree_pacientes.heading(col, text=col)
            tree_pacientes.column(col, width=150, anchor=tk.CENTER)

        tree_pacientes.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        frame_pacientes.grid_columnconfigure(1, weight=1)
        carregar_pacientes_db(tree_pacientes)
    def abrir_janela_medicamentos(self):
        pass
JanelaPrincipal()
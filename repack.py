#atualizacao do app com intuito de facilitar o desenvolvimento

from tkinter import *
from customtkinter import *

class JanelaPrincipal:

    def __init__(self):
        
        self.root = CTk()
        self.root.title("MTC - Controle de Medicamentos")
        self.root.geometry("1300x800")
        self.root.minsize(1300, 800)
        

        # Frame lateral
        left_frame = CTkFrame(self.root, fg_color="lightblue", corner_radius=15,height=500)
        left_frame.pack(padx=10, pady=40,side=LEFT,anchor="nw")

        tv_frame=CTkFrame(self.root, fg_color="lightblue", corner_radius=10, height=500)
        tv_frame.pack(fill=X,pady=40)



        self.root.mainloop()



JanelaPrincipal()
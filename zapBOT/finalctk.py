import customtkinter as ctk
from tkinter import *

def botaofoda():
    msg = entryfoda.get("1.0", END)
    labeldokrl.config(text=msg)

janela = Tk()
janela.title("Suamaede4")

entryfoda = ctk.CTkEntry(master=janela, width=120, height=25, corner_radius=10)
entryfoda.place(relx=0.5, rely=0.5, anchor=CENTER)

labeldokrl = ctk.CTkLabel(master=janela, text="", width=120, height=25, corner_radius=8)
labeldokrl.place(relx=0.5, rely=0.5, anchor=CENTER)

botao = ctk.CTkButton(master=janela, corner_radius=10, command=botaofoda)
botao.place(relx=0.5, rely=0.5, anchor=CENTER)

janela.mainloop()
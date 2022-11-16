from tkinter import *
from tkinter import ttk

def sexzzz():
    meupau = "seucu"

janela = Tk()
janela.resizable(False, False)
janela.title("Sua mae teste")

lb = Label(janela, text="Escolha um na lista!")
lb.grid(column=0, row=0, padx=10, pady=10)

stv = StringVar()
cbx = ttk.Combobox(janela, textvariable=stv)
cbx["values"] = ["Sua mae é minha tudo bom?", "Escrevi e sai correndo pnc de quem ta lendo!", "Ai ai ai ai ser bandido é bom demais"]
cbx["state"] = "readonly"
cbx.grid(column=0, row=1, padx=10, pady=10)


def suamae(event):
    meupau = stv.get()
    print (meupau)

cbx.bind("<<ComboboxSelected>>", suamae)


janela.mainloop()
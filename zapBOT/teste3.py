from tkinter import *
from tkinter import ttk


janela = Tk()



def macaco(event):
    brabo = int(lsbx.curselection()[0])
    monk = lsbx.get(brabo)
    print(monk)


lsbx = Listbox(janela, height=10, width=50)
lsbx.grid(column=0, row=0, padx=5, pady=5)
lsbx.bind("<<ListboxSelect>>", macaco)

lsbx.insert(END, "sexo?")
lsbx.insert(END, "Suamae")


janela.mainloop()
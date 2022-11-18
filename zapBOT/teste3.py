from tkinter import *
from tkinter import ttk
import pywhatkit as kit


janela = Tk()



def macaco(event):
    brabo = int(lsbx.curselection()[0])
    monk = lsbx.get(brabo)
    print(monk)
    kit.sendwhatmsg_instantly("55_65999532826", monk)

lsbx = Listbox(janela, height=10, width=50)
lsbx.grid(column=0, row=0, padx=5, pady=5)
lsbx.bind("<<ListboxSelect>>", macaco)

lsbx.insert(END, "sexo?")
lsbx.insert(END, "Suamae")


janela.mainloop()
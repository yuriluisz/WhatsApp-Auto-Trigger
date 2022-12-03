import pywhatkit as kit
from tkinter import *

def envflist():
        numtxt = open("zapBOT/numeros.txt")
        leituranum = numtxt.readlines()
        brabo = int(listafoda.curselection()[0])
        msgzz = listafoda.get(brabo)
        for env in leituranum:
            kit.sendwhatmsg_instantly(f"{env}", msgzz, tab_close= True, close_time=3)
        numtxt.close()

janela = Tk()

botaofoda = Button(janela, text="Sua mae", command=envflist)
botaofoda.grid(column=0, row=0, padx=5, pady=5)

listvarpica = StringVar()
listafoda = Listbox(janela, listvariable=listvarpica, height=10, width=20)
listafoda.grid(column=1, row=0, padx=5, pady=5)

openmsg = open ("zapBOT/mensagens.txt")
leituramsg = openmsg.readlines()

for txt in leituramsg:
    listafoda.insert(END, txt)


janela.mainloop()
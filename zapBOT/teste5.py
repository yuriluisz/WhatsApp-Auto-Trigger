import pywhatkit as kit
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

def teucu():
    imge = filedialog.askopenfilename(initialdir="/", title="Selecione UMA imagem", filetypes=((".JPG","*.jpg*"),(".PNG","*.png*"),("Todos","*.*")))
    msgs = open("zapBOT/numeros.txt")
    numeros = msgs.readlines()
    msgzz = "jvlkejdvblkhevb"
    print(numeros)
    for pau in numeros:
        kit.sendwhats_image(f"{pau}", imge, msgzz, tab_close= True, close_time= 3)


janela = Tk()
janela.geometry("300x200")

botao = Button(janela, text="spdjvbesofhbr", command=teucu)
botao.grid(column=0, row=0, padx=5, pady=5)


janela.mainloop()
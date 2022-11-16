from tkinter import *
from tkinter.ttk import*

janela = Tk()
janela.title("Listbox")
janela.geometry('300x200')


def test(Event):
    # imprime apenas o primeiro elemento
    index = int(lb.curselection()[0])
    value = lb.get(index)

    print(value)


lb = Listbox(janela, height=8)
lb.grid(row=0, column=0)

# Adicionando um elemento à listbox
lb.insert(1, 'PHP')
lb.insert(2, 'Python')
lb.insert(3, 'MySQL')

items = ["JS", "Java", "C++"]

for i in items:
    lb.insert(END, i)

lb.bind('<<ListboxSelect>>', test)

janela.mainloop()
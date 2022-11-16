import pywhatkit as pk
from tkinter import *
from tkinter import ttk

def EnviarMSG():
    try:
        num = inputnum.get("1.0", END)
        msgzz = inputmsg.get("1.0", END)
        pk.sendwhatmsg_instantly(f"{num}", msgzz)
        status.config(text="Status: Mensagem Enviada!")

    except:
        status.config(text="Status: Erro no Envio! verifique o número.")

def selecmsg(event):
    try:
        num = inputnum.get("1.0", END)
        msgzz = selmsg.get()
        pk.sendwhatmsg_instantly(f"{num}", msgzz)
        status.config(text="Status: Mensagem Enviada!")

    except:
        status.config(text="Status: Erro no Envio! verifique o número.")


# Mensagens
msg1 = "Olá, logo logo entraremos em contato!"
msg2 = "Olá, No momento estamos indisponiveis, entraremos em contato o mais rapido possivel em breve"
msg3 = "Olá, E um prazer atender-lo como posso ajudar"

janela = Tk()
janela.title("WhatsApp auto message")
janela.resizable(False, False)

num = Label(janela, text='Insira o nmero de telefone e coloque um "_" apos o DDD ex:55_65...')
num.grid(column=0, row=0, padx=10, pady=0)

inputnum = Text(janela, height=1, width=40)
inputnum.grid(column=0, row=1, padx=10, pady=10)

msg = Label(janela, text="Insira a mensagem que deseja enviar:")
msg.grid(column=0, row=2, padx=10, pady=10)

inputmsg = Text(janela, height=3, width=40)
inputmsg.grid(column=0, row=3, padx=10, pady=10)

selmsg = StringVar()
combox = ttk.Combobox(janela, textvariable=selmsg)
combox["values"] = [msg1, msg2, msg3]
combox["state"] = "readonly"
combox.grid(column=2, row=3, padx=10, pady=10)
combox.bind("<<ComboboxSelected>>", selecmsg)

status = Label(janela, text="Status:")
status.grid(column=0,row=4, padx=10, pady=10)

Enviar = Button(janela, text="Enviar", command=EnviarMSG)
Enviar.grid(column=0, row=5, padx=10, pady=10)

sair = Button(janela, text="Sair", command=janela.destroy)
sair.grid(column=0, row=6, padx=10, pady=10)


janela.mainloop()

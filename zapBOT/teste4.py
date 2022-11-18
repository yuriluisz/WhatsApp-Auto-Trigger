import pywhatkit as pk
from tkinter import *
from tkinter import ttk


# Def do botao de enviar mensagem selecionada
def msgpronta():
    for i in listbox.curselection():
        try:
            num = inputnum.get("1.0", END)
            brabo = int(listbox.curselection()[0])
            msgzz = listbox.get(brabo)
            print(msgzz)
            pk.sendwhatmsg_instantly(f"{num}", msgzz)
            status.config(text="Status: Mensagem Enviada!")
        except:
            status.config(text="Status: Erro no Envio! verifique o numero.")

# Def do botao de enviar mensagem escrita
def EnviarMSG():
    try:
        num = inputnum.get("1.0", END)
        msgzz = inputmsg.get("1.0", END)
        pk.sendwhatmsg_instantly(f"{num}", msgzz)
        status.config(text="Status: Mensagem Enviada!")
    except:
        status.config(text="Status: Erro no Envio! verifique o número.")

def adicionar():
    print("mae?")


# Mensagens
msg1 = "Olá, Logo Logo vamos te responder!"
msg2 = "Olá, No momento estamos indisponiveis, entraremos em contato o mais rapido possivel."
msg3 = "Olá, E um prazer atender-lo como posso ajudar?"
msg4 = "Olá, No momento não estamos atendendo."

mensagens = [msg1, msg2, msg3, msg4]

# Interface
janela = Tk()
janela.title("WhatsApp auto message")
janela.resizable(False, False)

# Inserir Numero de telefone
num = Label(janela, text='Insira o nmero de telefone e coloque um "_" apos o DDD ex:55_65...')
num.grid(column=0, row=0, padx=10, pady=0)

inputnum = Text(janela, height=1, width=40)
inputnum.grid(column=0, row=1, padx=10, pady=10)

# Inserir Mensagem
msg = Label(janela, text="Insira a mensagem que deseja enviar:")
msg.grid(column=0, row=2, padx=10, pady=10)

inputmsg = Text(janela, height=5, width=40)
inputmsg.grid(column=0, row=3, padx=10, pady=10)

# Escolher mensagem predefinida
listbox = Listbox(janela, height=5, width=40)
listbox.insert(END, msg1)
listbox.insert(END, msg2)
listbox.insert(END, msg3)
listbox.insert(END, msg4)
listbox.grid(column=1, row=3, padx=10, pady=10)

# Status do Envio
status = Label(janela, text="Status:")
status.grid(column=1,row=0, padx=10, pady=10)

# Botao Enviar mensagem pronta
Enviarpronta = Button(janela, text="Enviar mensagem selecionada", command=msgpronta)
Enviarpronta.grid(column=1, row=4, padx=10, pady=10)

# Botao Enviar mensagem escrita
Enviar = Button(janela, text="Enviar mensagem escrita", command=EnviarMSG)
Enviar.grid(column=0, row=4, padx=10, pady=10)

# Botao Adicionar mensagem escrita
adc = Button(janela, text="Adicionar Mensagem", command=adicionar)
adc.grid(column=0, row=5, padx=10, pady=10)

# Botao Sair
sair = Button(janela, text="Sair", command=janela.destroy)
sair.grid(column=1, row=5, padx=10, pady=10)


janela.mainloop()

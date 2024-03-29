"""
Este projeto foi feito com o intuito de automatizar o disparo de mensagens em massa no WhatsApp.
Está versão não representa sua versão final, tudo ainda está em teste e pode ser melhorado futuramente!
--------------------- WhatsApp Auto Trigger by: https://github.com/yuriluisz --------------------------
"""

# Importar bibliotecas necessarias para o funcionamento do codigo
from tkinter import *
from tkinter import filedialog, ttk
from tkinter.messagebox import showinfo
import pywhatkit as pk

# Abrir o arquivos de mensagens
msgtxt = open("mensagens.txt")
leituramsg = msgtxt.readlines()

# Def do botao de enviar mensagem selecionada
def msgpronta():
    for i in listbox.curselection():
        try:
            num = inputnum.get("1.0", END)
            brabo = int(listbox.curselection()[0])
            msgzz = listbox.get(brabo)
            pk.sendwhatmsg_instantly(f"{num}", msgzz, tab_close= True, close_time=3)
            status.config(text="Status: Mensagem Enviada!")
        except:
            status.config(text="Status: Erro no Envio! verifique o numero.")

# Def do botao de enviar mensagem escrita
def EnviarMSG():
    try:
        num = inputnum.get("1.0", END)
        msgzz = inputmsg.get("1.0", END)
        pk.sendwhatmsg_instantly(f"{num}", msgzz, tab_close= True, close_time=3)
        status.config(text="Status: Mensagem Enviada!")
    except:
        status.config(text="Status: Erro no Envio! verifique o número.")

# Def do botao de escolher imagem
def fndimg():
    try:       
        imge = filedialog.askopenfilename(initialdir="/", title="Selecione UMA imagem", filetypes=((".JPG","*.jpg*"),(".PNG","*.png*"),("Todos","*.*")))
        msgs = open("numeros.txt")
        numeros = msgs.readlines()
        msgzz = inputmsg.get("1.0", END)
        print(numeros)
        for pau in numeros:
            pk.sendwhats_image(f"{pau}", imge, msgzz, tab_close= True, close_time= 3)
        status.config(text="Status: Erro no envio! verifique o número.")
    except:
        status.config(text="Status: Erro no Envio! verifique o número.")
        print(imge)

# Def do botao de Como usar?
def hwtuse():
    showinfo(
        title="Como usar?",
        message="Numero: Sempre que for inserir o numero coloque da seguinte maneira 55_65xxxxxxxx com um _ depois do DDD \n Imagens: Imagens precisam ter o numero já inserido, caso contrario nao sera enviada, pois o programa envia automaticamente apos escolher a imagem. Também é possivel enviar imagens com mensagens, basta escrever a mensagem e escolher a imagen (nao funciona com mensagem pronta)")

# Def para adicionar mensagens a lista
def adcmensg():
    try:
        msgstxt = open("mensagens.txt", "a")
        mensagensfodas = inputmsg.get("1.0", END)
        msgstxt.write(mensagensfodas)
        msgtxt.close()
        status.config(text="Status: A mensagem foi adicionada a lista!")
    except:
        status.config(text="Status: A mensagem não foi adicionada.")

# Def para excluir mensagens da lista
def excmsg():
    try:
        msgstxt = open("mensagens.txt", "w")
        msgstxt.write("")
        msgstxt.close()
        status.config(text="Status: Todas as mensagens da lista foram excluidas!")
    except:
        status.config(text="Status: As mensagens não foram excluidas.")

# Def para adicionar numero a lista
def adcnumero():
    try:
        numtxt = open("numeros.txt", "a")
        lernumin = inputnum.get("1.0", END)
        numtxt.write(lernumin)
        numtxt.close()
        status.config(text="Status: Numero Adicionado!")
    except:
        status.config(text="Status: O Numero não foi Adicionado.")

# Def para excluir numero da lista
def excnumero():
    try:
        numtxt = open("numeros.txt", "w")
        numtxt.write("")
        numtxt.close()
        status.config(text="Status: Todos os numeros da lista foram excluidos!")
    except:
        status.config(text="Status: Os numeros não foram excluidos")

# Def para enviar mensagem escrita para lista
def envflwrite():
    try:
        numtxt = open("numeros.txt")
        leituranum = numtxt.readlines()
        msgzz = inputmsg.get("1.0", END)
        for env in leituranum:
            pk.sendwhatmsg_instantly(f"{env},", msgzz, tab_close= True, close_time=3)
        numtxt.close()
        status.config(text="Status: Mensagem Enviada!")
    except:
        status.config(text="Status: Erro no Envio! verifique o número.")

# Def para enviar mensagem selecionada para lista
def envflist():
    try:
        numtxt = open("numeros.txt")
        leituranum = numtxt.readlines()
        brabo = int(listbox.curselection()[0])
        msgzz = listbox.get(brabo)
        for env in leituranum:
            pk.sendwhatmsg_instantly(f"{env}", msgzz, tab_close= True, close_time=3)
        numtxt.close()
        status.config(text="Status: Mensagem Enviada!")
    except:
        status.config(text="Status: Erro no Envio! verifique o número.")

# Interface
janela = Tk()
janela.configure(bg="#BFBFBF")
janela.title("WhatsApp auto message")
janela.resizable(False, False)

# Criação de frames
frame0 = Frame(janela, bg="#BFBFBF")
frame0.grid(column=0, row=0)

frame1 = Frame(janela, bg="#BFBFBF")
frame1.grid(column=1, row=0)

frame2 = Frame(janela, bg="#BFBFBF")
frame2.grid(column=2, row=0)

# Inserir Numero de telefone
num = Label(frame1, text='Insira o numero de telefone:', bg="#BFBFBF")
num.grid(column=1, row=0, padx=1, pady=1)

inputnum = Text(frame1, height=1, width=40)
inputnum.grid(column=1, row=1, padx=5, pady=5)

# Inserir Mensagem
msg = Label(frame1, text="Insira a mensagem:", bg="#BFBFBF")
msg.grid(column=1, row=2, padx=1, pady=1)

inputmsg = Text(frame1, height=15, width=40)
inputmsg.grid(column=1, row=3, padx=5, pady=5)

# Escolher mensagem predefinida
listvar = StringVar()
listbox = Listbox(frame2, listvariable=listvar, height=25, width=50)

for txt in leituramsg:
    listbox.insert(END, txt)
listbox.grid(column=2, row=0, padx=10, pady=10)

# Status do Envio
status = Label(frame1 , text="Status:", bg="#BFBFBF")
status.grid(column=1,row=4, padx=5, pady=5)

# Botao Enviar mensagem pronta
Enviarpronta = Button(frame0, text="Enviar mensagem selecionada", command=msgpronta, width=25, bg="#FFFFFF")
Enviarpronta.grid(column=0, row=0, padx=5, pady=5)

# Botao Enviar mensagem escrita
Enviar = Button(frame0, text="Enviar mensagem escrita", command=EnviarMSG, width=25, bg="#FFFFFF")
Enviar.grid(column=0, row=1, padx=5, pady=5)

# Botao Como usar?
adc = Button(frame0, text="Como usar?", command=hwtuse, width=25, bg="#FFFFFF")
adc.grid(column=0, row=12, padx=5, pady=5)

# Botao Sair
sair = Button(frame0, text="Sair", command=janela.destroy, width=25, bg="#FFFFFF")
sair.grid(column=0, row=13, padx=5, pady=5)

# Botao para escolher uma imagem
slcimg = Button(frame0, text="Escolher imagem", command=fndimg, width=25, bg="#FFFFFF")
slcimg.grid(column=0, row=6, padx=5, pady=5)

# Botao para adicionar mensagem a lista
adcmsg = Button(frame0, text="Adicionar mensagem", command=adcmensg, width=25, bg="#FFFFFF")
adcmsg.grid(column=0, row=7, padx=5, pady=5)

# Botao para excluir todas as mensagens da lista
delist = Button(frame0, text="Excluir mensagens", command=excmsg, width=25, bg="#FFFFFF")
delist.grid(column=0, row=9, padx=5, pady=5)

# Botao para adicionar um numero na lista
adcnum = Button(frame0, text="Adicionar Numero", command=adcnumero, width=25, bg="#FFFFFF")
adcnum.grid(column=0, row=10, padx=5, pady=5)

# Botao para excluir um numero da lista
excnum = Button(frame0, text="Excluir Numeros", command=excnumero, width=25, bg="#FFFFFF")
excnum.grid(column=0, row=11, padx=5, pady=5)

# Botao para enviar mensagem escrita para a lista de numeros
envescrita = Button(frame0, text="Enviar para lista (escrita)",command=envflwrite, width=25, bg="#FFFFFF")
envescrita.grid(column=0, row=5, padx=5, pady=5)

# Botao para enviar mensagem selecionada da lista para a lista de numeros
envselect = Button(frame0, text="Enviar para lista (selec)",command=envflist, width=25, bg="#FFFFFF")
envselect.grid(column=0, row=3, padx=5, pady=5)

janela.mainloop()

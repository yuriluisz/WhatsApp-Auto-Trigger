import customtkinter
import tkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("WhatsApp auto messager")
        self.geometry("800x600")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.btnframe = customtkinter.CTkFrame(self)
        self.btnframe.grid(row=0, column=0, padx=5, pady=(5, 0), sticky="nsw")

        self.numero = customtkinter.CTkEntry(self)
        self.numero.grid(row=1, column=1, padx=150, pady=10, sticky="nswe")
        
        self.labeltit1 = customtkinter.CTkLabel(self.btnframe, text="Opções", font=(format, 25))
        self.labeltit1.grid(row=0, column=0, padx=5, pady=0, sticky="n")
        
        self.button1 = customtkinter.CTkButton(self.btnframe, text="Manda um oi pra mim", command=self.mandaumoi)
        self.button1.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        
        self.button2 = customtkinter.CTkButton(self.btnframe, text="ele vai te mandar", command=self.mandaumoi)
        self.button2.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        
        self.titulogamer = customtkinter.CTkLabel(self, text="WhatsApp auto messager", font=(format, 30))
        self.titulogamer.grid(row=0, column=1, padx=150, pady=5, sticky="nw")

        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)
        

    def mandaumoi(self):
        print("Ola")

    def button_callback(self):
        print("botao muito legal")
        
app = App()
app.mainloop()
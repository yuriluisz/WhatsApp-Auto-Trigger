import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("minimal example app")
        self.minsize(100, 120)

        self.label = customtkinter.CTkLabel(master=self, text="A mensagem aparecera aqui!")
        self.label.pack(padx=10, pady=10)

        self.cudoce = customtkinter.CTkEntry(master=self, width=120, height=3)
        self.cudoce.pack(padx=10, pady=10,)

        self.button = customtkinter.CTkButton(master=self, command=self.button_callback)
        self.button.pack(padx=10, pady=10)



    def button_callback(self):
        msg = self.cudoce.get()
        self.label.configure(text=msg)



if __name__ == "__main__":
    app = App()
    app.mainloop()
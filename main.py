import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Starter App")
        self.geometry("400x250")
        self.grid_columnconfigure((0, 1), weight=1)

        self.text = ctk.CTkLabel(self, text="Starter App")
        self.text.grid(column=0, row=0, columnspan=2)

        self.virusButton = ctk.CTkButton(self, text="Virus", command=self.button_callback)
        self.virusButton.grid(column=0, row=1, columnspan=1)

    def button_callback(self):
        print("button pressed")
        VirusMsgBox().mainloop()



class VirusMsgBox(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Warning!")
        self.geometry("320x100")

        self.text = ctk.CTkLabel(self, text="Do you really want to continue?")
        self.text.grid(column=0, row=0, columnspan=2)
        self.text = ctk.CTkLabel(self, text="This program can harm your PC! Do not run it on real PC!")
        self.text.grid(column=0, row=2, columnspan=2)

        self.button = ctk.CTkButton(self, text="my button")
        self.button.grid(column=0, row=10, columnspan=2)

app = App()
app.mainloop()
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

from modules.users.data.external.usecases.authentication import Authentication
from views.telaMain import TelaMain


class Application:
    def __init__(self, master=None):

        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        imagem = PhotoImage(file="fingerprint.png")
        self.imagem = Label(root, image=imagem)
        self.imagem.imagem = imagem
        self.imagem.pack()

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()

        self.mensagem = Label(self.quartoContainer,
                              text="", font=self.fontePadrao)
        self.mensagem.pack()

    def verificaSenha(self):
        filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select a File",
                                              filetypes=(("Text files",
                                                          "*.tif"),
                                                         ("all files",
                                                          "*.*")))

        try:
            user = Authentication.auth(filename)

            TelaMain.abrirTela(user)

        except Exception as error:
            messagebox.showerror("Error", error)


root = Tk()
root.title("Biometria")
Application(root)
root.mainloop()

import tkinter as t
from tkinter import messagebox


class TelaMain():

    @staticmethod
    def abrirTela(user):
        janelaMain = t.Toplevel()
        janelaMain.title("Tela Principal")
        messagebox.showinfo("Informativo", "Ola " +
                            user['nome'] + "\nSeja bem vindo")

from tkinter import *
import random

cor1 = "#3d3d3d" # Preta
cor2 = "#fafcff" # Branca
cor3 = "#21c25c" # Verde
cor4 = "#eb463b" #Vermelha
cor5 = "#dedcdc" #Cinza
cor6 = "#3080f0" #Azul

Sorteio = random.randint(1,10)
cont = 0
tent = 5
fundo = cor5
root = Tk()
root.geometry("320x180")


class JogoDeAdvinhacao:
    def __init__(self, master=None):

        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()


        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()
        self.terceiroConteiner = Frame(master)
        self.terceiroConteiner.pack()

        self.contador = Label(self.segundoContainer, text=0, font=("Arial", "12", "bold"), fg=cor4)
        self.contador.pack()

        self.title = Label(self.primeiroContainer, text="Jogo de Adivinhação")
        self.title["font"] = ("Arial", "20", "bold")
        self.title.pack()


        self.ChuteLabel = Label(self.segundoContainer, text="Palpite",font= ("Arial", "15", "bold"))
        self.ChuteLabel.pack(side=LEFT)

        self.chute = Entry(self.segundoContainer)
        self.chute["width"] = 30
        self.chute["font"] = "Arial", "15", "bold"
        self.chute.pack(side=LEFT)

        self.verificar = Button(self.terceiroConteiner)
        self.verificar["text"] = "CHUTAR"
        self.verificar["font"] = ("Arial", "12")
        self.verificar["command"] = self.Verificacao
        self.verificar.pack(pady=5)

        self.mensagem = Label(self.terceiroConteiner, text="", font=("Arial", "15", "bold"))
        self.mensagem.pack()

    def Verificacao(self):
        global tent
        global cont
        tent-=1
        cont += 1
        self.contador["text"] = tent
        if tent == 0:
            self.mensagem["text"] = "Suas tentativas acabaram"
            self.Verificacao(root.destroy())
        Chute = int(self.chute.get())
        if Chute == Sorteio:
            self.mensagem["text"] = "Acertou apos {} tentativas".format(cont)
        elif Chute > Sorteio:
            self.mensagem["text"] = "Seu chute foi maior"
        elif Chute < Sorteio:
            self.mensagem["text"] = "Seu chute foi menor"




JogoDeAdvinhacao(root)
root.mainloop()




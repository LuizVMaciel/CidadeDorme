from tkinter import *
janela = Tk()
janela.title('Cidade Dorme')
janela.configure(background = "#424242")
botaoJogar = Button(janela, text = 'Jogar')
botaoJogar.place(relx = 0.25, rely = 0.75, relwidth = 0.50, relheight = 0.1)
textoBemVindo = Label(janela, text = 'Bem vindo ao Cidade Dorme!')
textoBemVindo.place(relx = 0.1, rely = 0.25, relwidth = 0.8, relheight = 0.1)
janela.mainloop()
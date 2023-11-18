from tkinter import *

#Cria a janela
janela = Tk()

#Titulo desta janela
janela.title("Conversor")

#Tamanho da janela
janela.geometry('850x850')

#Cria o rótulo da janela com as config desejadas
rotulo = Label(janela, text="Número Decimal: ", font=("Arial",12))
rotulo.place(relx=0.26, rely=0.35, anchor=CENTER)

rotulo = Label(janela, text="Resultado: ", font=("Arial",12))
rotulo.place(relx=0.26, rely=0.40, anchor=CENTER)

def clique():
    a =  caixa_texto.get()

    caixa_texto_2.insert(0,)

def clique_hex():
    a =  caixa_texto.get()

    caixa_texto_2.insert(0,)

def clique_oct():
    a =  caixa_texto.get()

    caixa_texto_2.delete("0", "end")

#Criação de caixa de texto
caixa_texto = Entry(janela, width=30, font=("Arial", 12))
#Posicionando caixa de texto
caixa_texto.place(relx=0.5, rely=0.35, anchor=CENTER)

#Criação de caixa de texto
caixa_texto_2 = Entry(janela, width=30, font=("Arial", 12))
#Posicionando caixa de texto
caixa_texto_2.place(relx=0.5, rely=0.40, anchor=CENTER)

#Criação do obj botão
#Comand chama a função definida acima
btn = Button(janela, text="Binário", command=clique)
btn_2 = Button(janela, text="Hexadecimal", command=clique_hex)
btn_3 = Button(janela, text="Octal", command=clique_oct)
#Posicionamento do obj botão
btn.place(relx=0.4, rely=0.5, anchor=CENTER)
btn_2.place(relx=0.5, rely=0.5, anchor=CENTER)
btn_3.place(relx=0.6, rely=0.5, anchor=CENTER)

#Função de loop para manter a janela aberta
janela.mainloop()
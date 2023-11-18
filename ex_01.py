from tkinter import *

#Cria a janela
janela = Tk()

#Titulo desta janela
janela.title("Teste GUI")

#Tamanho da janela
janela.geometry('850x850')

#Cria o rótulo da janela com as config desejadas
rotulo = Label(janela, text="Some dois valores", font=("Arial",12))

#config de onde o texto vai aparecer na tela
#podemos usar valores fixos com as cord x e y
#E valores relativos com relx e rely
rotulo.place(relx=0.5, rely=0.25, anchor=CENTER)

#Função definida para ser chamada ao clicar no botão
def clique():
    #Pega o valor definido no obj caixa_texto
    a =  caixa_texto.get()
    b =  caixa_texto_2.get()
    #Altera o valor de text no elemento rotulo
    caixa_texto_3.insert(0,(int(a)+int(b)))

#Criação de caixa de texto
caixa_texto = Entry(janela, width=60, font=("Arial", 12))
#Posicionando caixa de texto
caixa_texto.place(relx=0.5, rely=0.35, anchor=CENTER)

#Criação de caixa de texto
caixa_texto_2 = Entry(janela, width=60, font=("Arial", 12))
#Posicionando caixa de texto
caixa_texto_2.place(relx=0.5, rely=0.40, anchor=CENTER)

#Criação de caixa de texto
caixa_texto_3 = Entry(janela, width=60, font=("Arial", 12))
#Posicionando caixa de texto
caixa_texto_3.place(relx=0.5, rely=0.45, anchor=CENTER)

#Criação do obj botão
#Comand chama a função definida acima
btn = Button(janela, text="Clique aqui", command=clique)
#Posicionamento do obj botão
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

#Função de loop para manter a janela aberta
janela.mainloop()
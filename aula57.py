from tkinter import *

#Introdução aos elementos básicos

app = Tk()
#Título da Janela
app.title("CFB Crusos")
#Tamanho da janela
app.geometry("500x300")
#Configurações da janela
app.configure(background="#008")
#Como inserir os elementos na janela
txt1 = Label(app, text="Curso de Python", background="#ff0", foreground="#000")
txt1.place(x=10, y=10, width=150, height=30)
'''
Quando usamos o .place() temos que definir o local na posção 'x' e 'y' da nossa janela
para contornar isso e tornar a distribuição dos elementos mais organizada e fácil
podemos usar o .pack() que por sua vez é usando junto com o container
'''
#Variáveis de texto
vtxt = "Módulo Tkinter"
vbg = "#ff0"
vfg= "#000"
txt2 = Label(app, text=vtxt, bg=vbg, fg=vfg)
txt2.pack(ipadx=20, ipady=20, padx=5, pady=5, side="top", fill=X, expand=True)
'''
Usamos o ipadx e ipady no contesto do Label para criar um espaço entre
o texto e o próprio elemento do Label. Onde esses elementos podem ou não
ser expansivos sendo definidos por fill e expand.

padx e pady é o espaço entre a janela e o elemento
'''

app.mainloop()
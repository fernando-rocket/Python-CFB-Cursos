from tkinter import *

def semComando():
    print("-----")


app = Tk() # Settings básicos
app.title("Fernando Host")
app.geometry("500x500")
app.configure(bg="#dde")

barraDeMenus = Menu(app) #Criando o Menu
menuContatos = Menu(barraDeMenus, tearoff=0)
menuContatos.add_command(label="Novo", command=semComando)
menuContatos.add_command(label="Pesquisar", command=semComando)
menuContatos.add_command(label="Delete", command=semComando)
menuContatos.add_separator()
menuContatos.add_command(label="Fechar", command=app.quit)

menuManutencao = Menu(barraDeMenus, tearoff=0)
menuManutencao.add_command(label="Banco de dados", command=semComando)

menuSobre = Menu(barraDeMenus, tearoff=0)
menuSobre.add_command(label="Sobre Mim", command=semComando)

barraDeMenus.add_cascade(label="Contatos", menu=menuContatos)
barraDeMenus.add_cascade(label="Manutenção", menu=menuManutencao)
barraDeMenus.add_cascade(label="Sobre", menu=menuSobre)

app.config(menu=barraDeMenus)

app.mainloop() #Comando para a janela aparecer

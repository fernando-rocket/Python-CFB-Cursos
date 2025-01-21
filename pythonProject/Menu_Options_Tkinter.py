from tkinter import *

def showinfo():
    print(var_esporte.get())

app = Tk()
app.title("Menu Options FGS")
app.geometry("500x500")
app.configure(bg="white")

lb_esportes = Label(app, text="Esportes")
lb_esportes.pack()

listaEsportes=["Futebol", "Vôlei", "Basquete"]
var_esporte = StringVar()
var_esporte.set("Selecione um Esporte")

op_esportes = OptionMenu(app, var_esporte, *listaEsportes)
op_esportes.pack()

btn = Button(app, text="Esporte Selecionado", command=showinfo)
btn.pack(pady=30)
app.mainloop()

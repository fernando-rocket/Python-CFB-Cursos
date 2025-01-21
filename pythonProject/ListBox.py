from tkinter import *
from tkinter import messagebox


def add_sport():
    if new_sport.get() != "":
        listBox_esportes.insert(END, new_sport.get())
    else:
        messagebox.showinfo(title="Informação", message="Escreva Algo")


def show_list():
    print(listBox_esportes.get(0, END))


def selectedsport():
    print(listBox_esportes.get(ACTIVE))


app = Tk()
app.title("Fernando ListBox")
app.geometry("500x500")
app.configure(bg="#efede9")

listBox_esportes = Listbox(app) # Criando a ListBox
listBox_esportes.pack()

listaEsportes = ["Futebol", "Vôlei", "Basquete"] # Criando os itens da lista
for esporte in listaEsportes: # Inserindo os itens na ListBox
    listBox_esportes.insert(END, esporte)

new_sport = Entry(app)
new_sport.pack(pady=10)

btn = Button(app, text="Adicionar", command=add_sport)
btn.pack()

btn2 = Button(app, text="Mostrar Lista", command=show_list)
btn2.pack()

btn3 = Button(app, text="Mostrar Esportes", command=selectedsport)
btn3.pack()

app.mainloop()

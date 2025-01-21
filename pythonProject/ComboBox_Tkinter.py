from tkinter import *
from tkinter import ttk

def showsport():
    print(cb_esportes.get())
    res_label["text"] = cb_esportes.get()

app = Tk()
app.title("Fernando ComboBox")
app.geometry("300x300")
app.configure(bg="#efede9")

listaEsportes = ["Futebol", "Vôlei", "Basquete"]
label_esportes = Label(app, text="Esportes")
label_esportes.pack(pady=10)

cb_esportes = ttk.Combobox(app, values=listaEsportes)
cb_esportes.set("Futebol")
cb_esportes.pack()

btn = Button(app, text="Mostrar Esporte", command=showsport)
btn.pack()

res_label = Label(app, text="")
res_label.pack()

app.mainloop()
